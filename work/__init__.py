# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __init__.py.py
# @Time : 2022/9/27 13:38
# @Software : PyCharm

from openpyxl import load_workbook
import os


class StuList:
    name = ""
    id = ""
    checked = False


# 配置所有学生名单并选择表
listURL = r"C:\Users\Lenovo\Documents\RB软工移213名单.xlsx"
wsheet = load_workbook(listURL)['RB软工移213点名表']
# 一，创建学生集合并把读到的学生信息加载入内存
allStu = []
tmp = StuList
for row in wsheet.rows:
    tmp.name = row[2].value  # 学生姓名
    tmp.id = row[5].value  # 学生学号
    allStu.append(tmp)
    tmp = StuList()
# 二，对输入的文件夹进行格式化存储对象
# Hwdir = input("[*] 作业的目录在哪儿？")
Hwdir = r"C:\Users\Lenovo\Desktop\Files\临时处理文件夹\net"
if not os.path.exists(Hwdir):
    print("[-] 路径不存在！")
    exit(0)
else:
    fileCol = os.listdir(Hwdir)
    for cell in allStu:  # cell代表每个学生
        print(cell.name + "  " + cell.id + "  " + str(cell.checked))
        for x in fileCol:  # x代表每个文件名
            if x.__contains__(cell.id) or x.__contains__(cell.name):
                cell.checked = True
                break
# 三，循环完毕，对结果整理
sumall = len(allStu)
sumed = 0
sumno = 0
print("[+] 已提交作业同学名单：")
for x in allStu:
    if x.checked:
        print("\t[+] ", x.name, "已提交作业")
        sumed += 1
notSubmit = []
print("[-] 未提交作业同学名单：")
for x in allStu:
    if not x.checked:
        print("\t[-] ", x.name, "未提交作业")
        notSubmit.append(x.name)
        sumno += 1
print("{1}人已提交作业，{2}人未提交作业，总人数为{3}人".format(sumed, sumed, sumno, sumall))
choice = input("[*] 是否要将未提交同学输出？(1/0)")
if int(choice) == 1:
    for x in notSubmit:
        print(x)
