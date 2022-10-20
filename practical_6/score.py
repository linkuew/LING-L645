import sys, re
import numpy as np
import math

from model import *

###############################################################################

blob = torch.load('model.lm')
idx2word = blob['vocab']
word2idx = {k: v for v, k in idx2word.items()}
vocabulary = set(idx2word.values())

#model = BigramNNmodel(len(vocabulary), EMBEDDING_DIM, CONTEXT_SIZE, HIDDEN_DIM)
model = TrigramNNmodel(len(vocabulary), EMBEDDING_DIM, TRI_CONTEXT_SIZE, HIDDEN_DIM)
model.load_state_dict(blob['model'])

###############################################################################

BATCH_SIZE = 1

line = sys.stdin.readline()
while line:
    tokens = preprocess(line)

    x_test = []
    y_test = []
#    for i in range(len(tokens) - 1): #!!!#
    for i in range(len(tokens) - 2):
#        x_test.append([word2idx[tokens[i]]]) #!!!#
#        y_test.append([word2idx[tokens[i+1]]]) #!!!#
        x_test.append([word2idx[tokens[i]], word2idx[tokens[i+1]]])
        y_test.append([word2idx[tokens[i+2]]])

    x_test = np.array(x_test)
    y_test = np.array(y_test)

    test_set = np.concatenate((x_test, y_test), axis=1)
    test_loader = DataLoader(test_set, batch_size=BATCH_SIZE)

    total_prob = 1.0
    for i, data_tensor in enumerate(test_loader):
#        context_tensor = data_tensor[:,0:1] #!!!#
#        target_tensor = data_tensor[:,1] #!!!#
        context_tensor = data_tensor[:,0:2]
        target_tensor = data_tensor[:,2]

        log_probs = model(context_tensor)
        probs = torch.exp(log_probs)
        predicted_label = int(torch.argmax(probs, dim=1)[0])

        true_label = y_test[i][0]
        true_word = idx2word[true_label]

        prob_true = float(probs[0][true_label])
        total_prob *= prob_true

    print('%.6f\t%.6f\t' % (total_prob, math.log(total_prob)), tokens)

    line = sys.stdin.readline()


cos = nn.CosineSimilarity(dim=0)

lm_similarities = {}

# word pairs to calculate similarity
words = {('england','mexico'),('england','here'),('england','you'),('england','still')}

# ----------- Calculate LM similarities using cosine similarity ----------
for word_pairs in words:
    w1 = word_pairs[0]
    w2 = word_pairs[1]
    words_tensor = torch.LongTensor([word2idx[w1], word2idx[w2]])
    # get word embeddings from the best model
    words_embeds = model.embeddings(words_tensor)
    # calculate cosine similarity between word vectors
    sim = cos(words_embeds[0],words_embeds[1])
    lm_similarities[word_pairs] = sim.item()

print(lm_similarities)
