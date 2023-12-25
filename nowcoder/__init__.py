# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : main.py.py
# @Time : 2022/8/9 11:03
# @Software : PyCharm

from pprint import pprint
import bs4  # 网页解析获取数据
import re  # 正则表达式文字匹配
import urllib  # 制定URL获取网页数据
import urllib.request
import xlwt  # 进行excel操作
import sqlite3  # 数据库操作


def main():
    baseUrl = "https://ac.nowcoder.com/acm/problem/2000"  # https://ac.nowcoder.com/acm/problem/20000
    savePath = "now_coder.xls"

    # 爬取数据
    dateList = getDate(baseUrl)
    pprint(dateList)

    # 保存数据
    # saveDate(dateList, savePath)


def getDate(baseUrl):
    datas = []

    for i in range(0, 1, 1):
        url = baseUrl + str(i)
        html = askUrl(url)
        pprint(html)

        # 逐一解析数据
        # soup = bs4.BeautifulSoup(html, "html.parser")
        # for item in soup.find_all('div', class_="item"):
        #     pass

    return datas


def askUrl(url):
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        # "Cookie": "NOWCODERUID=1B2CDC63B0F1B5C6150D92543D347EE8;NOWCODERCLINETID=EB53E606FBAC28DB9A9BD2C8A8AC73D0;Hm_lvt_a808a1326b6c06c437de769d1b85b870=1653779632,1653780747,1653789831,1653794614;gr_user_id=ebc42253-4f8f-43c1-94e2-8bf0468cb6b1;c196c3667d214851b11233f5c17f99d5_gr_last_sent_cs1=523588061;ssxmod_itna=eqUxg7eQqWqDqhxl4iuitD909eGQzDBigBBo2ABG40yDpeGzDAxn40iDtoaTPUI7qeFNWGh00xtRi0PRIKb2fFTf7mDB3DEx0=PvnYxiigDCeDIDWeDiDGbtDFxYoDeoHQDFF5X/ZcpxAQDQ4GyDitDKq0VDG3D08=q/O=SnRiDreDSWGUxK7=DjqGgDBdKYchcDDUbNcxDbhpRY…c629b9caa86c67c88e7f8a6f36fac8bffa9b763a8a6a584e479889ca18eea4e8f8c85bbae4b94ec849bf2408cebf88bed60afb8ba8de663899d8d87eb3db7f0b9a8c767938e85d1eb479c90fcbae87bb5a7be90c43e958eae96f246aeb689b2e47394b181aaf646fbeff7add35af78aaea6c25297b49fccd080a8f1adb8d437e2a3;YD00000586307807%3AWM_TID=hyzyxrzTa15AFQVFRAKEVx%2FUeaMwy%2Bfo;t=1B012FCF563BB01D64B97009B230CF24;from=acdiscuss;acw_tc=707c9fd716613322167305663e7bb0050e0c772517954fefb67e03357b2130;SERVERID=b929f4463c6f3dd15e635f802ff2ab92|1661332217|1661332216"
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveDate(dateList, savePath):
    pass


if __name__ == '__main__':
    main()
