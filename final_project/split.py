import pandas as pd
import random

# Load the CSV file into a Pandas DataFrame
file_path = 'fakenews.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Shuffle the DataFrame to get random rows
df_shuffled = df.sample(frac=1, random_state=42)  # Shuffle with a fixed random state for reproducibility

# Split the DataFrame into two parts
num_rows_first_part = 3000
df_part1 = df_shuffled.iloc[:num_rows_first_part]
df_part2 = df_shuffled.iloc[num_rows_first_part:]

# Save the two DataFrames into separate CSV files
file_part1_path = 'news_3000.csv'  # Replace with the path for the first file
file_part2_path = 'news_10000.csv'  # Replace with the path for the second file

df_part1.to_csv(file_part1_path, index=False)
df_part2.to_csv(file_part2_path, index=False)

# Model config MBartConfig {
#   "_name_or_path": "ku-nlp/bart-base-japanese",
#   "activation_dropout": 0.1,
#   "activation_function": "gelu",
#   "add_bias_logits": false,
#   "add_final_layer_norm": true,
#   "architectures": [
#     "MBartForConditionalGeneration"
#   ]