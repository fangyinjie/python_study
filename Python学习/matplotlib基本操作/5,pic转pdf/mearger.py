#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# Randomized DAG Generator
# Create Time: 2023/8/615:47
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #

from PyPDF2 import PdfReader,PdfMerger

merger = PdfMerger()
for pdf in ['./2.pdf','./1.pdf']:
    reader = PdfReader(pdf)     # 读取pdf文件
    merger.append(reader)       # 追加到合并对象里
merger.write('./PDF_合并.pdf')
merger.close()
