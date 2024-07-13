import json

# Load the train.json and context.json files
with open('train.json', 'r', encoding='utf-8') as train_file:
    train_data = json.load(train_file)

with open('context.json', 'r', encoding='utf-8') as context_file:
    context_data = json.load(context_file)

# Create a mapping of paragraph numbers to paragraphs from context.json
paragraph_mapping = {str(i): paragraph for i, paragraph in enumerate(context_data)}

# Iterate through the train.json data and update the fields
new_train_data = []
for item in train_data:
    updated_item = {
        "fold-ind": item['id'],
        "sent1": item['question'],
        "sent2": "",  # Add a "sent2" field with an empty string
    }
    for i, paragraph_num in enumerate(item['paragraphs']):
        updated_item[f"ending{i}"] = paragraph_mapping[str(paragraph_num)]
    
    # Calculate the label based on the position of "relevant" within "paragraphs"
    relevant_position = item['paragraphs'].index(item['relevant']) if item['relevant'] in item['paragraphs'] else -1
    updated_item["label"] = relevant_position
    
    new_train_data.append(updated_item)

# Save the new data to a data.json file
with open('train_data.json', 'w', encoding='utf-8') as output_file:
    json.dump(new_train_data, output_file, ensure_ascii=False, indent=4)

print("train.json  =========>  train_data.json.")
