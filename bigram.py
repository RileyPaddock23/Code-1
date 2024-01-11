import numpy as np

f = open("./OscarWilde.txt", "r")
substitutions = {k:k for k in "abcdefghijklmnopqrstuvwxyzã- "}
substitutions["\n"] = " "

adjusted_text = ""
for c in f.read().lower():
    try:
        adjusted_text += substitutions[c]
    except KeyError:
        adjusted_text += ""

ordered_words = adjusted_text.split(" ")

word_bank = list(set(ordered_words))
stoi = {w:i for i,w in enumerate(word_bank)}
itos = {stoi[key]:key for key in stoi}
dim = len(set(ordered_words))
probabs = np.zeros((dim, dim))#first index previous word, second next word occurance

for i in range(1,len(ordered_words)):
    probabs[stoi[ordered_words[i-1]]][stoi[ordered_words[i]]] += 1

for i in range(dim):
    s = sum(probabs[i])
    probabs[i] = [x/s for x in probabs[i]]

np.save("bigram_arr.npy",probabs)
# probabs = np.load("bigram_arr.npy")

prev = np.random.choice(word_bank)
for x in range(10):
    print(prev)
    next = itos[np.random.choice([i for i in range(dim)], p = probabs[stoi[prev]])]
    prev = next
