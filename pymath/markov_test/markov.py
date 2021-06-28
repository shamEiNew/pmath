import pandas as pd
import seaborn as sns
import numpy as np
import glob

file_names = glob.glob('books/*.txt')

def get_sentences(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as f:
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
#print(sentences)

corpus = ""
for file_name in file_names:
    with open(file_name, 'r', encoding='utf-8') as f:
            corpus+=f.read()
corpus = corpus.replace('\n',' ')
corpus = corpus.replace('\t',' ')
corpus = corpus.replace('“', ' " ')
corpus = corpus.replace('”', ' " ')
for spaced in ['.','-',',','!','?','(','—',')']:
    corpus = corpus.replace(spaced, ' {0} '.format(spaced))
print(len(corpus))

corpus_words = corpus.split(' ')
corpus_words = [word for word in corpus_words if word != '']
#for word in corpus_words: print(word)

distinct_words = list(set(corpus_words))
word_idx_dict = {word: i for i, word in enumerate(distinct_words)}
distinct_words_count = len(list(set(corpus_words)))
print(distinct_words_count)

#next_word_matrix = np.zeros([distinct_words_count,distinct_words_count])
print(word_idx_dict)