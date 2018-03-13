cnt = 1000
view_dict = {}
pos_dict = {}

with open('view_distribute.dat') as fp:
    lines = fp.readlines()
    for line in lines:
        td, pv = line.rstrip().split("\t")
        key = float(td)
        if key < cnt:
            view_dict[str(key)] = float(pv)
with open('pos_distribute.dat') as fp:
    lines = fp.readlines()
    for line in lines:
        td, pv = line.rstrip().split("\t")
        key = float(td)
        if key < cnt:
            pos_dict[str(key)] = float(pv)

print pos_dict
with open("pos_vs_neg_" + str(cnt) + ".dat", 'w') as wfp:
    for i in view_dict.keys():
        wfp.write(str(i) + "\t" + str(pos_dict.get(i, 0)) + "\t" + str(view_dict.get(i, 0)) + "\n")
