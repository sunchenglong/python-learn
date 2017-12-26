result = {}
with open('source_result', 'r') as fp:
    lines = fp.readlines()

    for line in lines:
        bkt, sources, platform, cnt = line.rstrip().split('\t')

        if bkt not in result:
            result[bkt] = {}
        if platform not in result[bkt]:
            result[bkt][platform] = {}
        for source in sources.replace(',', '').split('|'):
            if source not in result[bkt][platform]:
                result[bkt][platform][source] = int(cnt)
            else:
                result[bkt][platform][source] = result[bkt][platform][source] + int(cnt)


for i in result["cantor_baseline_x1"]["32"]:
    print i + "," + str(result["cantor_baseline_x1"]["32"][i]) + "," + str(result["cantor_recall_v1"]["32"][i])