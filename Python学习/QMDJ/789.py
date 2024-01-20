#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # #
# Create Time: 2023/9/1818:27
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
import itertools

# 列表中的元素
items = ['a', 'b', 'c', 'c']

# 使用itertools.permutations得到所有可能的排列组合
permutations = list(set(itertools.permutations(items)))

# 筛选出其中重复的元素只出现一次的排列
unique_permutations = [p for p in permutations if len(set(p)) == len(p)]

# 输出不重复的排列结果
for l in unique_permutations:
    print(l)