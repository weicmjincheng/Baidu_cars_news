import requests
from lxml import etree
from time import sleep

f4 = open(r"E:\Html-cheyin-data\data_error_11.txt", 'a+', encoding='utf-8')
f3 = open(r"E:\Html-cheyin-data\data_none_11.txt", 'a+', encoding='utf-8')
f2 = open(r"E:\Html-cheyin-data\data10.txt", 'a+', encoding='utf-8')
with open('url.txt', "r+", encoding='utf-8') as f:
    # 一次性读取全部文件内容 返回list类型
    lines = f.readlines()
    for list in lines:
        print(list.strip())
        try:
            list = list.replace('\n', '')
            html = requests.get(list,timeout=10)
            bianma = html.encoding
            print(bianma)
            if bianma == 'utf-8' or bianma == 'UTF-8':
                html.encoding = 'utf-8'
            elif bianma == 'gbk' or bianma == 'GBK':
                html.encoding = 'gbk'
            elif bianma == 'gb2312':
                html.encoding = 'gbk'
            elif bianma == 'ISO-8859-1':
                html.encoding = 'utf-8'
            html = html.text
            # 解析html源代码
            sel = etree.HTML(html)
            # //div[@class="detail-r fr"]/p
            page_contexts = sel.xpath(
                '//div[@class="left_zw"]//p//text()|//div[@class="detail"]//p//text()|//div[@class="post_text"]//p//text()|//div[@class="text clear"]//p//text()|//div[@class="page-content clearfix article_16"]//p//text()|//div[@class="post_text"]//p//text()|//div[@class="content"]//p//text()|//div[@class="main lazyload"]//p//text()|//div[@class="article_main"]//p//text()|//div[@class="news-detail-txt"]//p//text()|//div[@class="article-content motu_cont"]//p//text()|//div[@class="details"]//p//text()|//div[@class="article-content motu_cont"]//p//span//text()|//div[@class="arl-c-txt"]//p//text()|//div[@class="auto_wz_40"]//p//text()|//div[@class="news-editbox"]//p//text()|//div[@class="Cnt-Main-Article-QQ"]//p//text()|//div[@class="c_tcon clearfix"]//p//text()|//article[@id="article-DI5FATSO0514R9LP"]//p/text()|//div[@class="article-content"]//p//text()|//div[@class="details"]/div//span//text()|//div[@class="details"]/div/strong/span/text()|//div[@class="detail-r fr"]//p//text()|//div[@class="text"]//p//text()')

        except Exception:
            print("报错打印报错地址：%s" % list)
            f4.write(list + "\n")
            f4.close()
        else:
            # print(page_contexts)
            page_contextss = str(page_contexts)
            print(page_contextss)
            if len(page_contextss) <5:
                f3.write(list + "\n")
                f3.close()
            for page_context in page_contextss.split(u'。'):
                page_context4 = page_context.replace(',', '').replace("'", '').replace(' ', '').replace('[', '').replace(
                "]", '').replace("\n", '')
                print(page_context4 + u'。')
                f2.write(page_context4 + u'。' + "\n")
                f2.close()
            # sleep(3)