from z3 import *
import networkx as nx
# 1、定义求解的数据类型为int整形
n = Int('n')                # 只定义一个int整形
a, s, d = Ints('a s d')     # 同时定义多个int整形。

x = Solver()        # 2、初始化一个Solver类
x.add(a-d == 18)    # 3、对于数据进行约束、即写方程
x.add(a > 20)    # 3、对于数据进行约束、即写方程
x.add(d > 3)    # 3、对于数据进行约束、即写方程
# x.add(a+s == 12)
# x.add(s-d == 20)

s.push()
s.add()

while str(x.check()) == 'sat':
    result = x.model()
    print(result)
    # make_span = result[tasks['v_snk']]
    # make_span -= 1
    # s.pop()
    # s.push()
    s.add(result)

# check = x.check()   # 4、检测是否有解（有解sat、无解unsat）
# print(check)
# model = x.model()   # 5、取出所有结果，一个ModelRef类，
# print(model)
#

G = nx.DiGraph()  # 创建空的有向图
G.add_node(1, name='n1', weight=1)
G.add_node(2, name='n2', weight=3)
G.add_node(3, name='n3', weight=3)
G.add_node(4, name='n4', weight=6)
G.add_node(5, name='n5', weight=7)
G.add_node(6, name='n6', weight=8)

G.add_edges_from([(1, 2, {'weight': 8}),
                  (1, 3, {'weight': 8}),
                  (1, 4, {'weight': 8}),
                  (1, 5, {'weight': 8}),
                  (2, 6, {'weight': 8}),
                  (3, 6, {'weight': 8}),
                  (4, 6, {'weight': 8}),
                  (5, 6, {'weight': 8})])

G2 = nx.DiGraph()  # 创建空的有向图
G2.add_node(1, name='n1', weight=1)
G2.add_node(2, name='n2', weight=3)
G2.add_node(3, name='n3', weight=3)
G2.add_node(4, name='n4', weight=6)
G2.add_node(5, name='n5', weight=7)
G2.add_node(6, name='n6', weight=8)

G2.add_edges_from([ (1, 2, {'weight': 8}),
                    (2, 3, {'weight': 8}),
                    (3, 4, {'weight': 8}),
                    (4, 5, {'weight': 8}),
                    (5, 6, {'weight': 8})]    )