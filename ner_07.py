from grammer.rules import grammer_parse

fp = open("car_news_data_cleanout.txt", "r", encoding="utf-8")
fout = open("out.txt", "w", encoding="utf-8")

# [grammer_parse(line.strip(),fout) for line in fp if len(line.strip())>0]

for line in fp:
    if len(line.strip()) > 0:
        grammer_parse(line.strip(), fout)

fout.close()

if __name__ == "__main__":
    pass
