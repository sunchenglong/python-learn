import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
df = pd.read_csv('userprofile', "\t", names=["uid", "type", "value"])
print df.head(20)
print df.describe()
print df.groupby("type").agg({"type": np.sum, "value": pd.Series.nunique})
consumption = df[df['type'] == "consumption_level_of_baidu"]['value'].map(lambda x: int(x.split(":")[0]))

def plot_value_weight(name):
    consumption = df[df['type'] == name]['value']
    value_weight = {}
    multiscore = 0
    for co in consumption:
        parts = co.split(",")
        if len(parts) > 1:
            multiscore = 1
        for part in parts:
            key = part.split(":")[0]
            value = float(part.split(":")[1])
            if key not in value_weight:
                value_weight[key] = []
            value_weight[key].append(value)
    for key in value_weight.keys():
        plt.hist(value_weight[key], 100, label=str(key))
    if multiscore == 1:
        print "Multi score value"
    else:
        print "Single score value"
    plt.legend()
    plt.title(name)
    plt.show()
#plot_value_weight("consumption_level_of_baidu")
plot_value_weight("occupation_of_baidu")