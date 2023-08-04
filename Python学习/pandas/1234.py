#!/usr/bin/env python


# -*- coding: utf-8 -*-

"""
version: 0.1
author: wang pei
license: copyright(c) 2017 pei.wang
summary:
 (1)padas dataframe生成excel
 (2)excel中增加sheet表
"""
import sys
import os
import numpy as np
import pandas as pd
from openpyxl import load_workbook

def get_header():
    """
    获取列名
    return: list
    """
    df1 = pd.read_clipboard(header=None, dtype=str)
    headers = [i.pop() for i in np.array(df1).tolist()]
    return headers


def gen_df():
    """针对复制源数据有空值的"""
    df3 = pd.read_clipboard(header=None, sep=r'\s', dtype=str).replace('nan', '')
    return df3


def write_excel(headers, sheet, df_piece=None):
    """
    数据写入到Excel,可以写入不同的sheet
    """
    df2 = pd.read_clipboard(header=None, dtype=str)
    if df_piece is not None:  # 主要针对有空值得时候，需要拼接df
        df2 = df2.append(df_piece)
    writer = pd.ExcelWriter(r'C:\Users\hand\Desktop\result\data.xlsx', engine='openpyxl')
    print(df2)
    if os.path.exists(r'C:\Users\hand\Desktop\result\data.xlsx') != True:
        df2.to_excel(writer, sheet_name=sheet, index=None)
    else:
        book = load_workbook(writer.path)
        writer.book = book
    df2.to_excel(writer, index=False, sheet_name=sheet, header=headers)
    writer.save()
    writer.close()

    df = pd.DataFrame(columns=["title", "content"])
    df.to_excel('E:\\data.xlsx', index=False)