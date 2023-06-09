# This file is created to test the MAIVE package

# from maive.maive import Maive

# import maive 

from maive.maive import Maive

m = Maive()


import pandas as pd
import numpy as np

# data = pd.read_csv('testData1.csv')

# x = data[['size','year']]
# y = data['price']


# test = m.LinearRegression(x,y)

# print(m.r2(test, x.values.reshape(-1,1), y))
# print(m.regressionReport(x.values.reshape(-1,1), y))

# t = m.scatterPlot(x,y, "Size", "Price", "Linear Regression")

# t = m.summaryTable(x, y)

# print(t)

# x = [
#     [23,2,5,3224,2,234,234,2423,4],
#     [23,2,5,3224,2,234,234,2423,4],
#     [23,2,5,3224,2,234,234,2423,4],
#     [23,2,5,3224,2,234,234,2423,4],
#     [23,2,5,3224,2,234,234,2423,4],
#     [23,2,5,3224,2,234,234,2423,4],
#     [23,2,5,3224,2,234,234,2423,4],
#     ]
# y = [23,2,5,3224,2,234,234,2423,4]

# t = m.createCSV('csvdata.csv',y)


# t = m.featureScaling(x)

# print(t)


# data = pd.read_csv('testData2.csv')
# t = m.elbowMethod(data)


data = np.load("testData3.npz")




