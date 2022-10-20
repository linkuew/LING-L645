import sys, math, re, pickle
from collections import defaultdict, Counter

def tokenise(s):
    s = re.sub('([.,!?])', r' \1', s)
    s = s.split()
    return s

model = defaultdict(lambda : defaultdict(float))

bigrams, unigrams = defaultdict(Counter), Counter() # Unigram and bigram counts

line = sys.stdin.readline()
while line: # Collect counts from standard input
    tokens = ['<BOS>'] + tokenise(line)

    for tok in tokens:
        if unigrams[tok]:
            unigrams[tok] += 1
        else:
            unigrams[tok] = 1

    for i in range(len(tokens)-1):
        if bigrams[tokens[i]+' '+tokens[i+1]]:
            bigrams[tokens[i]+' '+tokens[i+1]] += 1
        else:
            bigrams[tokens[i]+' '+tokens[i+1]] = 1


    line = sys.stdin.readline()

# !!! Now calculate the probabilities !!!
max = 0
for k,v in unigrams.items():
    if v > max:
        max = v

for k,v in bigrams.items():
    bigrams[k] = v / float(max)


print('Saved %d bigrams.' % sum([len(i) for i in model.items()]))
pickle.dump(dict(model), open('model.lm', 'wb'))
