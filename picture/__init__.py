# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : main.py.py
# @Time : 2022/8/22 21:25
# @Software : PyCharm

import requests
import re
import os


def main():
    # 设置全局变量
    aSear, page = "city", 1
    aua = {
        "referer": "https://wallhaven.cc/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
    }
    aURL = "https://wallhaven.cc/search?q={0}&page={1}".format(aSear, page)
    # print(aURL)保留测试
    rText = requests.get(aURL, headers=aua).text  # 请求搜索数据并保存到rtext
    aLinks = re.findall(r'<a class="preview" href="(.*?)"', rText)  # 包含详情页列表
    print("[+]爬取到{}张壁纸！".format(len(aLinks)), aLinks)
    for items in aLinks:
        print(items)

    # 校验本地是否存在wallpaper文件夹
    if os.path.exists("wallpapers"):
        pass
    else:
        os.makedirs("wallpapers")
    # 校验结束

    for x in aLinks:  # x为一个壁纸的详情页链接
        print("[*]在{}中寻找...".format(x))
        subtext = requests.get(url=x, headers=aua).text  # 详情页地址（包含图片地址，名称）
        # print(subtext)
        img_src = re.findall(r'< img id="wallpaper" src="(.*.jpg)"[\w\d\s]*?alt="(.*?)"', subtext)  # 返回图片(地址,名称)元组的列表
        for single in img_src:  # 解析列表，single为元组
            fileName = r".\wallpapers\{}.jpg".format(single[1])
            with open(fileName, "wb") as down:
                imageBytes = requests.get(url=single[0], headers=aua).content
                down.write(imageBytes)
            print("[+]{}下载完成！".format(single[1]))
    print("[*]爬取完毕！")


if __name__ == '__main__':
    main()

