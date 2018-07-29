# _*_coding:utf-8 _*_
"""
@Time    :2018/6/20 15:14
@Author  :weicm
#@Software: PyCharm
"""

from gensim.models import word2vec
# from gensim.models.keyedvectors import KeyedVectors
# 导入模型
model = word2vec.Word2Vec.load(r"example_model.model")
# model = KeyedVectors.load_word2vec_format(r"w2v.bin", binary=True)
file = r"E:\Html-cheyin-data\baidu_cars_news\company_true_entity.txt"
f2 = open("company_true_entity.txt","w",encoding="utf-8")
with open(file,'r',encoding="utf-8") as f:
    words = f.readlines()
    for word in words:
        word = word.strip()
        try:
            word_similars = model.most_similar(word)
        except Exception:
            print("\n")
        else:
            for word_similar in word_similars:
                word_similar_score = word_similar[1]
                if word_similar_score > 0.85:
                    print(word+"\t"+word_similar[0]+"\t"+str(word_similar[1]))
                    word_similar1 = word + "\t" + word_similar[0] + "\t" + str(word_similar[1])
                    f2.write(word_similar1+"\n")

    f2.close()