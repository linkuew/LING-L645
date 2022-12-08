from math import log
import numpy as np
import json
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

# beam search
def beam_search_decoder(data, k):
    sequences = [[list(), 0.0]]
    # walk over each step in sequence

    max_T, max_A = data.shape

    # Loop over time
    for t in range(max_T):
        all_candidates = list()
        # expand each current candidate
        for i in range(len(sequences)):
            seq, score = sequences[i]
            # Loop over possible alphabet outputs
            for c in range(max_A - 1):
                candidate = [seq + [c], score - log(data[t, c])]
                all_candidates.append(candidate)
        # order all candidates by score
        ordered = sorted(all_candidates, key=lambda tup:tup[1])
        # select k best
        sequences = ordered[:k]
    return sequences

def decode(string):
    new_list = []
    new_list.append(string[0])
    for char in string:
        if char == new_list[-1]:
            continue
        else:
            new_list.append(char)
    return new_list


# define a sequence of 10 words (rows) over a vocab of 5 words (columns),
# e.g.
#      a  bites cat  dog  the
# 1   0.1  0.2  0.3  0.4  0.5
# 2   0.5  0.3  0.5  0.2  0.1
# ...
# 10  0.3  0.4  0.5  0.2  0.1

#data = [[0.1, 0.2, 0.3, 0.4, 0.5],
#        [0.4, 0.3, 0.5, 0.2, 0.1],
#        [0.1, 0.2, 0.3, 0.4, 0.5],
#        [0.5, 0.4, 0.3, 0.2, 0.1],
#        [0.1, 0.2, 0.3, 0.4, 0.5],
#        [0.5, 0.4, 0.3, 0.2, 0.1],
#        [0.1, 0.2, 0.3, 0.4, 0.5],
#        [0.5, 0.4, 0.3, 0.2, 0.1],
#        [0.1, 0.2, 0.3, 0.4, 0.5],
#        [0.3, 0.4, 0.5, 0.2, 0.1]]

with open('output.json') as file:
    data = json.load(file)
    data = data["logits"]
data = np.array(data)
beam_width = 3

dict = {0: " ",1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i",10: "j",11: "k",12: "l",13: "m",14: "n",15: "o",16: "p",17: "q",18: "r",19: "s",20: "t",21: "u",22: "v",23: "w",24: "x",25: "y",26: "z",27: "'"}

# decode sequence
result = beam_search_decoder(data, beam_width)

# print result
for i, seq in enumerate(result):
    print(i, seq)
    sequence = seq[0]
    sequence = decode(sequence)
    prob = seq[1]
    for k in sequence:
        print(dict[k], end='')
    print()

# produce heatmap
fig, ax = plt.subplots()
im = ax.imshow(data)

fig.tight_layout()
plt.show()
