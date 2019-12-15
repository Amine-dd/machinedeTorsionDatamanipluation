# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:45:28 2019

@author: pc
"""

import pandas as pd
df = pd.read_csv('data.csv')
import re

data = []
with open("data.csv", "r") as csvfile:
    for line in csvfile:
        data.append(re.split("[\t\t\n]", line)[:-1])
        
df1 = pd.DataFrame(data)
##df1 = df1.dropna(axis='columns')
cols = [1,3,5,7,9,11,13,14,15,16,17,18]
df1.drop(df1.columns[cols],axis=1,inplace=True)
df1.drop([0,1],inplace = True)
df1.columns = ["Load","Extension","Broadwise Extension","Displacement","Stress","Strain","Time"]
import matplotlib.pyplot as plt
fig1 = plt.plot(df1['Displacement'],df1['Stress'],linestyle='-',c='red')
plt.xlabel('Displacement')
plt.ylabel('Stress')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])
plt.show()
fig2 = plt.plot(df1['Extension'],df1["Strain"],linestyle='-',color='blue')
plt.xlabel('Extension')
plt.ylabel('Strain')
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([])
frame.axes.get_yaxis().set_ticks([])
plt.show()