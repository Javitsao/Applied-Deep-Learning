import pandas as pd
import argparse
from sklearn.model_selection import train_test_split

def clean_and_save_csv(input_csv, columns_to_keep, split_ratio):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Drop rows with label=1 to achieve a 10:1 ratio
    df_label_0 = df[df['label'] == 0]
    df_label_1 = df[df['label'] == 1].sample(frac=0.1, random_state=42)

    df_cleaned = pd.concat([df_label_0, df_label_1])

    # Add missing columns with value 0 or ""
    for column in columns_to_keep:
        if column not in df_cleaned.columns:
            if df_cleaned.dtypes.get(column) == 'object':
                df_cleaned[column] = ""  # For string columns, replace missing values with an empty string
            else:
                df_cleaned[column] = 0   # For numeric columns, replace missing values with 0

    # Fill missing values with 0 for numeric columns and an empty string for string columns
    df_cleaned = df_cleaned.fillna(0) if df_cleaned.dtypes.get(column) != 'object' else df_cleaned.fillna("")

    # Check if split_ratio is 0, save the cleaned DataFrame to a single output CSV file
    if split_ratio == 0:
        output_csv = input_csv.replace(input_csv, 'output_news3.csv')
        df_cleaned.to_csv(output_csv, index=False)
        print(f'Data has been successfully cleaned and saved to {output_csv}')
    else:
        # Split the DataFrame into train and test sets
        train_df, test_df = train_test_split(df_cleaned, test_size=1-split_ratio, random_state=42, stratify=df_cleaned['label'])

        # Generate the output CSV file names
        output_train_csv = input_csv.replace(input_csv, 'train_fake_less_old.csv')
        output_test_csv = input_csv.replace(input_csv, 'test_fake_less_old.csv')

        # Save the cleaned DataFrames to new CSV files
        train_df.to_csv(output_train_csv, index=False)
        test_df.to_csv(output_test_csv, index=False)

        print(f'Data has been successfully split and saved to {output_train_csv} (train) and {output_test_csv} (test)')

if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Clean and save a CSV file with specified columns and perform train/test split.')
    parser.add_argument('input_csv', help='Path to the input CSV file')
    parser.add_argument('columns_to_keep', nargs='+', help='Columns to keep in the output CSV')
    parser.add_argument('--split-ratio', type=float, default=0.8, help='Ratio to split the data into train and test sets (default: 0.8)')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the function with provided arguments
    clean_and_save_csv(args.input_csv, args.columns_to_keep, args.split_ratio)
