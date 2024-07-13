import json
import sys

if len(sys.argv) != 3:
    print("Usage: python jsonl_to_json.py input.jsonl output.json")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

json_objects = []

# Read the JSONL file and parse each line as a JSON object
with open(input_file, "r") as file:
    for line in file:
        try:
            json_obj = json.loads(line)
            # Add 'title' field with an empty string to each JSON object
            json_obj['title'] = ''
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            print(f"Skipping invalid JSON line: {line}")

# Write the JSON objects to a single JSON file
with open(output_file, "w") as output:
    json.dump(json_objects, output, indent=4)

print(f"Converted {input_file} to {output_file}")
