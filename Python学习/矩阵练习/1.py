#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# Randomized DAG Generator
# Create Time: 2023/8/1417:08
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
import numpy as np


a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.array([[0,0,0]])

c = np.r_[a,b]

d = np.c_[a,b.T]

print (c)
print (d)

array1=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)
array2=np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)
# result=np.multiply(array1,array2)
result=np.matmul(array1,array2)

print(array1)
print(array2)
print(result)

cc = (np.full(shape=(3, 3), fill_value=1) - np.eye(3)) * result
print(f'full1:\n{cc }')


cd11 = np.array([[0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]])

cd12 = np.array([[0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]])


print(cd11)
print(np.identity(5))
print(np.power(cd11 + np.identity(5), 5) - np.identity(5))


cd22 = np.array([[1, 1],
                 [0, 1]])

print(np.power(cd22, 2))


print(np.dot(cd22, cd22))


print(cd22 ** 2)