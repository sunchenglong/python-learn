num = "nan"
print(float('-inf') < float(num) < float('inf'))
num = "1e13222"
print(float('-inf') < float(num) < float('inf'))

import numpy as np
import pandas as pd

df = pd.DataFrame({'key1': [1, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                   'key2': ['one', 'two', 'one', 'two', 'one', 'one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(10),
                   'data2': np.random.randn(10)})

print(df)

ctrgrouped_result = df['key1'].groupby(df['key2']).agg(['sum', 'count']).reset_index()
ctrgrouped_result['ctr'] = ctrgrouped_result["sum"] / ctrgrouped_result["count"]

weightctr_grouped_result = df['data1'].groupby(df['key2']).agg(['sum', 'count']).reset_index()
weightctr_grouped_result['weight_ctr'] = weightctr_grouped_result['sum'] / weightctr_grouped_result['count']

print(weightctr_grouped_result)
result = pd.merge(ctrgrouped_result, weightctr_grouped_result, left_on='key2', right_on='key2', how='inner')
print(result)
