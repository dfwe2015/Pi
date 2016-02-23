# -*- coding: gbk -*-

"""����csv�ļ�,�ҵ����ʵ���"""

import csv
import os, sys

import modify_ip


class CsvMatch(object):
    """��ip��ַ�ַ������бȶ�csv�ļ���ǰ���У�
    �õ��׸�ƥ����У��Լ���һ�У�title�У�"""
    def __init__(self, ip_str):
        # url = os.path.split(sys.argv[0])[0] + os.sep + 'IP.csv'
        # url = 'C:\Users\Rob\OneDrive\PycharmProjects\Pi\pi\IP.csv'
        # print(sys.path)
        url = sys.path[0] + os.sep + 'IP.csv'
        print(url)

        with open(url, 'rb') as csv_file:
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
