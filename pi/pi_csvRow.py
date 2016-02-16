# -*- coding: utf-8 -*-

"""处理csv文件,找到合适的行"""

import csv
import pi_modifyIP


class Row(object):
    """用address ip地址逐行比对csv文件的前两列"""
    def __init__(self, ip_str):
        with open('IP.csv', 'rb') as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
            self.first_row = spam_reader.next()[0].split(',')
            self.row = None
            for row in spam_reader:
                row = row[0].split(',')
                if self.compare_ip(row, ip_str):
                    print("---Get a row!---\n")
                    self.row = row
                    break

    @staticmethod
    def compare_ip(ip_list, ip_str):
        if pi_modifyIP.ip2int(ip_list[0]) <= pi_modifyIP.ip2int(ip_str) <= pi_modifyIP.ip2int(ip_list[1]):
            return ip_list

    def get_row(self):
        return self.row

    def get_first_row(self):
        return self.first_row
