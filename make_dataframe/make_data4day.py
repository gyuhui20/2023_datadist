import random
import numpy as np
import datetime
import sys
    
def make_data4day(seed=0):
    np.set_printoptions(linewidth=np.inf)
    
    time_list = [(date + datetime.timedelta(minutes=i)).strftime("%H:%M:%S") for i in range(0,1440,10)] #0시 00분~ 23시 50분
    random.seed(int(seed)-1)
    date_ = []
    for i in range(144):
        date_.append(date_list[int(seed)-1])

    price_list = np.c_[date_, time_list]
    rd_range = []
    for i in range(100):
        rd_range.append(random.randrange(100000,500000,10))
        name_lst = []
        for j in range(144):
            a = rd_range[i]-i+(-1)**(i)*10*j
            if a >= 0: 
                name_lst.append(a) #i번째 stock의 데이터
            else :
                name_lst.append(-a)
        price_list = np.c_[price_list, name_lst] #stock1부터 stock 100까지 값을 열 방향으로 추가
        
    return price_list


if __name__ == "__main__":
    date = datetime.datetime(2023, 1, 1, 0, 0, 0)
    time_list = [(date + datetime.timedelta(minutes=i)).strftime("%H:%M:%S") for i in range(0,1440,10)] #0시 00분~ 23시 50분
    date_list = [(date + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(365)] #2023-01-01 ~ 2023-12-31

    price_list = make_data4day(int(sys.argv[1]))
    #price_list = ' '.join(price_list)
    #print(*price_list, sep='\n')
    for i in range(144):
        print(*price_list[i])

