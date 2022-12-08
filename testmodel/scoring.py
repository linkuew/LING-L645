import pickle
import re

model = pickle.load(open('model.lm', 'rb'))

#sent = input('enter sentence: ')

corpus =['where are you?',
'were you in england?',
'are you in mexico?',
'i am in mexico.',
'are you still in mexico?' ]

bigrams = dict()

for sent in corpus:
    sent = re.sub('([.,!?])', r' \1', sent)
    words = sent.split()
    words = ['<BOS>'] + words

    for i in range(len(words)-1):
        try:
            bigrams[words[i]+' '+words[i+1]] += 1
        except:
            bigrams[words[i]+' '+words[i+1]] = 1

#P = 1
#
#for i in range(len(words) - 1):
#    P *= model[words[i]+words[i+1]]

tokens = []
for line in corpus:
    line = re.sub('([.,!?])', r' \1', line)
    words = line.split()
    words = ['<BOS>'] + words
    tokens += words
tokens = set(tokens)

P = 1
for k,v in bigrams.items():
    try:
        P *= model[k]
    except:
        continue

print(P**(-1/len(set(tokens))))


print(P, words)
