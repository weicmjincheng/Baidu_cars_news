file = r"E:\Html-cheyin-data\baidu_cars_news\entity_json.txt"
with open(file, "r+", encoding='UTF-8', errors='ignore') as f1:
    lines = f1.readlines()
    # print(lines[0])
    entity_set = []
    for line in lines:
        # print(line)
        line = line.replace("{","").replace("}","").replace('"',"").replace('"',"").replace(":","").replace("loc","").replace("org","").replace(",","").strip()
        if len(line)!=0:
            line_list = line.split(" ")
            # print(line.split(" "))
            for line in line_list:
                # print(line)
                if line not in entity_set:
                    entity_set.append(line)
                    f2 = open(r"E:\Html-cheyin-data\baidu_cars_news\entity.txt", 'a+', encoding='utf-8')
                    f2.write(line+"\n")
                    f2.close()

    for i in entity_set:
        print(i)