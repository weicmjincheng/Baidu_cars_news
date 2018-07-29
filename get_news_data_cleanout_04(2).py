file = r"E:\Html-cheyin-data\baidu_cars_news\car_news_baidu.txt"
with open(file, "r+", encoding='UTF-8', errors='ignore') as f1:
    lines = f1.readlines()
    # print(lines)
    in_str = lines


def is_ustr(in_str):
    out_str = ''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str = out_str + in_str[i]
        else:
            out_str = out_str + ''
    f2 = open(r"E:\Html-cheyin-data\baidu_cars_news\data_cleanout.txt", 'a+', encoding='utf-8')
    f2.write(out_str.replace("\\u3000", '').replace("\\xa0", '').replace("\\r", '').replace("\\n", '').replace("\\t",
                                                                                                               '').replace(
        "【", "").replace("】", "").replace("（", "").replace("）", "").replace("↓", "").replace(".", ""))
    f2.close()


def is_uchar(uchar):
    # 判断一个unicode是否是汉字
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    # 判断一个unicode是否是数字
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
        # 判断一个unicode是否是英文字母
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    if uchar in ('-', ',', '，', '。', '.', '>', '?'):
        return True
    return False


is_ustr(in_str)
