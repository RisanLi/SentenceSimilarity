# 使用说明
## 1.train.py
    该文件是存放 训练方法的类
## 2.test.py
    该文件是用来测试 训练方法的类的逻辑
## 3.test2.py
    该文件是用来形成word2vec模型，如 test2.model
## 4.splitDescription.py
    把csv的句子导入到一个文本 形成语料库
## 5.cross_validation.py
    用来测试最终结果

## 使用顺序说明
    首先splitDescription.py 生成语料库
    然后test2.py 形成 word2vec 模型
    其次查看train.py 里面存放 训练逻辑
    然后test.py 尝试导入一两个句子或者词组 查看train.py是否正确
    最后cross_validation.py 查看句子正确率