import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('filename.csv')

# Identify and remove duplicate rows
df.drop_duplicates(inplace=True)

# Print the resulting DataFrame
print(df)