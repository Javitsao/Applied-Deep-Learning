import pandas as pd
import argparse

def transform_and_save_csv(input_csv, output_csv, columns_to_keep):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Drop 90% of the rows with label 1
    df = df.drop(df[df['label'] == 1].sample(frac=0.9, random_state=42).index)

    # Select specified columns
    df_selected = df.loc[:, columns_to_keep]

    df_selected = df_selected.dropna()

    # Save the transformed DataFrame to a new CSV file
    df_selected.to_csv(output_csv, index=False)

    print(f'Data has been successfully transformed and saved to {output_csv}')

if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Transform and save a CSV file with label swapping and row dropping.')
    parser.add_argument('input_csv', help='Path to the input CSV file')
    parser.add_argument('output_csv', help='Path to the output CSV file')
    parser.add_argument('columns_to_keep', nargs='+', help='Columns to keep in the output CSV')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the function with provided arguments
    transform_and_save_csv(args.input_csv, args.output_csv, args.columns_to_keep)
