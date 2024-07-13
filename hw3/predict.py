import json
import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from utils import get_prompt, get_bnb_config
import argparse

def predict(input_text, model, tokenizer):
    prompt = get_prompt(input_text)
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        predict_results = model.generate(**inputs)

    predictions = tokenizer.decode(predict_results[0], skip_special_tokens=True)
    return predictions

def process_data(input_data, model, tokenizer):
    predictions = []
    for entry in input_data:
        instruction_id = entry["id"]
        instruction_text = entry["instruction"]

        output_text = predict(instruction_text, model, tokenizer)
        assistant_response = re.split(r'ASSISTANT:', output_text)[-1].strip()

        print(assistant_response)
        
        predictions.append({
            "id": instruction_id,
            "output": assistant_response
        })
    return predictions

def main():
    parser = argparse.ArgumentParser(description='Process input file using a specified model')
    parser.add_argument('--base_model_path', type=str, help='Path to the base model')
    parser.add_argument('--peft_path', type=str, help='Path to the PEFT checkpoint')
    parser.add_argument('--test_data_path', type=str, help='Path to the test data JSON file')
    parser.add_argument('--output_path', type=str, help='Path to save predictions JSON file')
    args = parser.parse_args()

    model_name = args.base_model_path
    input_file = args.test_data_path
    output_file = args.output_path

    bnb_config = get_bnb_config()
    #tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        quantization_config=bnb_config
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    peft_path = args.peft_path
    model = PeftModel.from_pretrained(model, peft_path)
    predictions = process_data(data, model, tokenizer)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(predictions, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
