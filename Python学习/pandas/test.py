import pandas as pd

""" 

# 第一个key 为列标 ['dag_id', 'dag_index', 'wcet', 'bcet', 'acet', 'rank']
# 第二各key 为行标 ['dag_1', 'dag_2', 'dag_3', 'dag_4']
dict = {'dag_id':       {'dag_1': 1,  'dag_2': 2,  'dag_3': 3,  'dag_4': 4},
        'dag_index':    {'dag_1': 1,  'dag_2': 2,  'dag_3': 3,  'dag_4': 4},
        'wcet':         {'dag_1': 31, 'dag_2': 32, 'dag_3': 33, 'dag_4': 34},
        'acet':         {'dag_1': 21, 'dag_2': 22, 'dag_3': 23, 'dag_4': 24},
        'bcet':         {'dag_1': 11, 'dag_2': 12, 'dag_3': 13, 'dag_4': 14}}

df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')
"""
"""
df = pd.read_csv('site.csv')
print(df)
# print(df.tail())
# print(df['dag_id'])
"""

# df = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
#                    ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
#                    ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
#                    ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
#                    ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
# df.to_csv('site.csv')
# print(df)
#
df = pd.DataFrame({'a1': {'A': [1], 'C': 2},
                   'a2': {'A': [3], 'B': 4},
                   'a3': {'A': [5], 'C': 6},
                   'a4': {'A': [1, 2, 3], 'B': 8},
                   'a5': {'A': [9], 'B': 10, 'E': 12}},
                  columns=['a1', 'a2', 'a3', 'a4', 'a5'],
                  index=['A', 'B', 'C', 'D'])
df.to_csv('site.csv')
print(df)


