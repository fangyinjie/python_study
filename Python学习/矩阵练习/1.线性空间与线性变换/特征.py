
#!/usr/bin/env python
# encoding: utf-8
'''
@Author  : pentiumCM
@Email   : 842679178@qq.com
@Software: PyCharm
@File    : __init__.py.py
@Time    : 2020/4/11 9:39
@desc	 : numpy计算矩阵的特征值，特征向量
'''

import numpy as np
import networkx as nx
# A1 = np.mat()
# A1 = np.array()

G = nx.fast_gnp_random_graph(4, 0.5)
adj_matrix = nx.adjacency_matrix(G).todense()
A1 = np.ones((4, 4))
B = A1 - adj_matrix
B = np.array(B, dtype=int)
det_B = np.linalg.det(B)

# mat = np.array([[-1, 1, 0],
#               [-4, 3, 0],
#               [1, 0, 2]])

mat = np.array([[0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0]])

eigenvalue, featurevector = np.linalg.eig(mat)

print(mat)
print(B)
print(adj_matrix)
print(det_B)
print("特征值：\n", eigenvalue)
print("特征向量：\n", featurevector)


