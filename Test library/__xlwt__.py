# -*- coding = utf-8 -*-
# @Author : x_DARK_
# @File : __xlwt__.py
# @Time : 2022/8/9 10:20
# @Software : PyCharm


import xlwt

'''
workBk = xlwt.Workbook(encoding="utf-8")  # 创建workBook对象
worksheet = workBk.add_sheet('sheet_1') # 创建工作表
worksheet.write(0,0,'hello')  # 写入数据(行，列，内容)
workBk.save('stu.xls') # 保存数据表
'''


def main():
    work = xlwt.Workbook(encoding='utf-8')
    multiplication_table = work.add_sheet('multiplication')
    for i in range(1, 10, 1):
        for j in range(1, i + 1, 1):
            multiplication_table.write(i - 1, j - 1, str(j) + " * " + str(i) + " = " + str(i * j))
    work.save('multiplication.xls')


if __name__ == '__main__':
    main()
