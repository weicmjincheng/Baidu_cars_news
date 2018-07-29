# _*_coding:utf-8 _*_
"""
@Time    :2018/6/20 10:36
@Author  :weicm
#@Software: PyCharm
"""
import re
import jieba


def jieba_stopwords():
    # 导入字典
    jieba.load_userdict('dict.txt')

    # 读取停用词
    stopwords = [line.strip() for line in open('my_stop_word.txt', 'r', encoding='utf-8').readlines()]

    file = r'E:\Html-cheyin-data\baidu_cars_news\car_news_data_cleanout.txt'
    f2 = open(r'E:\Html-cheyin-data\baidu_cars_news\jieba_news_data.txt', 'w', encoding='utf-8')
    with open(file, "r+", encoding='utf-8') as f1:
        lines = f1.readlines()
        for line in lines:
            print(line)
            lines2 = ''.join(line)
            # print(lines2)
            lines3 = lines2.replace('\n', '')
            lines4 = ''.join(re.findall(u'[\u4e00-\u9fa5]+', lines3))

            # 结巴分词 全模式
            seg_list = jieba.cut(lines4)
            # 去除停用词
            seg_list2 = [word for word in seg_list if not word in stopwords]
            seg_list3 = ' '.join(seg_list2)
            print(seg_list3)


            f2.write(seg_list3+'\n')
        f2.close()



if __name__ == "__main__":
    jieba_stopwords()