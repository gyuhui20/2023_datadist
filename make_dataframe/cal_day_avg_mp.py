import numpy as np
import sys
import multiprocessing

def cal_day_avg(i):
    np.set_printoptions(linewidth=np.inf)
    filename = f'csv_total/{i}.csv'
    data_day = np.loadtxt(filename, dtype="str", delimiter=' ')
    stock_data = np.array(data_day[:,2:], dtype='f')
    stock_avg = np.array(stock_data.sum(axis=0) / 144)
    print(*stock_avg)

if __name__ == '__main__':
    
    procs = []
    for i in range(1,int(sys.argv[1])):
        p = multiprocessing.Process(target=cal_day_avg, args=(i, ))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()
        