# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:46:35 2018

@author: Pulkit Garg
"""

import csv

print('A program to predict if the price of the stock will go up or not')

print('Please choose from the following companies')
print('1. Google')
print('2. Apple')
print('3. Facebook')
print('4. Goldman Sachs')
print('5. Walmart')
print('6. General Motors')

choice = input("Please choose one of the above ")



# initializing the titles and rows list
fields = []
rows = []
 
# reading csv file
with open("Google Stock Market Data.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    for row in reader:
        print(" ".join(row))





