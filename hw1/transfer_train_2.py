import json

# Load the train.json and context.json files
with open('train.json', 'r', encoding='utf-8') as train_file:
    train_data = json.load(train_file)

with open('context.json', 'r', encoding='utf-8') as context_file:
    context_data = json.load(context_file)

# Iterate through the train.json data, update the "relevant" field, and delete "paragraphs"
for item in train_data:
    item['context'] = context_data[item['relevant']]
    del item['paragraphs']
    del item['relevant']

    # Update "answer" to "answers" and wrap content in square brackets
    item['answers'] = {
        "text": [item['answer']['text']],
        "answer_start": [item['answer']['start']]
    }
    del item['answer']

# Save the updated data to a data.json file
with open('train_data_2.json', 'w', encoding='utf-8') as output_file:
    json.dump(train_data, output_file, ensure_ascii=False, indent=4)
 
print("train_data.json  =========>  train_data_2.json.")
