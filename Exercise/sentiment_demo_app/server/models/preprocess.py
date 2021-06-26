import pandas as pd
import numpy as np
import string
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def load_data():
  with open("./data/sentiment.txt") as f:
      reviews = f.read()

  data = pd.DataFrame([ 
      review.split('\t') for review in reviews.split('\n') ],
      columns=['review', 'label']
  )

  return data


def clen_sentence(text):
    '''
    extract useful tokens from a sentence
    '''

    stop_words_en = stopwords.words('english')
    
    text = text.lower()

    text = text.translate(str.maketrans('', '', string.punctuation))
    
    tokens = word_tokenize(text)
    
    # remove stopping words
    tokens = [ w for w in tokens if w not in stop_words_en ]
    tokens = [ w for w in tokens if len(w) > 1 ]
    
    # return tokens
    return ' '.join(tokens)


def clean_df(data):
    data['cleaned_review'] = [ clen_sentence(review) for review in data['review'].values ]

    data['word_len'] = [ len(x.split()) for x in data['cleaned_review'] ]
    data = data[data['word_len'] > 1]
    
    print('max len: ', data['word_len'].max())
    print('min len: ', data['word_len'].min())
    print('mean len: ', data['word_len'].mean())

    corpus = [ x.split() for x in data['cleaned_review'] ]
    label = data['label'].values.astype(int)
    
    return corpus, label


def build_vocabulary(corpus):
    '''
    tokens: a list of tokens of the corpus
    build_vocabulary(['work', 'eat', 'school', 'read', 'cat', 'eat'])
    '''
    
    tokens = [ w for line in corpus for w in line ]
    vocab = set(tokens)

    word_id = {}
    inverse_word_id = {}
    for i, word in enumerate(vocab):
        word_id[word] = i+1
        inverse_word_id[i+1] = word

    pad_char = '*'
    word_id[pad_char] = 0
    inverse_word_id[0] = pad_char
    vocab.add(pad_char)

    print('voca size', len(word_id))

    return vocab, word_id, inverse_word_id

def pad_text(text, seq_len, pad_str):
    '''
    RNN takes a fixed length of sequence
    '''

    review = None
    text_size = len(text)

    if text_size >= seq_len:
        review = text[:seq_len]
    else:
        review = [pad_str] * (seq_len - text_size) + text
    return review


def text_preprocess(seq_len = 32):
    df = load_data()
    corpus, label = clean_df(df)
    _, word_id, inverse_word_id = build_vocabulary(corpus)

    padding_corpus = [ pad_text(text, seq_len, inverse_word_id[0]) for text in corpus ]
    encoded_fixed_len_corpus = np.array([ [ word_id[t] for t in sent ] for sent in padding_corpus ])

    # save
    np.savetxt(
        "data/cleaned_review.csv", 
        np.concatenate((encoded_fixed_len_corpus, label[:, np.newaxis]), axis=1), 
        fmt='%d', delimiter=","
    )
    with open('data/word_id.json', 'w') as f:
        json.dump(word_id, f)


    # return encoded_fixed_len_corpus, label, word_id, inverse_word_id


if __name__ == '__main__':
  text_preprocess()
  