# 获得所有对应标签当前页面的url  然后转example01
import requests
from lxml import etree
from selenium import webdriver
# 图形界面版
# from selenium.webdriver.chrome.options import Options
from time import sleep

# 需要加动态代理和头信息（06.09测试发现全部被拒绝）

# 图形界面版
# chrome_options = Options()
# # 打开安装的exe文件  打开浏览器
# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='E:\chromedriver.exe')

# 非图形界面版
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option, executable_path='E:\chromedriver.exe')

# driver.maximize_window()
# 打开网页
driver.get('https://www.baidu.com')
sleep(3)
# '奥迪', '宝马', '保时捷', '奔驰', '吉普', '三菱', '现代', '本田', '比亚迪', '标致', '别克', '宾利', '福特', '铃木', '马自达', '雪铁龙', '法拉利',
# '丰田', '红旗', '凯迪拉克', '兰博基尼','劳斯莱斯', '玛莎拉蒂''宝骏', '奔腾', '宾利', '拜腾', '长安', '长城', '大众', '东风', '福田', '广汽传祺', '观致', '哈弗',
# '红旗', '海马', '悍马', '吉利汽车',  '路虎', '铃木', '林肯', '雷诺', '猎豹汽车', '名爵', '迈巴赫', '奇瑞', '起亚', '日产', '荣威', '三菱',
# '斯柯达', '斯巴鲁', '上汽大通','Jeep','捷豹', '江淮', '金杯', '捷途','雷克萨斯','特斯拉', '沃尔沃', '五菱汽车', '五十铃', '雪佛兰',
list_car = ['大众', '东风']
# , , '福田', '广汽传祺','奔驰', '吉普', '三菱'
#   '现代', '本田', '比亚迪', '标致', '别克', '宾利', '福特', '铃木', '马自达',
#,'观致', '哈弗', '奥迪', '宝马', '保时捷','雪铁龙', '法拉利','Jeep'
# print(len(list_car))
# 上汽大通发动机涉水险开始没有做成功 结束后重做
# 多线程爬虫
# 关键词  租赁  抵押   投资   贷款   税收   保险  代表人   销量   总部  系列产品  金融  车祸  分期购  O2O  4s店  性价比   业内评价
# 市场份额  发展前景    财务报告    股票   利润  首付    二手车    售价    性能  外观  安全性能   油耗  售后服务     分时租赁
# '交强险', '保险', '车险', '机动车辆损失险', '第三者责任险', '车上人员责任险', '发动机涉水损失险', '自燃损失险', '盗抢险', '玻璃单独破碎险', '车身划痕损失险','不计免赔率特约险'
list_insurance = ['租赁', '抵押', '投资', '贷款', '税收', '保险', '代表人', '销量', '总部', '系列产品', '金融', '车祸', '分期购', 'O2O', '4s店', '性价比',
                  '业内评价',
                  '市场份额', '发展前景', '财务报告', '股票', '利润', '首付', '二手车', '售价', '性能', '外观', '安全性能', '油耗', '售后服务', '分时租赁']
# print(len(list_insurance))
list = []
for car in list_car:
    for insurance in list_insurance:
        input_kw = car + insurance
        # print(input_kw)
        list.append(input_kw)
f2 = open(r"E:\Html-cheyin-data\url44444444.txt", 'a+', encoding='utf-8')
for i in list:
    # 查看源码  找到输入框对应的位置   使用关键字查找的方式定位指定位置
    # 因为循环使用  所以需要每次定期刷新输入框位置
    input = driver.find_elements_by_id("kw")
    # 在输入框中输入需要查找的内容
    print(i)

    try:
        input[0].send_keys(i)
        # 点击百度一下按钮  如果直接以下面新闻形式访问 输入框会有下拉框  会点击错误报错
        driver.find_element_by_id("su").click()
        # 百度一下以后再点击新闻标题页面
        driver.find_element_by_link_text(u"新闻").click()

        list_url = []


        def get_all_page():
            url = driver.current_url
        # print(url)
            list_url.append(url)
        # 获取当前页面下所有网页的地址
            html = requests.get(url).text
        # print(html)
            sel = etree.HTML(html)  # 解析html源代码
        # //div[@id="content_left"]/ul/li/h3/a/@href 加|或形式主要是因为有的浏览器关闭再打开就会改变xpath规则
            title_list = sel.xpath('//div[@id="content_left"]/ul/li/h3/a/@href|//div[@class="result"]/h3/a/@href')

        # 拿到对应每个网址下面的文本内容
            for list in title_list:
                print(list)
                f2.write(list + "\n")
                f2.close()
        # 下一页机制
            try:
                next_page = driver.find_element_by_link_text(u"下一页>")
            except Exception:
                print("没有下一页，跳出循环")
                return
            else:
                # sleep(5)
                if next_page is not None:
                    next_page.click()
                    get_all_page()


        get_all_page()
        url_len = len(list_url)
        print(url_len)
    except Exception:
        print("报错继续执行")
        sleep(20)
    # 跳出循环应该是它前进多少页然后对应回退
    sleep(3)
    # 回退两次到初始的百度输入界面
    for i in range(url_len + 1):
        driver.back()
    sleep(3)
