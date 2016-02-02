# -*- coding: utf-8 -*-

import csv

def getrowlist():
    with open('IP.csv', 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
             row = row[0]
             rowlist = row.split(',')
             yield rowlist
             # 返回包含csv文件每行内容的生成器
             # 每行的格式为：起始ip，结束ip，网关地址


# print(getRow())
# for i in getRow():
#     print(i)