import pandas as pd
import os

# df = pd.DataFrame(columns=["title", "content"])
# df.to_excel('xxx.xlsx', index=False)

excel_path_name = './xxx.xlsx'

df1 = pd.DataFrame()
df2 = pd.DataFrame()
df1.to_excel(excel_path_name, "df1")
df2.to_excel(excel_path_name, "df2")
writer.save()
writer.close()

if os.path.exists('./xxx.xlsx'):
    os.remove('./xxx.xlsx')
df.to_excel(excel_path_name, "df1")

# writer = pd.ExcelWriter('./xxx.xlsx', mode='a', engine='openpyxl')

