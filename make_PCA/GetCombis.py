import pandas as pd
from itertools import *
path = '/Users/gyuhuikwon/Desktop/KHUphy/github/2023_datadist/dataset_2018/data_2018.xlsx'
feature_names = ['wind_direction', 'temperature', 'precipitation', 'humidity', 'ground_pressure', 'wind_speed', 'sky_condition']

combis = []
df = pd.read_excel(path)
for n_component in range(2,3):
    for combi in combinations(feature_names[:-1], n_component):
        combi_list = [x for x in combi]
        combis.append(combi_list)
        print(*combi_list, sep=' ')


