import pandas as pd

# List of CSV file paths
csv_files = ["data_59487666.csv", "data_9487.csv", "data_10902027.csv", "data_649.csv", "data_34595.csv", "data_592081.csv"]

# Initialize an empty DataFrame to store the data
combined_data = None

# Read and concatenate data from all CSV files
for csv_file in csv_files:
    data = pd.read_csv(csv_file)
    data = data.rename(columns={'answer': f'answer_{csv_files.index(csv_file) + 1}'})
    if combined_data is None:
        combined_data = data
    else:
        combined_data = combined_data.merge(data, on='id')

# Extract the 'id' column and answer columns
id_column = combined_data['id']
answer_columns = combined_data.filter(like='answer')

# Function to find the most common answer in a row
def most_common_answer(row):
    return row.mode().values[0]

# Apply the function to each row
result = answer_columns.apply(most_common_answer, axis=1)

# Combine the 'id' column and result into a new DataFrame
result_df = pd.DataFrame({'id': id_column, 'answer': result})

# Save the result to a new CSV file
result_df.to_csv('blend.csv', index=False)
