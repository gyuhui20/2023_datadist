import datetime
date = datetime.datetime(2023, 1, 1, 0, 0, 0)
date_list = [(date + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(365)] #2023-01-01 ~ 2023-12-31
print(*date_list, sep='\n')