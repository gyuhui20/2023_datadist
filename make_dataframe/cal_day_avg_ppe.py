import numpy as np
import sys
from concurrent.futures import ProcessPoolExecutor

np.set_printoptions(linewidth=np.inf)

def cal_day_avg(i):
    filename = f'csv_total/{i}.csv'
    data_day = np.loadtxt(filename, dtype="str", delimiter=' ')
    stock_data = np.array(data_day[:,2:], dtype='f')
    stock_avg = np.array(stock_data.sum(axis=0) / 144)
    print(*stock_avg)

if __name__ == '__main__':
    #results = list(pool.map(cal_day_avg, num))
    with ProcessPoolExecutor(max_workers=1) as executor:
        results = executor.map(cal_day_avg, range(1, int(sys.argv[1])))
    