from gensim.models import word2vec
sentences = word2vec.Text8Corpus(u"/home/risan/Desktop/text")
model = word2vec.Word2Vec(sentences,
                          min_count=1,
                          workers=2,
                          size=20,
                          window=10,
                          sg=1)
# 载入word2vec 模型
# model = word2vec.Word2Vec.load('test2.model')
# 测两个词的相似度
# y2 = model.similarity('idx', 'admiral')
# 求某个词的相近的词
# for i in model.most_similar(''):
#     print(i)
# print('相似度 ', y2)
# 保存模型
# model.save(u'test2.model')
