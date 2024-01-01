import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/gyuhuikwon/Desktop/KHUphy/github/2023_datadist/dataset_2018/data_2018.xlsx'  
feature_names = ['wind_direction', 'temperature', 'precipitation', 'humidity', 'ground_pressure', 'wind_speed', 'sky_condition']
df = pd.read_excel(path)

for names in feature_names:
    plt.hist(df[names], color = 'green', bins = 10, alpha = 0.4, histtype = 'stepfilled')
    plt.title(names)
    plt.xlabel('Time(hour)')
    plt.ylabel('Frequency(number)')
    plt.show() 