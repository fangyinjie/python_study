import gurobipy as gp
import numpy as np

try:
    m = gp.Model("model")

    A = np.full((5, 10), 1)
    # x1 = m.addMVar((1,10))
    x1 = m.addMVar(10)
    b = np.full(5, 10)
    print(np.dot(b, A))
    m.addConstr(A @ x1 == b, "xx")
    # m.addMConstrs(A, x1, '=', b)

    m.optimize()
    # print('%s %g' % (x1.varName, x1.x))
    print(x1.x)
    # for v in m.getVars():
    #     print('%s %g' % (v.varName, v.x))

    # print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error reported' + str(e.errno) + ':' + str(e))

except AttributeError:
    print('Encountered an attribute error')

