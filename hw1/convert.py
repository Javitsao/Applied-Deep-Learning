import json
import sys

if len(sys.argv) != 2:
    print("Usage: python convert.py [target_json_file]")
    sys.exit(1)

# Get the target JSON file from the command-line argument
target_json_file = sys.argv[1]

# Read the original JSON file
with open(target_json_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Create a dictionary to store the converted data
converted_data = []

# Load the context data from context.json
with open('context.json', 'r', encoding='utf-8') as context_file:
    context_data = json.load(context_file)

# Function to map "relevant" to "context"
def get_context(relevant):
    if relevant >= 0 and relevant < len(context_data):
        return context_data[relevant]
    else:
        return ""

# Determine "relevant" for test.json from test_output.txt
if target_json_file == 'test.json':
    relevant_indices = []  # Create a list to store relevant indices
    with open('test_output.txt', 'r') as test_output_file:
        for line in test_output_file:
            relevant_indices.append(int(line.strip()))
else:
    relevant_indices = None

# Loop through the original data and perform the conversion
for index, item in enumerate(data):
    if target_json_file == 'test.json':
        # For test.json, "relevant" comes from test_output.txt
        relevant_index = relevant_indices[index]
        relevant = item["paragraphs"][relevant_index]
        answer_start = [0]  # For test.json, set answer_start to 0
        answer_text = [""]  # For test.json, set text to an empty string
    else:
        # For other files, use "relevant" from the JSON data
        relevant = item["relevant"]
        answer_start = [item["answer"]["start"]]
        answer_text = [item["answer"]["text"]]

    converted_item = {
        "id": item["id"],
        "question": item["question"],
        "context": get_context(relevant),  # Map "relevant" to "context"
        "answers": {
            "answer_start": answer_start,
            "text": answer_text
        }
    }
    converted_data.append(converted_item)

# Generate the output JSON file name
output_file_name = "converted_" + target_json_file

# Write the converted data to the output JSON file
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    json.dump(converted_data, output_file, ensure_ascii=False, indent=2)

print(f"Conversion complete. Converted data saved in {output_file_name}")
