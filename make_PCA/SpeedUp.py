f=open("time_by_process.txt")
data = f.readlines()

time_data = []
for i in range(6):
    x = data[6*i+3][4:].strip()
    time = float(x[0])*60+float(x[2:-2])
    time_data.append(time) #type(float)

time_rate_data = []
for i in range(5):
    rate = time_data[i+1]/time_data[i]
    time_rate_data.append(rate)
print("time taken:", time_data)
print("time_rate:", time_rate_data)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(time_data,'-dg')
plt.xlabel('process_number')
plt.ylabel('time taken')
plt.title('Time taken depending on number of processes')
plt.savefig('proc_time.png')

plt.figure()
plt.plot(time_rate_data,'-db')
plt.xlabel('process sequence')
plt.ylabel('time rate')
plt.title('Efficiency improvement rate due to multiprocessing')
plt.savefig('proc_speedup.png')