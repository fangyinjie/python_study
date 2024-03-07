import pandas as pd
import timeit


start = timeit.default_timer()

# 创建一个Dataframe
data = {'Name': ['John', 'Bob', 'Mallory', 'Alice']*25,
        'Location': ['New York', 'Paris', 'Berlin', 'London']*25,
        'Age': [24, 13, 53, 33] * 25}
df = pd.DataFrame(data)

# 创建一个list
list_data = [{'Name': 'John','Location': 'New York','Age': 24},
             {'Name': 'Bob','Location': 'Paris','Age': 13},
             {'Name': 'Mallory','Location': 'Berlin','Age': 53},
             {'Name': 'Alice','Location': 'London','Age': 33}] * 25

# 找到data中Name = John的数据
start_data = timeit.default_timer()
john_data = df.loc[df['Name'] == 'John']
end_data = timeit.default_timer()

# 找到list_data中Name = John的数据
start_list = timeit.default_timer()
john_list = [data for data in list_data if data['Name'] == 'John']
end_list = timeit.default_timer()

print(john_data)
print(john_list)
end = timeit.default_timer()

print('df找到Name = John的数据：', (end_data - start_data)*1000, 'ms')
print('list找到Name = John的数据：', (end_list - start_list)*1000, 'ms')
print('代码总执行时间：', (end - start)*1000, 'ms')

