#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # #
# Create Time: 2023/9/1416:45
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
import time
import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.DiGraph()
G2 = nx.DiGraph()
G3 = nx.DiGraph()
G4 = nx.DiGraph()
G5 = nx.DiGraph()

edges_dict = {
    1: [  1,  2,  3,  4,  5,  6,  7,  8],
    2: ['a','b','c','d','e','f','g','h'],
    3: ['A','B','C','D','E','F','G','H'],
}

edge_list = [(1,2), (1,3), (2,4), (3,4), (4,5), (4,6), (5,7), (6,7)]
for edge_t in edge_list:
    G1.add_edge(edges_dict[1][edge_t[0]], edges_dict[1][edge_t[1]])
    G2.add_edge(edges_dict[2][edge_t[0]], edges_dict[2][edge_t[1]])
    G3.add_edge(edges_dict[3][edge_t[0]], edges_dict[3][edge_t[1]])

G3.add_edge('A','G')

G4.add_edge(1,2)
G4.add_edge(1,3)

G5.add_edge(3,1)
G5.add_edge(3,2)

stime = time.time()
for _ in range(10000):
    GM = nx.isomorphism.GraphMatcher(G1, G2)
    C = GM.is_isomorphic()
etime = time.time()
print(f'1time:{etime - stime}')
 # mapping = GM.mapping
stime = time.time()
for _ in range(10000):
    D = nx.is_isomorphic(G1, G2)
etime = time.time()
print(f'1time:{etime - stime}')

GM = nx.isomorphism.GraphMatcher(G4, G5)
E = GM.is_isomorphic()
# print(C)
# print(D)
print(E)