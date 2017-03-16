# -*- coding: utf-8 -*-
import pandas as pd

import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "house")
db.set_character_set('utf8')
cursor = db.cursor()
SQL = "select dealDate, case when region = 'BJXC' then '西城' else '昌平' end, avg(totalPrice), avg(totalPrice/square) from ods_house_new where (region = 'BJXC' or region = 'BJCP' ) AND dealDate > '2012.01.01' group by dealDate, region union select dealDate,area as region, avg(totalPrice), avg(totalPrice/square) from ods_house_new where (area like '%新龙城%' or area like '%荣丰%') AND dealDate > '2012.01.01' AND room < 20  group by dealDate, area"
cursor.execute(SQL)
rows = cursor.fetchall()
df = pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns={0: 'date', 1: 'region', 2: 'price', 3: 'pricePerA'}, inplace=True)
index = 0

print df.to_json()
