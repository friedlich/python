c_param_range = [0.01,0.1,1,10,100]
print(len(c_param_range))
index = range(len(c_param_range),2)
print(index)

import pandas as pd
c_param_range = [0.01, 0.1, 1, 10, 100]
# results_table = pd.DataFrame(index=range(len(c_param_range), 2), columns=['C_parameter', 'Mean recall score'])
results_table = pd.DataFrame(columns=['C_parameter', 'Mean recall score'])
results_table['C_parameter'] = c_param_range
print(results_table)
print(results_table.dtypes)

import numpy as np
print(np.arange(2))