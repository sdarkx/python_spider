# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# def main():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     ans = 0
#     for i in range(n - 1):
#         if (arr[i] & ans) < (arr[i + 1] & ans):
#             continue
#         else:
#             temp = 1
#             for _ in range(99999):
#                 while temp & ans:
#                     temp <<= 1
#                 if arr[i] & (temp + ans) < arr[i + 1] & (temp + ans):
#                     break
#                 else:
#                     temp <<= 1
#         ans += temp
#         print(ans, end=' ')
#     print(ans, end='')
#
#
# if __name__ == '__main__':
#     main()

import os

a = 100


def solve():
    print("solve %d" % a)


# 在函数中修改全局变量

def solve():
    global a  # 使用全局的a
    print(a)
    a = 111
    print(a)
    a = 222
    print(a)


# read读取指定字符，每读取一次向后移动多少个字符
def solve():
    f = open("test.txt", "r")
    # s = f.read(3)
    # print(s, end='')
    # s = f.read(12)
    # print(s)

    # os.rename()

    s = f.readlines()
    # print(s) # ['Hello World!'] 文件内全部读进来
    for i in s:
        print(i)
    f.close()


def solve():
    try:
        # print(x)
        f = open("1.txt", "r")  # 打开一个不存在的文件异常捕获
        # try except 嵌套
    except (IOError, NameError) as res:
        print("IOError")
        print(res)
        # IOError
        # name 'x' is not defined
        # 捕获所有的异常 Exception 所有异常父类
    finally:
        print("都会执行")


def solve():
    pass


def solve():
    solve()


def solve():
    a, b = map(float, input().split(" "))
    print("%.3f" % (a / b))
    print(int(b * 2))


def main():
    pass


if __name__ == '__main__':
    main()
