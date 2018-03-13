import matplotlib.pyplot as plt

x_y = {}
result = {}
hour = 3600 * 1000
minute = 60 * 1000
second = 100
time_choose = second
with open('pos_distribute.dat') as fp:
    lines = fp.readlines()
    for line in lines:
        td, pv = line.rstrip().split("\t")
        key = int(float(td) / time_choose + 1)
        if key in x_y:
            x_y[key] += float(pv)
        else:
            x_y[key] = float(pv)
with open("pos_distribute" + str(time_choose), 'w') as wfp:
    for i in x_y:
        wfp.write(str(i) + "\t" + str(x_y[i]) + "\n")
