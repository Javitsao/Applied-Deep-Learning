import json

# Load the train.json and context.json files
with open('test.json', 'r', encoding='utf-8') as train_file:
    train_data = json.load(train_file)

with open('context.json', 'r', encoding='utf-8') as context_file:
    context_data = json.load(context_file)

# Read the input list from a file
with open('test_data_2_input', 'r') as input_list_file:
    input_list = [int(line.strip()) for line in input_list_file]

# Iterate through the train.json data, update the "context" field based on input, and delete "paragraphs"
for item, selected_paragraph in zip(train_data, input_list):
    if selected_paragraph < len(item['paragraphs']):
        item['context'] = context_data[item['paragraphs'][selected_paragraph]]
    del item['paragraphs']
    item['answers'] = {
        "text": [""],
        "answer_start": [0]
    }

# Save the updated data to a data.json file
with open('test_data_2.json', 'w', encoding='utf-8') as output_file:
    json.dump(train_data, output_file, ensure_ascii=False, indent=4)

print("test_data.json  =========>  test_data_2.json.")
