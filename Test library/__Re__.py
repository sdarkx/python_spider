# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __Re__.py
# @Time : 2022/8/9 9:09
# @Software : PyCharm

import re

# print(re.findall("[a-z]", "AsadfnsaeionFSAODNW"))
# ['s', 'a', 'd', 'f', 'n', 's', 'a', 'e', 'i', 'o', 'n']

# print(re.findall("[a-z]+", "AsadfnsaeionFSAODNW"))
# ['sadfnsaeion']

# print(re.sub("a","A","applause"))
# 找到a用A替换


# 建议在正则表达式中，被比较的字符串加上r，不用担心转义字符问题
# a = r"a\de\afe\fc"
# print(a)  # a\de\afe\fc
