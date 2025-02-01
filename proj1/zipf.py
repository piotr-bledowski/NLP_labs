import pandas as pd

df = pd.read_csv('proj1/words.txt', sep='\t', header=None, 
                 names=['Index', 'Word', 'Frequency'])

df['Index'] = df['Index'] - 100

df['Zipf_score'] = df['Frequency'] * df['Index']

print(df.head(10))

df.to_csv('proj1/zipf_results.csv', index=False)
