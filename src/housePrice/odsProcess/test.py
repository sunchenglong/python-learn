
# -*- coding: utf-8 -*-
import pylab as pl
x = range(10) 
y = [i*i for i in x]
z = [i*i*i for i in x]

#pl.plot(x, y, label='x2')
#pl.plot(x, z, label='x3')

#pl.show()


import matplotlib.pyplot as plt
import pandas as pd
import ipykernel
import jupyter_client
import MySQLdb
db = MySQLdb.connect("localhost", "root", "root", "house")
db.set_character_set('utf8')
cursor = db.cursor()
SQL = "select dealDate, region, avg(totalPrice), avg(totalPrice/square) from ods_house_new  \
      where (region = 'BJXC' or region = 'BJCP' ) AND dealDate > '2012.01.01' \
      group by dealDate, region"
cursor.execute(SQL)
rows = cursor.fetchall()
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'date', 1: 'region', 2: 'price', 3: 'pricePerA'}, inplace=True)
#df.plot()
groups = df.groupby('region')
index = 0
for name, group in groups:
    pl.plot(pd.to_datetime(group.date), group.pricePerA)
    index += 1

SQL = "select dealDate,area as region, avg(totalPrice), avg(totalPrice/square) from ods_house_new where (area like '%新龙城%' or area like '%荣丰%') AND dealDate > '2012.01.01' AND room < 20  group by dealDate, area"
print SQL
cursor.execute(SQL)
rows = cursor.fetchall()

df2 = pd.DataFrame( [[ij for ij in i] for i in rows] )
df2.rename(columns={0: 'date', 1: 'region', 2: 'price', 3: 'pricePerA'}, inplace=True)
#df.plot()
print df2
groups = df2.groupby('region')
for name, group in groups:
    pl.plot(pd.to_datetime(group.date), group.pricePerA)
    index += 1

pl.show()