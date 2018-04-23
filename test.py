# coding:utf-8

from train import Word2Vec

w2v = Word2Vec('test2.model')

print('short|short-term: ', w2v.word_similarity('short', 'short-term'))
print('dow|dj: ', w2v.word_similarity('dow', 'dj'))
print('admiral|instl: ', w2v.word_similarity('admiral', 'instl'))

# print('\n与"漂亮"语义相似的前10个词语:')
# similarWords = w2v.get_similar_Words('漂亮', 10)
# for word, simi in similarWords:
#     print(word, ':', simi)

s1 = 'first trust dow jones internet'
s2 = 'first trust dj internet idx'
s3 = 'vanguard total bond market index admiral shares'
s4 = 'vanguard total bond market idx instl pls'
s5 = 'ford motor co new div: 0.600'
s6 = 'ford motor co'
wordList1 = s1.split()
wordList2 = s2.split()
wordList3 = s3.split()
wordList4 = s4.split()
wordList5 = s5.split()
wordList6 = s6.split()

print("s1|s1: " + str(w2v.sentence_similarity(wordList1, wordList1)))
print("s1|s2: " + str(w2v.sentence_similarity(wordList1, wordList2)))
print("s3|s4: " + str(w2v.sentence_similarity(wordList3, wordList4)))
print("s5|s6: " + str(w2v.sentence_similarity(wordList5, wordList6)))