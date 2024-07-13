import csv
import json

# Read the data from the text file and replace single quotes with double quotes
with open('prediction.txt', 'r', encoding='utf-8') as text_file:
    text_data = text_file.read()
    corrected_data = text_data.replace("'", '"')

# Load the corrected data as JSON
data = json.loads(corrected_data)

# Specify the output CSV file
#csv_file = 'prediction.csv'

# Write the data to the CSV file with 'id' and 'answer' as titles
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'answer']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for item in data:
        writer.writerow({'id': item['id'], 'answer': item['prediction_text']})

print(f'Data has been converted to data.csv.')
