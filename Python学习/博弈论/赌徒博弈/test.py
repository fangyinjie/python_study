#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # #
# Create Time: 2023/9/718:32
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
from random import choice
import seaborn as sns
import matplotlib.pyplot as plot

if __name__ == "__main__":
    res = [-0.5, 0.7]
    ret = []
    for exam_num in range(1000):
        init_cost = 100
        for running_num in range(1000):
            init_cost *= 1 + choice(res)
        # print(init_cost)
        ret.append(init_cost)
    ax = sns.histplot(ret, binwidth=max(ret)/100)
    plot.show()
    pass