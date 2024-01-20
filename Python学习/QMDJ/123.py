#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# Randomized DAG Generator
# Create Time: 2023/9/1811:14
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #


# def shape_enumate(n, l, width, shape_max, shape_min, deg_in_max, deg_out_min):
#     assert (n-l) > width
import itertools

def sub_dag_shape_enumate(sub_dag, n, l, width, shape_max, shape_min, deg_in_max, deg_out_min):
    assert (n-l) > width
    dag_list = []

    return dag_list
# 定义箱子和球的数量
num_boxes = 4
num_balls = 10

# 生成所有可能的组合
combinations = []
for i in range(num_boxes + 1):
    for j in range(num_boxes + 1 - i):
        for k in range(num_boxes + 1 - i - j):
            l = num_balls - i - j - k
            combinations.append((i, j, k, l))

# 输出每种组合
for combination in combinations:
    print(f"箱子分配数量为：{' '.join(map(str, combination))}")