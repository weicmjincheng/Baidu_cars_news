# _*_coding:utf-8 _*_
"""
@Time    :2018/6/20 17:35
@Author  :weicm
#@Software: PyCharm
"""
f2 = open("company_clean_entity.txt","w",encoding="utf-8")
with open("company_true_entity.txt","r",encoding="utf-8") as f:
    words = f.readlines()
    list_word = []
    for word11 in words:
        word = word11.split("\t")
        word1 = word[0]+word[1]
        word2 = word[1] + word[0]
        if word1 or word2 not in list_word:
            list_word.append(word1)
            print(word)
            f2.write(word11)
    f2.close()

