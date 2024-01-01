import numpy as np
import sys
import time as time


np.set_printoptions(linewidth=np.inf)

filename = f'csv_total/{sys.argv[1]}.csv'
data_day = np.loadtxt(filename, dtype="str", delimiter=' ')
stock_data = np.array(data_day[:,2:], dtype='f')
stock_avg = np.array(stock_data.sum(axis=0) / 144)
print(*stock_avg)

