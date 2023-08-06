#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# Dynamic
# Create Time: 2023/8/518:03
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(n):  # 更新函数
    x1.append(n)  # 添加X轴坐标
    y1.append(10 * np.sin(n))  # 添加Y轴坐标
    axes[0,0].plot(x1, y1, "r--")  # 绘制折线图

    line1.set_ydata(np.sin(x2 + n / 10.0))  # 改变线条y的坐标值
    line2.set_ydata(np.cos(x2 + n / 10.0))  # 改变线条y的坐标值


if __name__ == "__main__":
    # fig = plt.figure(figsize=(10, 5))  # 创建图
    fig, axes = plt.subplots(nrows=2, ncols=2)
    axes[0, 0].set( title='dynamic_1_1',  # 图的名字
                    xlim=[0, 2 * np.pi],    xticks=[0.5 * i for i in range(14)],
                    ylim=[-12, 12],         yticks=[-12 + 2 * i for i in range(13)],# X轴刻度
                    xlabel='X-Axis',        ylabel='Y-Axis')  # x与y轴坐标
    x1, y1 = [], []  # 用于保存绘图数据，最开始时什么都没有，默认为空

    axes[0, 1].set_axis_off()           # 不显示坐标轴
    x2 = np.arange(0, 2 * np.pi, 0.01)   # 生成X轴坐标序列
    line1, = axes[0, 1].plot(x2, np.sin(x2))  # 获取折线图对象，逗号不可少，如果没有逗号，得到的是元组
    line2, = axes[0, 1].plot(x2, np.cos(x2))  # 获取折线图对象，逗号不可少

    ani = FuncAnimation(fig, update, frames=np.arange(0, 2 * np.pi, 0.1),
                        interval=50, blit=False, repeat=False)
    plt.show()
