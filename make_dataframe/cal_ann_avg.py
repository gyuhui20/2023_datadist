import numpy as np
import matplotlib.pyplot as plt
def cal_ann(filename):
    day_avg = np.loadtxt(f'{filename}', dtype="str", delimiter=' ').astype(float)
    stock_ann_avg = np.array(day_avg.sum(axis=0) / 365)
    num = stock_ann_avg.argmax()
    print("최대 연평균값:", stock_ann_avg[num], "/ 해당 종목", num,"번 가상화폐 종목") #44

    plt.plot(day_avg[:,num])
    plt.xlabel('date')
    plt.ylabel('daily average price')
    plt.title(f'daily average of {num}th stock')
    plt.show()