import pandas as pd
import random
# 使用pandas的read_excel函数读取指定的Excel文件
# df = pd.read_csv('./site.csv', nrows=0)

# 获取"Sheet1"工作表中的数据
# data = df.values.tolist()
     # orient="index" 表头算进每一行的字典
for line_x in range(10):
    df = pd.read_csv('data/site.csv', index_col=0)
    # labels = list(df.columns.values)
    df = df.T
    labels = list(df.columns.values)
    # data = df.to_dict(orient="index")
    data = df.to_dict()
    t_data = {
        'a1': 123,
        'a2': 123,
        'a3': 123,
        'a4': 123,
        'a5': 123,
    }
    # for label_x in labels:
    #     t_data[label_x] = random.random() * 100
    data[f'new_{line_x}'] = t_data
    df = pd.DataFrame(data)
    df = df.T
    df.to_csv('./site.csv')
