import re

f2 = open(r"E:\Html-cheyin-data\url_need_write.txt", 'a+', encoding='utf-8')
with open(r"E:\Html-cheyin-data\data_none_11.txt","r+",encoding="utf-8") as f:
    urls = f.readlines()
    url_list = []
    for url in urls:
        url_new2 = re.findall(r"(.*.com.cn)", url)
        url_new5 = re.findall(r"(.*.org)", url)
        url_new6 = re.findall(r"(.*.cc)", url)
        if len(url_new2)>0:
            # print(url_new2[0])
            if url_new2[0] not in url_list:
                url_list.append(url_new2[0])
        else:
            url_new1 = re.findall(r"(.*.com)", url)
            if len(url_new1)>0:
                # print(url_new1[0])
                if url_new1[0] not in url_list:
                    url_list.append(url_new1[0])
            else:
                url_new3 = re.findall(r"(.*.cn)", url)
                if len(url_new3)>0:
                    # print(url_new3[0])
                    if url_new3[0] not in url_list:
                        url_list.append(url_new3[0])
                else:
                    url_new4 = re.findall(r"(.*.net)", url)
                    if len(url_new4)>0:
                        # print(url_new4[0])
                        if url_new4[0] not in url_list:
                            url_list.append(url_new4[0])
                    else:
                        url_new5 = re.findall(r"(.*.org)", url)
                        if len(url_new5) > 0:
                            # print(url_new5[0])
                            if url_new5[0] not in url_list:

                                url_list.append(url_new5[0])
                        else:
                            url_new6 = re.findall(r"(.*.cc)", url)
                            if len(url_new6) > 0:
                                # print(url_new6)
                                if url_new6[0] not in url_list:
                                    url_list.append(url_new6[0])
    i = 0
    for url in url_list:
        print(url)
        # 将需要重写的地址写入url_need_write文件中，然后按匹配规则进行xpath规则书写
        f2.write(url + "\n")
        f2.close()
        i+=1
    print(i)

