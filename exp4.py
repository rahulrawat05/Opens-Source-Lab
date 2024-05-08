import nltk
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import defaultdict

print("Rahul Singh Rawat")
print("RN : 210410101092")

model = defaultdict(lambda: defaultdict(lambda: 0))

for sentence in reuters.sents():
    sentence = [word.lower() for word in sentence]
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1

def predict_next_word(words):
    words = [word.lower() for word in words]
    next_word = max(model[tuple(words)].items(), key=lambda x: x[1])[0]
    return next_word

input_words = ['today', 'is']
next_word = predict_next_word(input_words)
print(f"The next word after '{' '.join(input_words)}' is '{next_word}'.")
