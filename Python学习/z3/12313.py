from z3 import *
from z3 import z3
import numpy as np
from z3.z3 import sat


x2 = z3.Int('x2')
f1 = z3.Function('f1', z3.IntSort(), z3.IntSort(), z3.IntSort())

node_num = 10

Lower_Triangular = z3.Array('Lower_Triangular', z3.IntSort(), z3.IntSort())
# 定义行和列的类型
# ADJ_Matrix = np.full(shape=(node_num, node_num), fill_value=z3.Int('None'))
#
# for x in range(node_num):
#     for y in range(node_num):
#         Lower_Triangular[x + y * node_num] = z3.Int(f"ADJ_{x}_{y}")
#         ADJ_Matrix[x][y] = Lower_Triangular[x + y * node_num]
        # ADJ_Matrix[x][y] = arr[x * n + y]

s = z3.Solver()
x1 = z3.Int('x1')
y1 = z3.Int('y1')
y2 = z3.Int('y2')
s.add(x1 >= 0, x1 < 2)
s.add(x2 >= 2, x2 < node_num)
s.add(y1 >= 0, y1 < node_num)
# s.add(y2 > x1, y2 < node_num)
# for xx in range(node_num):
#     s.add(Lower_Triangular[xx]==1)
s.add(z3.ForAll([x1, y1], Lower_Triangular[x1*node_num+y1]==0))
s.add(Lower_Triangular[3*node_num+1]==1)
# s.add(z3.ForAll([x2, y1], Lower_Triangular[x2*node_num+y1]==1))
# s.add(z3.ForAll([x1, y2], Lower_Triangular[x1*node_num+y2]==1))

# s.add(Lower_Triangular[]==1)
# s.add(z3.ForAll([xxx], xx[xxx]>0))

# 定义一个函数，将 'f' 的每个元素设置为其索引的平方
# for i in range(10):
#     s.add(f[i] > 0)

# (1) 基础约束1，一个source & sink结点；sink 和 source 分别默认为第一个和最后一个结点；
# for n_y in range(1, n):
#     s.add(ADJ_Matrix[:, n_y].sum() > 0)  # 除了第一例，其他列的和都大于0；

# 打印数组变量的定义
# print(arr[1])

# z3.Exists
# s.add(f(1, 10) == 42)

# print(s.sexpr())

# """
# x = z3.Int('x')
# s.add(z3.ForAll([x], f[x] == 1))
# 打印 'f' 的前五个元素
# print(f[0:5])

if s.check() == sat:
    result = s.model()
    # ret_ADJ_Matrix = np.full(shape=(node_num, node_num), fill_value=1, dtype=int)
    # for i in range(node_num):
    #     ret_ADJ_Matrix[i][0] = result.eval(Lower_Triangular[i])
    for x in range(node_num):
        for y in range(node_num):
            print(result.eval(Lower_Triangular[x1*node_num+y1]) ,end=',')
        print()
    # print(s.model())
    # for xc in range(10):
    #     print(s.model().eval(f[xc]))
    # print(s.model().eval(f(1, 10)))
    # print(s.model().eval(f(2, 10)))

else:
    print("No solution found")
