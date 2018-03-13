import matplotlib.pyplot as plt

x_y = {}
result = {}
with open('result_new') as fp:
    lines = fp.readlines()
    for line in lines:
        td, pv = line.rstrip().split("\t")
        x_y[float(td)] = float(pv)
    tmp_sum = 0
    cnt = 1
    hour = 3600 * 1000
    second = 1000
    time_choose = second
    keys = sorted(x_y.keys(), key=lambda d: float(d))

    for i in keys:
        print i

    for i in keys:
        print i
        if i >= second * cnt:
            result[cnt] = tmp_sum
            tmp_sum = 0
            cnt += 1
        tmp_sum += x_y[i]
    keys = sorted(result.keys(), key=lambda d: float(d))
    for i in result.keys():
#        print i, result[i]
        pass