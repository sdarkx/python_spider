# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __Urllib__.py
# @Time : 2022/8/1 11:47
# @Software : PyCharm
import urllib.request
from urllib import request

# get请求
# cons = urllib.request.urlopen("http://www.baidu.com")
# print(cons.read().decode('utf-8'))
# 加.decode('utf-8') 解析返回 对获取到的网页源码进行utf-8解码


# post请求
# http://httpbin.org/post
# import urllib.parse
#
# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8") # 按照post方式封装
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)  # 要封装表单包含信息
# print(response.read().decode("utf-8"))
'''
模拟浏览器发出请求
"form": {
    "hello": "world"
  },
'''

# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)  # 超时处理
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")

'''
模拟请求
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.10", 
    "X-Amzn-Trace-Id": "Root=1-62e8c236-18cd2aac2ddbdc442c1da350"
  }, 
  "origin": "39.148.165.21", 
  "url": "http://httpbin.org/get"
}
 浏览器请求
{
  "args": {},
  "headers": {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "httpbin.org",
    "Referer": "http://httpbin.org/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-62e8c267-6da0f533124e534f1a294984"
  },
  "origin": "39.148.165.21",
  "url": "http://httpbin.org/get"
}
'''

# response = urllib.request.urlopen("https://baidu.com")
# response_ = urllib.request.urlopen("https://douban.com") # HTTP Error 418:
# print(response.status)
# print(response.getheaders()) # 多个信息
# print(response.getheader("Server"))  # 具体的一个信息


# 不让别人知道自己是爬虫，伪装成浏览器
# url = "https://douban.com"
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name': 'DARK'}), encoding="utf-8")
# head = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# req = urllib.request.Request(url=url, data=data, headers=head, method="POST")  # 对象包装
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "DARK"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "9", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    // 更像浏览器了
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-62e8c6f9-5ed2bb8f012c90715b14d03a"
  }, 
  "json": null, 
  "origin": "39.148.165.21", 
  "url": "http://httpbin.org/post"
}
'''

# 记
url = "http://douban.com"
head = {
    # headers里面是浏览器信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=head)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
