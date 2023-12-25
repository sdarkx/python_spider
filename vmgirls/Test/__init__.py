# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __init__.py
# @Time : 2022/11/17 0017 21:11
# @Software : PyCharm

import re

import requests

head = {
    # 注意不能有空格
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/103.0.0.0Safari/537.36"
}


def main():
    # 获得网页
    response = requests.get('https://www.vmgirls.com/20529.html', headers=head)
    html = response.text
    # 解析网页 取到图片链接
    dir_name = re.findall('<h1 class="post-title mb-3">(.*?)</h1>', html)[-1]
    urls = re.findall('<a rel="(.*?)" href="(.*?)" alt=".*?" title=".*?">', html)


if __name__ == '__main__':
    main()
