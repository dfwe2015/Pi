# -*- coding: utf-8 -*-

import pi_compare
import csv

class Row(object):

    def __init__(self):
        with open('IP.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            first_row = spamreader.next()[0].split(',')
            self.first_row = first_row
            for row in spamreader:
                row = row[0].split(',')
                if pi_compare.compareip(row):
                    print("get a row")
                    self.row = row
                    break

    def getFirstRow(self):
        return self.first_row

    def getRow(self):
        return self.row
