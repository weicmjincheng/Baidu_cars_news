# _*_coding:utf-8 _*_
"""
@Time    :2018/6/20 13:15
@Author  :weicm
#@Software: PyCharm

"""

from gensim.models import word2vec

sentences = word2vec.Text8Corpus(r"E:\Html-cheyin-data\baidu_cars_news\jieba_news_data.txt")  # 加载语料
model = word2vec.Word2Vec(sentences, size=200, min_count=5)

# 保存模型，以便重用
model.save("example_model.model")
