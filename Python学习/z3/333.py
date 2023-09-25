import z3
from z3.z3 import IntSort, And, Solver, sat

# 创建一个整数类型的数组变量
arr = z3.Array(IntSort(), 'arr')

# 定义一个约束条件
constraint = And(arr[0] == 1, arr[1] == 2, arr[2] == 3)

# 求解约束条件
solver = Solver()
solver.add(constraint)
if solver.check() == sat:
    print(solver.model())
else:
    print("No solution found")