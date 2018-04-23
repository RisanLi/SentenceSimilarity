from gensim.models import word2vec



class Word2Vec():
    def __init__(self, modelPath):
        self.model = word2vec.Word2Vec.load('test2.model')

    def get_word_vector(self, word):
        """
        获得词向量

        word: 词语
        return: 词向量
        """

        if word in self.model:
            return self.model[word]
        return None

    def word_similarity(self, word1, word2):
        """
        计算词语相似度

        word1: 词语1
        word2: 词语2
        return: 词语1与词语2的相似度
        """

        if word1 not in self.model or word2 not in self.model:
            return 0
        return self.model.similarity(word1, word2)

    def get_similar_Words(self, word, maxReturnNum):
        """
        获得语义相似的词语

        word: 词语
        maxReturnNum: 最大返回词语数量
        return: 词语及相似度 [(word, simi)...]
        """

        if word not in self.model:
            return None
        return self.model.similar_by_word(word, topn=maxReturnNum)

    def __cal_max_similarity(self, centerWord, wordList):
        """
        计算词语与词语列表中词语的最大相似度

        centerWord: 词语
        wordList: 词语列表
        return: 词语与词语列表中词语的最大相似度
        """

        # max = 0
        # for targetWord in wordList:
        #     if self.model.similarity(targetWord, centerWord) > 0.9:
        #     # if targetWord in self.model.most_similar(centerWord)[0]:
        #         max = 1
        #     else:
        #         if max < self.model.similarity(targetWord, centerWord):
        #             max = self.model.similarity(targetWord, centerWord)
        # # print(sum)
        # return max

        maxSimi = -1
        if centerWord in wordList:
            return 1
        else:
            for word in wordList:
                temp = self.word_similarity(centerWord, word)
                if temp == 0:
                    continue
                if temp > maxSimi:
                    maxSimi = temp
        if maxSimi == -1:
            return 0
        return maxSimi

    def sentence_similarity(self, sentence1Words, sentence2Words):
        """
        计算句子相似度

        sentence1Words: 句子1词语列表
        sentence2Words: 句子2词语列表
        return: 两个句子的相似度
        """
        # newDifferenceWordList1 = list(set(sentence1Words).difference(set(sentence2Words)))
        # newDifferenceWordList2 = list(set(sentence2Words).difference(set(sentence1Words)))
        if len(sentence1Words) == 0 or len(sentence2Words) == 0:
            return 1

        vector1 = [self.__cal_max_similarity(word, sentence2Words) for word in sentence1Words]
        vector2 = [self.__cal_max_similarity(word, sentence1Words) for word in sentence2Words]
        return (sum(vector1) + sum(vector2)) / (len(vector1) + len(vector2))
        # return sum(vector1) / len(vector1)

