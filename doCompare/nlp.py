import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer#
from nltk.stem import WordNetLemmatizer

'''
TODO
*Breakpoint 1 - Tag First then lematize the tagged array and use the tags for proper lematizing
                and repackage into list of tuples form if possible.

'''

stemmer = PorterStemmer()#
lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words("english"))
stop.remove("not")
posIgnore = ["$","''","(",")",",","--",".",":","CD","FW","LS","NNP","NNPS","NNS","PRP","PRP$","SYM","TO","WDT","WP","WP$","WRB","``"]

#exStr = "Muad'Dib learned rapidly because his first training was in how to learn. And the first lesson of all was the basic trust that he could learn. It's shocking to find how many people do not believe they can learn, and how many more believe learning to be difficult."
exStr = "The striped bats are hanging on their feet for best. The striped bats are hanging on their feet for best."

stns = sent_tokenize(exStr)
wrds = []

for a in stns:
    wrds.append(word_tokenize(a))

wrdsFilt = []

for i in wrds:
    temp = []
    for j in i:
        if j.casefold() not in stop:
            temp.append(j)
    wrdsFilt.append(temp)

tagged = []
for words in wrdsFilt:
    tagged.append(nltk.pos_tag(words))

wrdsLem = []
for words in tagged:
    wrdsLem.append([lemmatizer.lemmatize(word[0],pos=word[1]) for word in words])

for a in wrdsFilt:
    print(a)

print()

#print(wrdsLem)
for a in wrdsLem:
    print(a)

print()

for a in tagged:
    print(a)


'''
for words in wrdsFilt:
    wrdsLem .append([lemmatizer.lemmatize(word) for word in words])
'''

'''
print(wrds)
print(wrdsFilt)
print(wrdsLem)
'''

'''
tagged = []
for words in wrdsLem:
    tagged.append(nltk.pos_tag(words))
print(tagged)
'''

'''
lotr_quote = "It's a dangerous business, Frodo, going out your door."
lotr_quote = exStr
words_in_lotr_quote = word_tokenize(lotr_quote)
lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
tree = nltk.ne_chunk(lotr_pos_tags)
tree.draw()
tree = nltk.ne_chunk(lotr_pos_tags, binary=True)
tree.draw()
'''
