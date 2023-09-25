from z3 import *
import numpy as np
from z3.z3 import Array, IntSort

# x = Int('x')
# print( "1st child:", arg(0))
# print( "2nd child:", np.arg(1))
# print( "operator: ", np.decl())
# print( "op name:  ", np.decl().name())

# from z3 import *

# 定义一个有界数组
a = Array('a', IntSort(), IntSort())

# 初始化数组
a[0] = 10
a[1] = 20

# 打印数组
print(a[0])  # 输出: 10
print(a[1])  # 输出: 20

# 定义一个函数，对数组进行操作
def increment(a):
    for i in range(a.arity):
        a[i] = a[i] + 1

# 对数组进行操作
increment(a)

# 打印操作后的数组
print(a[0])  # 输出: 11
print(a[1])  # 输出: 21