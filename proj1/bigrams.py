import pandas as pd
from collections import Counter

df = pd.read_csv('proj1/sentences.txt', sep='\t', header=None, 
                 names=['Index', 'Sentence'])

def get_bigrams(sentence):
    words = sentence.split()
    return [(words[i], words[i+1]) for i in range(len(words)-1)]

all_bigrams = []
for sentence in df['Sentence']:
    all_bigrams.extend(get_bigrams(sentence))

bigram_counts = Counter(all_bigrams)

bigram_df = pd.DataFrame(bigram_counts.most_common(10), 
                        columns=['Bigram', 'Frequency'])

bigram_df.to_csv('proj1/bigram_results.csv', index=False)

print("Top 10 most frequent bigrams:")
print(bigram_df)
