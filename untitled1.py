# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:55:54 2017

@author: ankur
"""
import pandas
import numpy
from nltk.book import *
import nltk
#text3.concordance('lived')
#text2.common_contexts(['monstrous','very'])
#print(len(text3))


#saying = ['After', 'all', 'is', 'said', 'and', 'done','more', 'is', 'said', 'than', 'done']
#tokens = set(saying)
#print(tokens)
#tokens = sorted(tokens)
#print(tokens)
#print(tokens[-2:])
#v = set(text1)
#long_words = [w for w in v if len(w)>15]
#print(sorted(long_words))
#fdist = FreqDist(text5)
#print(fdist['wow'])
#print(sorted([w for w in set(text7) if '-' in w and 'index' in w]))
#print(text9[621:644])
#print(sorted(set(list(set(sent1))+list(set(sent8)))))
#print(text2[-2:])

#words = [w for w in text5 if len(w) == 4]
#fidst = FreqDist(words)
#reverse_items = [(v,k) for (k,v) in fdist.items()]
#print(sorted(reverse_items))
#for text in text6:
#    if text.isupper():
#        print('\n' + text)
        
#print(list(set([w for w in text6 if w.lower().find('pt') != -1])))
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
for item in sent:
    if len(item)>4:
        print(item)
        
#def percent(word,text):
#   fdist = FreqDist(text)
#    x = fdist[word]
#    return (100*(x/(len(text))))
#print(percent('the',text1))
#print(set(sent3)<set(text1))
from nltk.corpus import brown
mystery = brown.words(categories = 'mystery')
wh_words = [w.lower() for w in mystery if w[0:2] == 'wh']
fdist = FreqDist(wh_words)
#print(fdist.items())



cfd = nltk.ConditionalFreqDist(
                               (target, fileid[:4])
                               for fileid in inaugural.fileids()
                               for w in inaugural.words(fileid)
                               for target in ['america', 'citizen']
                               if w.lower().startswith(target))
#cfd.plot()


from nltk.corpus import udhr
a = udhr.fileids()
#print(a)
raw_text = udhr.raw('Hindi-UTF8')
#FreqDist(raw_text).plot()



from nltk.corpus import PlaintextCorpusReader

corpus_root = 'C:/Users/IBM_ADMIN/Downloads/haxm-windows_v6_0_1'
words = PlaintextCorpusReader(corpus_root, '.*\.txt')
#print(words.fileids())


from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
                               (days, fileid)
                               for fileid in ['news', 'romance']
                               for days in ['monday','tuesday']
                               for w in brown.words(categories = fileid)
                               if w.lower()==days)
#cfd.tabulate()
#cfd.plot()  

#def generate_model(cfdist, word, num=15):
#    for i in range(num):
#        print(word)
#        word = cfdist[word].max()
        
        
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
#generate_model(cfd, 'living')







puzzle_letters = nltk.FreqDist('egivrvonl')
obligatory='r'
words = nltk.corpus.words.words()
#print([w for w in words if len(w)>=4 
#                  and obligatory in w
#                  and nltk.FreqDist(w)<=puzzle_letters])  

from nltk.corpus import wordnet as wn
#for i,j in enumerate(wn.synsets('dish')):
#    print ("Synonyms:", ", " .join(j.lemma_names()))

    
    
    
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[26]

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[26]
#print(types_of_motorcar)
#for i,j in enumerate(types_of_motorcar):
#    print(j.lemma_names())


names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist((fileid, name[0])
                            for fileid in names.fileids()
                            for name in names.words(fileid))
cfd.plot()


text_1 = [w.lower() for w in text1]
text_2 = [w.lower() for w in text2]

bigrams_1 = nltk.bigrams(text_1)
bigrams_2 = nltk.bigrams(text_2)
cfd_1 = nltk.ConditionalFreqDist(bigrams_1)
cfd_2 = nltk.ConditionalFreqDist(bigrams_2)
print('text1',':',cfd_1['monstrous'].max())
print('text2',':',cfd_2['monstrous'].max())





from nltk.corpus import cmudict

entries = cmudict.entries()
words = [w[0] for w in entries]
fd = nltk.FreqDist(words)
double_pronounce = [w for w in set(words) if fd[w]>1]
print(len(double_pronounce))



synset = wn.all_synsets('n')
new = [w for w in synset if len(w.hyponyms()) == 0]
print(len(new))


#def supergloss(s):
#    hyper = s.hypernyms()
#    hypo = s.hyponyms()

    
def supergloss(s):
    n = 0
    synset = (s.name, s.definition)
    hypernyms = s.hypernyms()
    hyponyms = s.hyponyms()

    if hypernyms != []:
        while n < len(hypernyms):
            for hypernym in s.hypernyms():
                hypernyms[n] = (hypernym.name, hypernym.definition)
                n = n + 1
    else:
        hypernyms = 'none'

    n = 0
    if hyponyms != []:
        while n < len(hyponyms):
            for hyponym in hyponyms:
                hyponyms[n] = (hyponym.name, hyponym.definition)
                n = n + 1
    else:
        hyponyms = 'none'

    total = 'ROOT WORD:', synset, 'HYPERNYMS:', hypernyms, 'HYPONYMS:', hyponyms
    return total

from nltk.corpus import brown
fdist = nltk.FreqDist(w.lower() for w in brown.words(fileids = brown.fileids()))
words = [' ']
for word in fdist:
    if fdist[word]>=3:
        words.append(word)
lexi = 0
for category in brown.categories():
    token = len(brown.words(categories = category))
    set_token = len(set(brown.words(categories = category)))
    lex = token/set_token
    if lex >= lexi:
        lexi = lex
        a = category
print(a)



from nltk.corpus import stopwords
stp_wrds = stopwords.words('english')
bigrams = nltk.bigrams([w.lower() for w in text_1])
new_bigrams = [(i,j) for (i,j) in bigrams if i not in stp_wrds and j not in stp_wrds]
fdist = nltk.FreqDist(new_bigrams)
keys = fdist.keys()
print(fdist.most_common(50))

def hedge(text):
    n = 3
    new_list = list(text)
    while n<= len(new_list):
        new_list.insert(n, 'like')
        n = n+4
    for w in new_list:
        print(w)
        
import nltk, pylab, matplotlib, random
from decimal import *        
def zipf(text):
    fdist = FreqDist([w.lower() for w in text])
    keys = fdist.keys()
    freq=[]
    rank=[]
    n=1
    for w in keys:
        frequency = Decimal.logb(Decimal(fdist[w]))
        freq.append(frequency)
        rank.append(Decimal.logb(Decimal(n)))
        n = n+1
    pylab.plot(rank, freq)
    return pylab.show()
#zipf(text_1)
import random
def zepf_random(text):
    n = 0
    scrambled = ''
    while n < len(text):
        scrambled = scrambled + ' ' + random.choice(text)
        n = n+1
    scrambled = scrambled.split()
    return zipf(scrambled)
zepf_random(text_1)
list1 = ['']
from nltk.corpus import udhr
def find_language(text):
    file_ids = [w for w in udhr.fileids() if w[-6:] == 'Latin1']
    for file in file_ids:
        if text in [w.lower() for w in udhr.words(file)]:
           list1.append(file[:-7])
    return list1
print(find_language('peace'))



