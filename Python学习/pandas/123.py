import pandas as pd
import os

os.crea
writer = pd.ExcelFile('./your_path.xlsx')

df1 = pd.DataFrame()
# df1.to_excel(writer, sheet_name='df_1')
df2 = pd.DataFrame()
# df2.to_excel(writer, sheet_name='df_2')

df1.to_excel(writer, sheet_name='AAA')
df2.to_excel(writer, sheet_name='BBB')

#

# writer.save()
#     # save()
#
# import pandas as pd
#
# # 三个字段 name, site, age
# nme = ["Google", "Runoob", "Taobao", "Wiki"]
# st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
# ag = [90, 40, 80, 98]
#
# # 字典
# dict = {'name': nme, 'site': st, 'age': ag}
#
# df = pd.DataFrame(dict)
#
# # 保存 dataframe
# df.to_csv('site.csv')