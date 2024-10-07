import pandas as pd

# Load the CSV file into a Pandas DataFrame
file_path = 'fakenews.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Mapping dictionary to replace values
replace_map = {0: 0, 1: 1, 2: 1}

# Replace values in the 'isfake' column using the mapping dictionary
df['isfake'] = df['isfake'].map(replace_map).fillna(df['isfake'])

# Save the updated DataFrame back to a CSV file
updated_file_path = 'news_fm.csv'  # Replace with your desired file path
df.to_csv(updated_file_path, index=False)
