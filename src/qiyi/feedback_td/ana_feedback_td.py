import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

td_data = pd.read_csv('feedback_distribute.dat', sep='\t')

view_data = td_data[td_data.feedback == 'view'][td_data.td < 1000 * 20][td_data.td > 0]
sumpv = sum(view_data.pv)
view_data['sumpv'] = view_data['td'] * view_data['pv']

print str(sum(view_data['sumpv']) / sumpv / 1000) + "s"

# plt.plot(view_data['td'], view_data['pv'])
# plt.show()

# unit = ms
td_interval = 1000 * 60 * 60 * 10  # 20s
feedbacks = pd.unique(td_data.feedback)
all_df = {}
feedback_result = {}

for f in feedbacks:
    all_df[f] = td_data[td_data.feedback == f][td_data.td > 0]
    # all_df[f] = td_data[td_data.feedback == f][td_data.td < td_interval][td_data.td > 0]
    all_df[f]['sumpv'] = all_df[f]['td'] * all_df[f]['pv']
    all_df[f]['pvratio'] = all_df[f]['pv'] / sum(td_data[td_data.feedback == f]['pv'])
    feedback_result[f] = sum(all_df[f]['sumpv'] / sum(all_df[f]['pv']) / 1000)

for f in feedbacks:
    print f + "\t" + str(feedback_result[f])

    # plt.plot(all_df['click_detailpage']['td'],
    #         all_df['click_detailpage']['pvratio'], '-r',
    #         all_df['click_picture']['td'],
    #         all_df['click_picture']['pvratio'], '-b')

# plt.plot(all_df['click_detailpage']['td'],
#         [sum(all_df['click_detailpage'][all_df['click_detailpage'].td < x]['pvratio']) for x in
#          all_df['click_detailpage']['td']], '-r',
#         all_df['click_picture']['td'],
#         [sum(all_df['click_picture'][all_df['click_picture'].td < x]['pvratio']) for x in
#          all_df['click_picture']['td']], '-b')
plt.show()

print "fafa".__contains__("faa")
from scipy.sparse import csr_matrix