import pandas as pd
"""
df = pd.read_excel('./data/result模块.xls', sheet_name=None)
x = df.keys()       # 查看所有sheet 名字
y = df.values()
pass
# df['AAA']       # 为读取“AAA"工作薄中的内容
"""

df = pd.ExcelFile('../../DAG_9-28_new/data/result模块.xls')
c = df.sheet_names  # 查看所有sheet 名字
cc = df.parse(c[1])  # 为读取AAA工作薄中的内容
df_concat = pd.concat([ pd.read_excel(df, sheet) for sheet in df.sheet_names])  # 将所有sheet中数据合并到一个df中

# import pandas as pd
writer = pd.ExcelWriter('test_excel.xlsx')
df.to_excel(writer, sheet_name='AAA')
df.to_excel(writer, sheet_name='BBB')

pass