# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __init__.py
# @Time : 2022/11/17 0017 19:32
# @Software : PyCharm

import os
import time

import requests
import re

head = {
    # 注意不能有空格
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/103.0.0.0Safari/537.36"
}


def any_html(url_html):
    # 获得网页
    # response = requests.get('https://www.vmgirls.com/20529.html', headers=head)
    response = requests.get(url_html, headers=head)
    html = response.text
    # 解析网页 取到图片链接
    dir_name = re.findall('<h1 class="post-title mb-3">(.*?)</h1>', html)[-1]
    urls = re.findall('<a rel="(.*?)" href="(.*?)" alt=".*?" title=".*?">', html)
    # 保存图片的位置
    path = r'F:\WorkSpace\pythonfile\vmgirls\img\\' + dir_name  # 写道指定文件夹
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    # 保存图片 count 成功下载图片数量
    count = 0
    for i in range(len(urls)):
        time.sleep(1)
        img_name = str(i + 1) + '-' + urls[1][1].split('/')[-1]
        any_path = path + '\\' + img_name  # 写道指定文件夹
        flag = False
        with open(any_path, "wb") as down:
            resp = requests.get(urls[i][1], headers=head)
            down.write(resp.content)
            down.close()
            flag = True
            count += 1  # python 中的数据类型不具备自增的功能 每有一个新的数据 都会申请一个新的内存来存储
            print(f"[+]{{img_name}}Download complete!")
        if not flag:
            print(f"[+]{{img_name}}Download failed!")
    print(f"[=]Successfully downloaded [{count}] picture")


def main():
    resp = requests.get('https://www.vmgirls.com/pure/', headers=head)
    html = resp.text
    re_tag = re.compile(r'https://www.vmgirls.com/[\d]+.html')
    HrefAndDir_names = re_tag.findall(html)
    for i in range(len(HrefAndDir_names)):
        time.sleep(1)
        any_html(HrefAndDir_names[i])
        print(f"[=====] Page {i + 1} complete")


if __name__ == '__main__':
    main()
