# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __gs__.py
# @Time : 2022/6/30 20:09
# @Software : PyCharm


def read():
    try:
        f = open("gs.txt", "r")
        try:
            s = f.readlines()
            # write(s) 报错
            for i in s:
                write(i)
        except IOError:
            print("?")
        f.close()
    except IOError:
        print("Fail")


def write(s):
    try:
        w = open("cp.txt", "a")
        try:
            w.write(s)
        except IOError:
            print("w, f")
        w.close()
    except IOError:
        print("IO_F")


if __name__ == '__main__':
    read()
