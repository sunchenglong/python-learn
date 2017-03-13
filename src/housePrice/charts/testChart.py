import charts
import sys
import numpy as np
import numpy.random
print(sys.path)


data = np.random.rand(10)
data2 = np.random.rand(10)*2
charts.plot(data, name='My list')
charts.plot(data2, name='My list2')