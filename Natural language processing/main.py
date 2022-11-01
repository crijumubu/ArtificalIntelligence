#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
import regex
from nltk.book import *
from nltk import ngrams
from nltk.corpus import wordnet as corpus

#nltk.download()

corpusWords = ['computador', 'gato']

for word in corpusWords:
    
    print('Word: ' + word)
    
    objCalculator = corpus.synsets(word,lang='spa')
    
    for  calculator in objCalculator:
        
        print('\t Phrase: ' + calculator.definition())
        #print('\t Similarity' + calculator.path_similarity(<varibale>))
        
    print('\n')
    
books = {
    'Moby Dick by Herman Melville 1851' : [text1, ['whale','boat','oil','white','harpoon']], 
    'The Book of Genesis' : [text3, ['adan', 'eva', 'world', 'god']],
    'Personals Corpus' : [text9, ['thursday', 'man', '1908']]
}

for book in books:

    print(book)

    tokens = len(books[book][0])
    print('Length database: ' + str(tokens))
    book_noRepitions = sorted(set(books[book][0]))
    tokens_noRepetitions = len(book_noRepitions)
    print('No Repitions: ' + str(tokens_noRepetitions))
    print('Lexical wealth: ' + str(tokens_noRepetitions/tokens))
    
    books[book][0].dispersion_plot(books[book][1])
    
    print('\n')
    
    distribution = FreqDist(book)
    distribution.most_common(17)
    distribution.plot(30)
    
    #books[book][0].concordance('boat')

    #books[book][0].similar('boat')
    
    book_bigrams = list(bigrams(book))
    tetagrams = list(ngrams(book,4))
    distribution = FreqDist(tetagrams)
    distribution.plot(30)

