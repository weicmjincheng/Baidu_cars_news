file = r"E:\Html-cheyin-data\baidu_cars_news\car_news_baidu.txt"
f2 = open(r"E:\Html-cheyin-data\baidu_cars_news\data_cleanout.txt", 'a+', encoding='utf-8')
with open(file, "r+", encoding='UTF-8', errors='ignore') as f1:
    lines = f1.readlines()
    # print(lines[0])
    for line in lines:
        # print(len(line))
        if len(line) != 2:
            f2.write(
            line.replace("\\u3000", '').replace("\\xa0", '').replace("\\r", '').replace("\\n", '').replace("\\t",
            '').replace("【", "").replace("】", "").replace("（", "").replace("）", "").replace("↓", "").replace(".", "").replace("★",""))
            f2.close()