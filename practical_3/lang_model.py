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
            bigrams[words[i]+words[i+1]] += 1
        except:
            bigrams[words[i]+words[i+1]] = 1

maxu = 0

for key,value in unigrams.items():
    if value > maxu:
        maxu = value

for key,value in bigrams.items():
    if value > maxu:
        maxu = value

for key,value in bigrams.items():
    bigrams[key] /= float(maxu)

for key,value in unigrams.items():
    print(key, value)

for key,value in bigrams.items():
    print(key, value)

pickle.dump(bigrams, open('model.lm', 'wb'))
