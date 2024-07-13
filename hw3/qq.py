import json
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainer,
    TrainingArguments,
    BitsAndBytesConfig,
    Seq2SeqTrainingArguments,
)
from utils import (
    get_bnb_config,
    get_prompt,
)
from peft import (
    prepare_model_for_kbit_training,
    LoraConfig,
    get_peft_model,
    PeftModel
)
bnb_config = get_bnb_config() # return a BitsAndBytesConfig

def prepare_training_data(file_path, tokenizer):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    instructions = [get_prompt(x["instruction"]) for x in data]
    outputs = [x["output"] for x in data]

    # Tokenize data
    tokenized_instructions = tokenizer(instructions, add_special_tokens=False)
    tokenized_outputs = tokenizer(outputs, add_special_tokens=False)

    train_dataset = list(zip(tokenized_instructions, tokenized_outputs))
    
    # train_dataset = list(zip(
    #     tokenized_instructions.input_ids,
    #     tokenized_instructions.attention_mask,
    #     tokenized_outputs.input_ids,
    #     tokenized_outputs.attention_mask,
    # ))

    return train_dataset

def train_model(model_name_or_path, train_dataset, training_args):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        quantization_config=bnb_config
    )
    peft_config = LoraConfig(
                r=8,
                lora_alpha=16,
                lora_dropout=0.05,
                bias="none",
                task_type="CAUSAL_LM",
            )
    model = get_peft_model(model, peft_config)
    model = prepare_model_for_kbit_training(model)

    #data_collator = DataCollatorForSeq2Seq(tokenizer, pad_to_multiple_of=None)

    trainer = Seq2SeqTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=train_dataset,
        #data_collator=data_collator,
        args=training_args,
    )
    
    trainer.train()
    return model

if __name__ == "__main__":
    train_file_path = "train.json"
    model_name = "Taiwan-LLM-7B-v2.0-chat"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    training_args = Seq2SeqTrainingArguments(
        output_dir="model_v1",
        num_train_epochs=3,
        per_device_train_batch_size=1,
        full_determinism=True,
        fp16=True,
        optim='paged_adamw_32bit',
        seed=42,
        gradient_accumulation_steps=16,
        learning_rate=1e-4,
        #logging_steps=1,
        # Add any other necessary training arguments
    )

    train_dataset = prepare_training_data(train_file_path, tokenizer)

    # Update collate_fn to format the data for Seq2SeqTrainer
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=1)

    train_model(model_name, train_dataset, training_args)



    # Save the quantized model
    trained_model.save_pretrained("model_v1_quantized")
