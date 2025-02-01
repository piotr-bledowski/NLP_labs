import pandas as pd

# Read the file into a dataframe with column names
df = pd.read_csv('proj1/words.txt', sep='\t', header=None, 
                 names=['Index', 'Word', 'Frequency'])

# Decrease the index column by 100
df['Index'] = df['Index'] - 100

# Calculate Zipf score (frequency / index)
df['Zipf_score'] = df['Frequency'] / df['Index']

# Display first 10 results
print(df.head(10))

# Save to CSV file with headers
df.to_csv('proj1/zipf_results.csv', index=False)
