import pandas as pd
import numpy as np
import networkx as nx

lable = ['name', 'int', 'float']
s1 = pd.Series(['123', 123, 123.0], lable)
s2 = pd.Series(['124', 124, 124.0], lable)
s3 = pd.Series(['125', 125, 125.0], lable)
s4 = pd.Series(['126', 126, 126.0], lable)

df = pd.DataFrame([s1, s2, s3, s4], index=[13,14,15,16], columns=lable)
# data = None,
# index: Axes | None = None,
# columns: Axes | None = None,
# dtype: Dtype | None = None,
# copy: bool | None = None,
# print(df.loc[:'name'])

print(df)
# print(df.loc["day2"])

df = pd.DataFrame(np.random.randn(8, 4), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], columns=['A', 'B', 'C', 'D'])
print(df)
print(df.loc[['a', 'b', 'f', 'h'], ['A', 'C']])
print(df[df['A']>1])
# df[df['A']>df['A'].mean()].sort_values(by='NOX',ascending=False).head()

data = {'dag_id':[1,2], 'dag_inst':[2,3], 'dag_num':[3,4], 'DAG':'DAG'},
s1 = pd.Series(data)
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame({'name': ['A', 'B', 'C', 'D'], 'age': [11, 12, 13, 14]})
print(df)
s = pd.Series(1, index=range(5))
df.insert(0, 'class', s)
print(df)


df = pd.DataFrame(columns=['name','number'])
# 采用.loc的方法进行
df.loc[0]=['cat', 3]  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
# 也可采用诸如df.loc['a'] = ['123',30]的形式


# 1.采用append方法合并两个dataframe
# 构造两个dataframe
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(df)
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
print(df2)
# 合并  ignore_index设置为 True可以重新排列索引
# df.concat(df2, ignore_index=True)
print('ffffffffffffff')
df = pd.concat([df, df2], ignore_index=True)
print(df)

print('ffffffffffffff')
# 同样如果是遍历添加多行，有一种更高效的方法
dff = pd.concat([pd.DataFrame([i], columns=['A']) for i in range(6)], ignore_index=True)
print(dff)

dag = nx.DiGraph()
print('ffffffffffffff')
a = np.array([dag])
print("ddd")
