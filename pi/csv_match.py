# -*- coding: utf-8 -*-

"""处理csv文件,找到合适的行"""

import csv

from pi import modify_ip


class CsvMatch(object):
    """用ip地址字符串逐行比对csv文件的前两列，
    得到首个匹配的行，以及第一行（title行）"""
    def __init__(self, ip_str):
        with open('IP.csv', 'rb') as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
            self.first_row = spam_reader.next()[0].split(',')
            self.row = None
            for row in spam_reader:
                row = row[0].split(',')
                if modify_ip.compare_ip(row, ip_str):
                    print("---Get a row!---\n")
                    self.row = row
                    break


    def get_csv_row(self):
        return self.row

    def get_csv_title(self):
        return self.first_row
