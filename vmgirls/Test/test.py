# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : test.py
# @Time : 2022/11/17 0017 21:14
# @Software : PyCharm

import re

import requests

head = {
    # 注意不能有空格
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/103.0.0.0Safari/537.36"
}


def main():
    # 获得网页
    resp = requests.get('https://www.vmgirls.com/pure/', headers=head)
    html = resp.text
    # print(html)
    # with open('html.txt', 'wb') as f:
    #     f.write(resp.content)
    #     f.close()
    # 解析网页 取到图片链接
    # re.compile(r'https://www.lz13.cn/[^\s]+.html')
    # HrefAndDir_names = re.findall('<a href="(.*?)" title="(.*?)" class="list-title h-2x">(.*?)</a>', html)
    # re_tag = re.compile(r'https://www.vmgirls.com/[\d]+.html')  # 应该找出所有的超链接
    re_tag = re.compile(r'https://www.vmgirls.com/[\d]+.html')
    HrefAndDir_names = re_tag.findall(html)
    print(HrefAndDir_names)
    # for i in range(len(HrefAndDir_names)):
    #     # print(f"[+]Href[{i + 1}]:\"{HrefAndDir_names[i][0]}\" And Name:{HrefAndDir_names[i][-1]}")
    #     print(HrefAndDir_names[i])
    print(len(HrefAndDir_names))


if __name__ == '__main__':
    main()
