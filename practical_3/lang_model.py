import pickle
import re

corpus = ['are you still here?',
            'where are you?',
            'are you tired?',
            'i am tired.',
            'are you in england?',
            'were you in mexico?']

unigrams = dict()
bigrams = dict()

for sent in corpus:
    sent = re.sub('([.,!?])', r' \1', sent)
    words = sent.split()
    words = ['<BOS>'] + words

    for word in words:
        try:
            unigrams[word] += 1
        except:
            unigrams[word] = 1

    for i in range(len(words)-1):
        try:
            bigrams[words[i]+' '+words[i+1]] += 1
        except:
            bigrams[words[i]+' '+words[i+1]] = 1

for key,value in bigrams.items():
    print(key)
    print(unigrams[key.split(' ')[0]])
    bigrams[key] /= float(unigrams[key.split()[0]])

#for key,value in unigrams.items():
#    print(key, value)

for key,value in bigrams.items():
    print(key, value)

tokens = []
for line in corpus:
    line = re.sub('([.,!?])', r' \1', line)
    words = line.split()
    words = ['<BOS>'] + words
    tokens += words
tokens = set(tokens)

P = 1
for k,v in bigrams.items():
    P *= v

print(P**(-1/len(set(tokens))))


pickle.dump(bigrams, open('model.lm', 'wb'))
