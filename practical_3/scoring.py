import pickle
import re

model = pickle.load(open('model.lm', 'rb'))

sent = input('enter sentence: ')

sent = re.sub('([.,!?])', r' \1', sent)
words = sent.split()
words = ['<BOS>'] + words

P = 1

for i in range(len(words) - 1):
    P *= model[words[i]+words[i+1]]

print(P, words)
