import pandas as pd
import seaborn as sns
import numpy as np
import glob

file_names = glob.glob('books/*.txt')

def get_sentences(file_name):
    with open(file_name, 'r') as f:
        return f.read().split('.')

MIN_LENGTH = 15
sentences = []
for file_name in file_names:
    sentences+=get_sentences(file_name)

sentences = [sentence.replace('\n','') for sentence in sentences]
sentences = [sentence.replace('\t','') for sentence in sentences]
sentences = [sentence for sentence in sentences if len(sentence)>MIN_LENGTH]

lengths = [len(sentence) for sentence in sentences]

lengths = pd.Series(lengths)

lengths.quantile(.8)
lengths.describe()

corpus = ""
for file_name in file_names:
    with open(file_name, 'r') as f:
            corpus+=f.read()
corpus = corpus.replace('\n',' ')
corpus = corpus.replace('\t',' ')
corpus = corpus.replace('“', ' " ')
corpus = corpus.replace('”', ' " ')
for spaced in ['.','-',',','!','?','(','—',')']:
    corpus = corpus.replace(spaced, ' {0} '.format(spaced))
len(corpus)

corpus_words = corpus.split(' ')
corpus_words= [word for word in corpus_words if word != '']

distinct_words = list(set(corpus_words))
word_idx_dict = {word: i for i, word in enumerate(distinct_words)}
distinct_words_count = len(list(set(corpus_words)))
distinct_words_count

next_word_matrix = np.zeros([distinct_words_count,distinct_words_count])

#print(word_idx_dict)

for i, word in enumerate(corpus_words[:-1]):
    first_word_idx = word_idx_dict[word]
    next_word_idx = word_idx_dict[corpus_words[i+1]]
    next_word_matrix[first_word_idx][next_word_idx] +=1

def most_likely_word_after(aWord):
    most_likely = next_word_matrix[word_idx_dict[aWord]].argmax()
    return distinct_words[most_likely]

def naive_chain(seed, length=15):
    current_word = seed
    sentence = seed

    for _ in range(length):
        sentence+=' '
        next_word = most_likely_word_after(current_word)
        sentence+=next_word
        current_word = next_word
    return sentence

#print(naive_chain('Admetus'))

import random
from random import random 

def weighted_choice(objects, weights):
    """ returns randomly an element from the sequence of 'objects', 
        the likelihood of the objects is weighted according 
        to the sequence of 'weights', i.e. percentages."""

    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()
    # standardization:
    np.multiply(weights, 1 / sum_of_weights, weights)
    weights = weights.cumsum()
    x = random()
    for i in range(len(weights)):
        if x < weights[i]:
            return objects[i]

from numpy.random import choice

def sample_next_word_after(aWord, alpha = 0):
    next_word_vector = next_word_matrix[word_idx_dict[aWord]] + alpha
    likelihoods = next_word_vector/next_word_vector.sum()
    return weighted_choice(distinct_words, likelihoods)

#print(sample_next_word_after('Zeus'))

def stochastic_chain(seed, chain_length=15, seed_length=2):
    current_words = seed.split(' ')
    if len(current_words) != seed_length:
        raise ValueError(f'wrong number of words, expected {seed_length}')
    sentence = seed

    for _ in range(chain_length):
        sentence+=' '
        next_word = sample_next_word_after_sequence(' '.join(current_words))
        sentence+=next_word
        current_words = current_words[1:]+[next_word]
    return sentence

k = 5
sets_of_k_words = [ ' '.join(corpus_words[i:i+k]) for i, _ in enumerate(corpus_words[:-k]) ]

print([len(list(set(sets_of_k_words))),
       len(sets_of_k_words)])

from scipy.sparse import dok_matrix

sets_count = len(list(set(sets_of_k_words)))
next_after_k_words_matrix = dok_matrix((sets_count, len(distinct_words)))
print(next_after_k_words_matrix.shape)

distinct_sets_of_k_words = list(set(sets_of_k_words))
k_words_idx_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)}
distinct_k_words_count = len(list(set(sets_of_k_words)))
print(len(sets_of_k_words))
for i, word in enumerate(sets_of_k_words[:-k]):
    if i % 50000 == 0:
        print(i)
    word_sequence_idx = k_words_idx_dict[word]
    next_word_idx = word_idx_dict[corpus_words[i+k]]
    next_after_k_words_matrix[word_sequence_idx, next_word_idx] +=1

from numpy.random import choice

def sample_next_word_after_sequence(word_sequence, alpha = 0):
    next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]] + alpha
    likelihoods = next_word_vector/next_word_vector.sum()
    return weighted_choice(distinct_words, likelihoods.toarray())

if __name__ == '__main__':
    print(stochastic_chain('Achilles then'))