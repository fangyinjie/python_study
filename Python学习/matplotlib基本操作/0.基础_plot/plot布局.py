#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# Randomized DAG Generator
# Create Time: 2023/8/515:26
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import numpy as np

def f(x1):              # 定义函数
    return (1 + x1) / (1 - x1)


if __name__ == "__main__":
    # # 1.1 Figure  # # 在任何绘图之前，我们需要一个Figure对象，可以理解成我们需要一张画板才能开始绘图。
    # fig = plt.figure()
    # plt.xlim(0.5, 4.5)      # plt.xlim(xmin, xmax) xmin：x轴上的最小值 x轴上的最大值
    # plt.ylim(10.0, 50)      # plt.ylim(ymin, ymax) ymin：y轴上的最小值 x轴上的最大值
    # # 1.2 Axes & Multiple Axes
    # # 作画还需要轴，没有轴的话就没有绘图基准，所以需要添加Axes。也可以理解成为真正可以作画的纸。
    # # 可以发现我们上面添加 Axes 似乎有点弱鸡，所以提供了下面的方式一次性生成所有 Axes：
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(128, 128), dpi=80,facecolor='w', edgecolor='k')
    axes[0, 0].set( title='An Example Axes',            # 图的名字
                    # xlim=[0.5, 4.5],ylim=[-2, 8],       # x与y轴的区间
                    xlabel='X-Axis', ylabel='Y-Axis' )  # x与y轴坐标
    x = np.arange(-1, 1, 0.1)       # 生成一组x值
    y = f(x)                        # 根据函数计算一组y值
    axes[0, 0].plot(x, y)           # 绘制函数曲线图
    # ### # (2) # ### #
    axes[0, 1].set(title='Upper Right', xlim=(0, 8), ylim=(0, 8),
                   xticks=np.arange(1, 8), yticks=np.arange(1, 8))
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)
    axes[0, 1].plot(x, y, linewidth=2.0)

    # ### # (3) # ### #
    axes[1, 0].set(title='Lower Left')

    # ### # (4) # ### #
    axes[1, 1].set(title='Lower Right')
    axes[1, 1].plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)        # 绘制线

    plt.savefig('./testblueline.jpg')
    plt.savefig('./testblueline.pdf')
    plt.show()

