import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

df = pd.read_csv('userprofile', "\t", names=["uid", "type", "value"])
print df.head(20)
print df.describe()
print df.groupby("type").agg({"type": np.sum, "value": pd.Series.nunique})
consumption = df[df['type'] == "consumption_level_of_baidu"]['value'].map(lambda x: int(x.split(":")[0]))
#plt.hist(consumption, 50)
#plt.show()
# plt.hist(np.array(consumption), 3, normed=1, facecolor='blue', alpha=0.5)
weights = np.ones_like(consumption) / float(len(consumption))
# plt.hist(consumption, weights=weights)
# plt.show()
name = "consumption_level_of_baidu"
consumption = df[df['type'] == name]['value']
industry = df[df['type'] == "industry_of_baidu"]['value']
print consumption
#plt.hist(consumption, 50)
#plt.show()
consumption = df[df['type'] == name]['value']
tmp = []
for co in consumption:
    parts = co.split(",")
    for weight in parts:
        tmp.append(float(weight.split(":")[1]))
plt.hist(tmp, 50)
tmp = []
for co in industry:
    parts = co.split(",")
    for weight in parts:
        tmp.append(float(weight.split(":")[1]))
plt.hist(tmp, 50, label="abd")
plt.legend()
plt.show()
