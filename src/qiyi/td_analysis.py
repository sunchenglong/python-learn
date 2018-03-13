import matplotlib.pyplot as plt

x = []
y = []
h = []
with open('result.data') as fp:
    lines = fp.readlines()
    cnt = 4000

    for line in lines:
        td, pv = line.rstrip().split("\t")
        x.append(float(td))
        y.append(float(pv))
        if cnt > 0:
            h.extend([float(td) for i in range(int(pv))])
        cnt -= 1
    pv_all = sum(y)
    max_plt_cnt = 1000
    # plt.plot(x[1:max_plt_cnt], [i/pv_all for i in y[1:max_plt_cnt]])
    # plt.show()
    # plt.hist([i / pv_all for i in y[1:max_plt_cnt]],1000)
    plt.hist(h, 200)
    plt.show()
