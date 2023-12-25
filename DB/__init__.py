# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : main.py
# @Time : 2022/8/1 11:07
# @Software : PyCharm
from pprint import pprint

import bs4  # 网页解析获取数据
import re  # 正则表达式文字匹配
import urllib  # 制定URL获取网页数据
import urllib.request
import xlwt  # 进行excel操作
import sqlite3  # 数据库操作


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    savePath = ".\\db top250.xls"

    # 1.爬取网页
    dateList = getDate(baseUrl)

    # 2.解析数据
    # getDate(baseUrl)

    # 3。保存数据
    saveDate(dateList, savePath)

    # test
    # baseurl = "https://movie.douban.com/top250?start="
    # askURL(baseurl)


# 全局表达式匹配规则
findLink = re.compile(r'<a href="(.*?)">')
# image
findImgSrc = re.compile(r'<img.*src="(.*?)" ', re.S)  # .S忽略换行符
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findPeople = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findIntro = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片相关内容
findMovInfo = re.compile(r'<p class="">(.*?)</p>', re.S)


def getDate(baseUrl):
    dates = []
    # 解析数据
    for i in range(0, 10):  # 左闭右开
        url = baseUrl + str(i * 25)  # 每个页面展示25项内容
        html = askURL(url)  # 保存获取到的网页源码
        # print(html)

        # 逐一解析
        soup = bs4.BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item) 测试查看信息
            data = []  # 保存一部电影的信息
            item = str(item)
            # 获取到影片超链接
            # link = re.findall(findLink, item)[0]  # 用re库通过正则表达式查找指定的字符串[0]表示只要第一个
            # print(link)

            link = re.findall(findLink, item)[0]
            data.append(link)

            image = re.findall(findImgSrc, item)[0]
            data.append(image)

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                title = titles[0]
                data.append(title)
                title = titles[1].replace("/", "")
                data.append(title)
            else:
                data.append(titles[0])
                data.append(' ')  # 第二名称即使没有也要留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            jpn = re.findall(findPeople, item)[0]
            data.append(jpn)

            intro = re.findall(findIntro, item)
            if len(intro) != 0:
                data.append(intro[0].replace("。", ""))
            else:
                data.append(" ")

            moveInfo = re.findall(findMovInfo, item)[0]
            moveInfo = re.sub('<br(\s+)?/>(\s+)?', ' ', moveInfo)  # 去掉<br>
            moveInfo = re.sub('/', ' ', moveInfo)  # 替换/
            data.append(moveInfo.strip())  # 去掉空格
            dates.append(data)
    # pprint(dates)
    return dates


# 得到指定一个url的网页信息
def askURL(url):
    # 模拟浏览器头部信息,向豆瓣服务器发送西
    head = {
        # 注意不能有空格
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/103.0.0.0Safari/537.36 "
    }
    # 用户代理,表示告诉服务器,我们是什么类型的机器,浏览器(本质是告诉浏览器我们能接受什么水平的信息)
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveDate(datalist, savePath):
    DK = xlwt.Workbook('utf-8')
    sheet = DK.add_sheet('Top250', cell_overwrite_ok=True)

    col = ('电影详链接', '图片链接', '影片名称', '影片外文名', '评分', '评价数', '概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])

    for i in range(0, 250):
        print("Number %d" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    # DK.save('top250.xls')
    DK.save(savePath)


if __name__ == "__main__":
    main()
