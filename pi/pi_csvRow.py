# -*- coding: utf-8 -*-

import pi_compare
import csv


def getRow():
    with open('IP.csv', 'rb') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
         for row in spamreader:
             row = row[0].split(',')
             if pi_compare.compareip(row):
                 return row
