from z3 import *
import numpy as np

cc1 = Bool('cc1')
cc2 = Bool('cc2')

nnmmcc = np.array([[True, True,  False],
                   [False, True,  True],
                   [False, False, True]])
# nnmmcc = np.array([[1, 1, 0],
#                    [0, 1, 1],
#                    [0, 0, 1]])
# nnmmcc = [[1, 1, 0],
#           [0, 1, 1],
#           [0, 0, 1]]
c4 = nnmmcc @ nnmmcc
print(np.dot(nnmmcc, nnmmcc))
print(nnmmcc@nnmmcc)
print(np.power(nnmmcc, 2))

nnmm = np.full(shape=(3, 3), fill_value=Bool('None'))
for x in range(3):
    for y in range(3):
        nnmm[x][y] = Bool(f'nm_{x}_{y}')


s = Solver()
s.add(Implies(cc1, cc2))
s.add(cc1 == True)
s.add(cc2 == False)
if s.check() == sat:
    models = s.model()
    # result_x11 = models.eval(x11)
    # result_y11 = models.eval(y11)
    # result_x1 = models.eval(x1)
    # result_z1 = models.eval(z1)
    # result_s1 = models.eval(s1)
    # print(result_x1, type(result_x1), float(result_x1.as_fraction()))
    # print(result_z1, type(result_z1), is_true(result_z1))
    # print(result_s1, type(result_s1), result_s1.eq(off))
    # ret_Matrix = models.eval(ctt)
    # ret_Matrix = models.eval(newCC1[1][1])
    # ret_Matrix = [[1,2,3],[1,2,3],[1,2,3]]

    result_cc1 = models.eval(cc1)
    result_cc2 = models.eval(cc2)

    print('NEW')
    print(result_cc1)
    print(result_cc2)
    # print(result_x11.as_long())
    # print(result_y11.as_long())
else:
    print('unsolve')
# print (s)
# s.add(x > 10, y == x + 2)
# print (s)
# print ("Solving constraints in the solver s ...")
# print (s.check())                       # 判断是否满足
#
# print ("Create a new scope...")         # 创建一个新的范围
# s.push()
# s.add(y < 11)
# s.add(y + x < 111)
#
# print (s)
# print ("Solving updated set of constraints...")
# print (s.check())
# print ("Restoring state...")
# s.pop()
# print (s)
# print ("Solving restored set of constraints...")
# print (s.check())

