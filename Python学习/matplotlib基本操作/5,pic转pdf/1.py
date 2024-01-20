#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# Randomized DAG Generator
# Create Time: 2023/8/615:28
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #

import matplotlib.pyplot as plt     # plt 用于显示图片
import matplotlib.image as mpimg    # mpimg 用于读取图片
from PyPDF2 import PdfFileMerger

test_png = mpimg.imread("./2.jpg")     # 读取png
              # 读取生成的图片
# figure(
plt.figure(figsize=(8.27, 11.69), dpi=1000)

ax = plt.gca()  # 获取图形坐标轴
ax.set_axis_off()  # 去掉坐标
ax.imshow(test_png)
# plt.show()
plt.savefig('./2.pdf', format='pdf')

file_merger = PdfFileMerger()
file_merger.append('./1.pdf', import_outline=False)  # 合并pdf文件
file_merger.append('./2.pdf', import_outline=False)  # 合并pdf文件
file_merger.write(r"./合并文件.pdf")
