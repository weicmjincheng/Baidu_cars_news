1	设定待爬取内容关键字列表
2	使用工具进行先期url爬取    		chrome_get_news_01.py
3	根据url书写xpath规则爬取页面文本信息	get_url_news_02.py
注：在数据量比较小的时候可以根据car_news_data_url_none.txt重写url规则获取更多数据  url_recognize_03.py 
4	清洗数据（去重、非法字符过滤）		get_news_data_cleanout_04.py or  get_news_data_cleanout_04(2).py(运行比较慢)
5	命名实体识别（按照命名实体识别规则进行词性识别后连接连续的相同词性的词）
6	获得命名实体并进行清洗
7	进行word2vec训练，找相似词判别关系，根据得分大小