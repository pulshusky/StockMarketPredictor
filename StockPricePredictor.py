# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:46:35 2018

@author: Pulkit Garg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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




