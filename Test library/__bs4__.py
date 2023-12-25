# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __bs4__.py
# @Time : 2022/8/1 11:35
# @Software : PyCharm


# 帮助我们分析HTML文档
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
# html = file.read()
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")  # html文件,html.parse解析器
'''
# 树形结构

# print(bs.title) # 找到第一个标签并返回 <标签>类型
# print(bs.title.string)  # 百度一下 我就知道 <- 返回标签里面的内容<字符串>类型

# print(bs.a) # 只拿到第一个<a class="mnav" href="http://news.baidu.com" name="tj_trnews"><!-- 新闻 --></a>
# print(bs.a.attrs)  # 拿到一个标签的所有属性 {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}

# print(bs.head)
# print(type(bs.head)) # <class 'bs4.element.Tag'>

# print(type(bs))  # BeautifulSoup 表示整个文档
# print(bs.name) # [document]
# print(bs.attrs) # {}
# print(bs)  # bs就是整个文档

# print(bs.a.string)
# print(type(bs.a.string)) # <Comment>类型，输出内容不包含注释符号
'''

# 文档的搜素 真的会性的拿东西

# 文件树的遍历
# print(bs.head.contents) 返回一个列表
# print(bs.head.contents[1])
# （1）find_all()
# 1 字符串搜索
# t_list = bs.find_all("a")  # 查找标签
# print(t_list)
# 2 正则表达式搜索
# t_list = bs.find_all(re.compile("a"))  # 正则表达式匹配标签及其内容，只要标签含有a
# print(t_list)
# 3 方法 ： 传入一个函数 根据函数的要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name") # 按照这个搜索
# t_list = bs.find_all(name_is_exists)
# print(t_list)

# (2) kwargs 参数搜索
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href="http://news.baidu.com")
# for i in t_list:
#     print(i)

# (3) text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图"])
# t_list = bs.find_all(text=re.compile("\w"))  # \d 表示包含数字 \w 表示字符串 找到所有包含特定文本的内容
# for i in t_list:
#     print(i)


# （4） limit参数
# t_list = bs.find_all("a", limit=3)
# for i in t_list:
#     print(i)


# （5）css选择器
# print(bs.select("title")) # 通过标签查找
# t_list = bs.select(".mnav") # 通过类名查找
# t_list = bs.select("#u1") # 通过id查找
# t_list = bs.select("a[class='bri']") # 通过属性查找
# t_list = bs.select("head > title")  # 通过子标签查找
t_list = bs.select(".mnav ~ .bri")  # 通过子标签查找

print(t_list[0].get_text())

# for i in t_list:
#     print(i, end='\n')

