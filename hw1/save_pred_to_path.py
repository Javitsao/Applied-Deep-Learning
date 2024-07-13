import pandas as pd
import sys
# Read data from the source CSV file
source_file = "blend.csv"
data = pd.read_csv(source_file)

# Perform any necessary operations on the data here, if needed

# Write the data to a new CSV file
destination_file = sys.argv[1]
data.to_csv(destination_file, index=False)