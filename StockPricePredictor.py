# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:46:35 2018

@author: Pulkit Garg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

"""
This function reads in the whole csv file and places it in a dicctionary with
the dates as its key values.

@author Tye Borden
"""
def wholeStock():
    try:
        
        addLines = {}   
        fileName = input('What file would you like to analyze?') 
        with open(fileName) as csvFile:
            
            for row in csvFile:
                lineStripped = row.strip()
                line = lineStripped.split(',')
                addLines[line[0]] = line[1:len(line)]
            addLines.pop('Date')
            return addLines
        
    except IOError:
        print('Cannot open file!\n'
              'File maynot exist! ')
"""
This function reads in a given csv file for a stock and returns a dictionary
of all data between the requested dates.

@author Tye Borden
"""
def dateRange():
    try:
        
        fileName = input('What file would you like to see?')
    
        print('What date range whould you like to see? ex yyyy-mm-dd')
        start = input('From: ')
        end = input('To: ')
        addLines = {}
        switch = False
    
        with open(fileName) as csvFile:
            for  row in csvFile:
                lineStripped = row.strip()
                line = lineStripped.split(',')
                if line[0] == start:
                    addLines[line[0]] = line[1:len(line)]
                    switch = True
                elif switch == True:
                    addLines[line[0]] = line[1:len(line)]
                    if line[0] == end:
                        switch = False
        
            return addLines    
                
                
    except IOError:
        
        print('Cannot open file!')
    except:
        print('No such date!')

print('A program to predict if the price of the stock will go up or not')

print('Please choose from the following companies')
print('1. Google')
print('2. Apple')
print('3. Facebook')
print('4. Goldman Sachs')
print('5. Walmart')
print('6. General Motors')

choice = input("Please choose one of the above ")
 
data = pd.read_csv('Google Stock Market Data.csv')
print(data)
data.head()
data['Date'] = pd.to_datetime(data['Date'].values)
date = data['Date'].values
price = data['Close'].values
plt.plot(date, price)
plt.title("Stock's closing price over time")
plt.xlabel('Year')
plt.ylabel('Price in USD')
plt.legend(['Google'])
plt.axis(['2004', '2015', 0, 1300])
plt.show()




