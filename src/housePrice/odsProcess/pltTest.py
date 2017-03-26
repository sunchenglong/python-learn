# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import MySQLdb
window = 30
db = MySQLdb.connect("localhost", "root", "root", "house")
db.set_character_set('utf8')
cursor = db.cursor()
fig, ax = plt.subplots()
SQL = "select dealDate, region, avg(totalPrice), avg(totalPrice/square) from ods_house_new  \
      where (region = 'BJXC' or region = 'BJCP' or region = 'BJFT') AND dealDate > '2012.01.01' \
      group by dealDate, region"
cursor.execute(SQL)
rows = cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'date', 1: 'region', 2: 'price', 3: 'pricePerA'}, inplace=True)
#df.plot()
groups = df.groupby('region')
for name, group in groups:
    if name =='BJFT':
        #ax.plot(np.array(pd.to_datetime(group.date)), np.array(pd.rolling_mean(group.pricePerA,window)), 'k.', label="fengtai", color= 'blue')
        pass
    else:
        pass
        #ax.plot(np.array(pd.to_datetime(group.date)), np.array(pd.rolling_mean(group.pricePerA,window)), 'k.', label="changping", color= 'blue')
SQL = "select dealDate,area as region, avg(totalPrice), avg(totalPrice/square) from ods_house_new where (area like '%银地%' or area like '%南庭%' ) AND dealDate > '2012.01.01' group by dealDate, area"
print SQL
#or area like '%天伦%'
cursor.execute(SQL)
rows = cursor.fetchall()

df2 = pd.DataFrame( [[ij for ij in i] for i in rows] )
df2.rename(columns={0: 'date', 1: 'region', 2: 'price', 3: 'pricePerA'}, inplace=True)
print df2
groups = df2.groupby('region')
index = 0

for name, group in groups:
    if index == 1:
        ax.plot(np.array(pd.to_datetime(group.date)), np.array(pd.rolling_mean(group.pricePerA,window)), 'k--', label="rongfeng", color= 'm')
    else:
        ax.plot(np.array(pd.to_datetime(group.date)), np.array(pd.rolling_mean(group.pricePerA,window)), 'k--', label="jintaixili", color= 'r')
    index += 1



SQL = "select dealDate,area as region, avg(totalPrice), avg(totalPrice/square) from ods_house_new where  dealDate > '2012.01.01' AND room < 30  group by dealDate, area"
print SQL
cursor.execute(SQL)
rows = cursor.fetchall()

df3 = pd.DataFrame( [[ij for ij in i] for i in rows] )
df3.rename(columns={0: 'date', 1: 'region', 2: 'price', 3: 'pricePerA'}, inplace=True)
#print df3
groups = df3.groupby('region')
index = 0
for name, group in groups:
    #print name
    pass
#for name, group in groups:
#    if index == 1:
#        ax.plot(np.array(pd.to_datetime(group.date)), np.array(pd.rolling_mean(group.pricePerA,window)), 'k--', label="area", color= 'm')
#    else:
#        ax.plot(np.array(pd.to_datetime(group.date)), np.array(pd.rolling_mean(group.pricePerA,window)), 'k--', label="area", color= 'yellow')
#    index += 1


legend = ax.legend(loc='upper center', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width
plt.show()
