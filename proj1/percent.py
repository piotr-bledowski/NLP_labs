import pandas as pd

df = pd.read_csv('proj1/words.txt', sep='\t', header=None, 
                 names=['Index', 'Word', 'Frequency'])

total_frequency = df['Frequency'].sum()

df['Cumulative_Frequency'] = df['Frequency'].cumsum()
df['Cumulative_Percentage'] = (df['Cumulative_Frequency'] / total_frequency) * 100

results = {}

for threshold in range(10, 101, 10):
    words_count = len(df[df['Cumulative_Percentage'] <= threshold])
    results[threshold] = words_count

results_df = pd.DataFrame(list(results.items()), 
                         columns=['Percentage', 'Number_of_Words'])
results_df.to_csv('proj1/percentage_results.csv', index=False)

print("Results:")
print(results_df)
