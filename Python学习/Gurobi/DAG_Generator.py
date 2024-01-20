#!/usr/bin/env python3.7

import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB


# Size of the n x n chess board

"""

    s.add([ADJ_Matrix[i][j] == 0 for i in range(n) for j in range(n) if i >= j])
    # (2) Shape内元素为0
    # (2.1) 确定shape
    for n_x in range(1, n-1):
        s.add(node_level_list[n_x] < k, node_level_list[n_x] > 1)
        s.add(node_level_list[n_x] >= node_level_list[n_x - 1], node_level_list[n_x] <= node_level_list[n_x + 1])  # 层数顺序递增
    for kx in range(2, k):
        self_level_node_num = Sum([If(nl_x == kx, 1, 0) for nl_x in node_level_list])
        last_level_node_num = Sum([If(nl_x == kx - 1, 1, 0) for nl_x in node_level_list])
        next_level_node_num = Sum([If(nl_x == kx + 1, 1, 0) for nl_x in node_level_list])
        s.add(self_level_node_num <= max_shape)  # 层为kx的节点数量
        s.add(self_level_node_num >= min_shape)  # 层为kx的节点数量
        s.add(self_level_node_num <= width)  # 层中节点的数量一定小于width
        s.add(last_level_node_num * max_out_degree >= self_level_node_num)  # 前一层节点的数量乘以最大出度必须大于等于本层节点数
        s.add(next_level_node_num * max_in_degree >= self_level_node_num)  # 后一层节点的数量乘以最大入度必须大于等于本层节点数
    s.add(node_level_list[0] == 1)  # 首节点在第一层
    s.add(node_level_list[n - 1] == k)  # 尾节点在第k层
    # (2.2) shape内元素为0
    for n_x in range(n):
        s.add([ADJ_Matrix[n_x][n_y] == If(node_level_list[n_x] == node_level_list[n_y], 0, ADJ_Matrix[n_x][n_y]) for
               n_y in range(n_x + 1, n)])
    # (3) jl, indegree, outdegree
    for n_x in range(1, n):
        s.add(Sum([If(node_level_list[n_x] - node_level_list[n_y] == 1, ADJ_Matrix[n_y][n_x], 0) for n_y in
                   range(n_x)]) >= 1)
        s.add(Sum([If(node_level_list[n_x] - node_level_list[n_y] > jl, ADJ_Matrix[n_y][
            n_x], 0) for n_y in
                   range(n_x)]) == 0)  # jl 约束向前
    for n_x in range(n - 1):
        s.add(Sum([If(node_level_list[n_y] - node_level_list[n_x] > 0, ADJ_Matrix[n_x][n_y], 0) for n_y in
                   range(n_x + 1, n)]) >= 1)  # jl 约束后前
        s.add(Sum([If(node_level_list[n_y] - node_level_list[n_x] > jl, ADJ_Matrix[n_x][n_y], 0) for n_y in
                   range(n_x + 1, n)]) == 0)  # jl 约束后前
    # (4) 稠密度约束  必须小于 connection_ratio 即 m 小于 connection_ratio * n * （n-1） / 2
    s.add(Sum([ADJ_Matrix[n_x][n_y] for n_x in range(n) for n_y in range(n_x + 1, n)]) <= (
                connection_ratio * n * (n - 1) / 2))
    # (5) 度约束
    for n_x in range(n):
        sum_out_degree = [ADJ_Matrix[n_x][n_y] for n_y in range(n_x + 1, n)]
        sum_in_degree = [ADJ_Matrix[n_y][n_x] for n_y in range(n_x)]
        s.add(Sum(sum_in_degree) <= max_in_degree)  # (6) 出度约束
        s.add(Sum(sum_out_degree) <= max_in_degree)  # (7) 入度约束
        # s.add(Sum(sum_out_degree + sum_in_degree) <= max_degree)  # (8) 度约束

    # (6) DAG的width 约束：
    # TEM1_Matrix_Array = np.array(TEM_Matrix_1)
    # for i in range(n):
    #     for j in range(n):
    #         if i == j:
    #             s.add(TEM1_Matrix_Array[i][j] == 1)
    #         else:
    #             s.add(TEM1_Matrix_Array[i][j] == ADJ_Matrix[i][j])
    # TEM1_Matrix_Array = np.linalg.matrix_power(TEM1_Matrix_Array, n)
    #
    # for n_x in range(n):
    #     for n_y in range(n):
    #         if n_x >= n_y:
    #             s.add(ACC_Matrix[n_x][n_y] == 0)
    #         else:
    #             s.add(ACC_Matrix[n_x][n_y] == If(TEM1_Matrix_Array[n_x][n_y] > 0, 1, 0))

    Temp_DAG_list = []
    for sDAG_NUM in range(DAG_Num):
        if str(s.check()) == 'sat':
            result = s.model()
            ret_list = [result[node_level_list[x]].as_long() for x in range(n)]
            # print(ret_list) # 邻接矩阵
            r = [[result[ADJ_Matrix[i][j]].as_long() for j in range(n)] for i in range(n)]
            print("")
            # for rx in r:
            #     print(rx)
            # rr = [[result[ACC_Matrix[i][j]].as_long() for j in range(n)] for i in range(n)]
            # print("")
            # for rx in rr:
            #     print(rx)
            Temp_G = nx.DiGraph(np.array(r))
            Temp_G.graph['DAG_ID'] = str(sDAG_NUM)
            # 生成结果检查
            assert format(nx.is_directed_acyclic_graph(Temp_G))
            for node_x in Temp_G.nodes(data=True):
                t_edges_list = ''
                for s_node_x in list(Temp_G.successors( node_x[0] )):
                    t_edges_list += '({0},{1});'.format(node_x[0], s_node_x)
                node_x[1]['Edges_List'] = t_edges_list
                node_x[1]['Node_Index'] = node_x[0]
                node_x[1]['Node_ID'] = node_x[0]
            # assert shape_list == [sorted(generation) for generation in nx.topological_generations(Temp_G)]
            Temp_DAG_list.append(Temp_G)
            s.add(Or([ADJ_Matrix[i][j] != result[ADJ_Matrix[i][j]] for i in range(n) for j in range(n)]))
        else:
            print("fully output!\n")
            return Temp_DAG_list
    return Temp_DAG_list
"""
node_num = 20
shape_num = 6
width = 6
max_shape = 5
min_shape = 1
max_out_degree = 4
max_in_degree = 4


# 设置变量---addVar()。
# 更新变量空间---update()。
# 设定目标函数---setObjective()。
# 设定约束条件---addConstr()。
# 执行最优化---optimize()。

try:
    m = gp.Model("DAG_AM")  # Create a new model
    AM = m.addMVar((node_num, node_num), vtype=GRB.BINARY, name="AM")    # Create a 2-D array of binary variables   AM,
    Test_AM = m.addMVar((3, 3), vtype=GRB.INTEGER, name="Test_AM")    # Create a 2-D array of binary variables   AM,
    test = m.addVar(vtype=GRB.INTEGER, name="test")    # Create a 2-D array of binary variables   AM,
    m.addConstr(test == 1, name=f"test")
    Shape_List = m.addMVar(shape_num, vtype=GRB.INTEGER, name="Shape_List")    # Create a 1-D array of binary variables   AM,
    Node_Level_List = m.addMVar((node_num), vtype=GRB.INTEGER, name="Node_Level_List")    # Create a 1-D array of binary variables   AM,

    for shape_x in range(shape_num):        # ([:)不能是0)
        if shape_x == 0 or shape_x == shape_num - 1:
            m.addConstr(Shape_List[shape_x] == 1, name=f"source and sink node num")
        else:
            m.addConstr(Shape_List[shape_x] <= width, name=f"width num")
            m.addConstr(Shape_List[shape_x] <= max_shape, name=f"max shape {shape_x}")
            m.addConstr(min_shape <= Shape_List[shape_x], name=f"min shape {shape_x}")
            m.addConstr(Shape_List[shape_x] <= Shape_List[shape_x + 1] * max_in_degree, name=f"nest_level_node_num {shape_x}")
            m.addConstr(Shape_List[shape_x] <= Shape_List[shape_x - 1] * max_out_degree, name=f"last_level_node_num {shape_x}")
    m.addConstr(Shape_List.sum() == node_num, name=f"node num shape")

    # m.addConstr(Test_AM[test, test] == 33, name=f"test test test")

    for node_x in range(node_num):
        if node_x == 0:
            m.addConstr(Node_Level_List[node_x] == 0, name=f"shapo_num_(1)_{node_x}")
        elif node_x == node_num - 1:
            m.addConstr(Node_Level_List[node_x] == shape_num - 1, name=f"shapo_num_(1)_{node_x}")
        else:
            m.addConstr(Node_Level_List[node_x] >= Node_Level_List[node_x-1], name=f"shapo_num_(1)_{node_x}")
    for shape_x in range(shape_num):
        if shape_x == 0:
            pass
        elif shape_x == shape_num - 1:
            pass
        else:
            pass
        pass

    # (0) 下三角 && 对角线全部为0
    for x in range(node_num):
        m.addConstr(AM[x, :x + 1] == 0, name=f"Lower Triangle Row {x}")     # ([:)不能是0)
    # (1) 上三角基本数据约束
    # for x in range(node_num-1):
    #     m.addConstr(AM[x, x + 1:] == 1, name=f"Upper Triangle Row {x}")     # ([:)不能是0)    # (2.1) 确定shape
    # node_num_x = 0
    # for shape_x in range(shape_num):
    #     node_num_old_x = node_num_x
    #     node_num_x = Shape_List[shape_x]
    #     # m.addConstr(AM[node_num_old_x:node_num_x, node_num_old_x:node_num_x] == 0, name=f"Triangle RXC {shape_x}")
    #
    # # (2.2) shape内元素为0
    # for n_x in range(n):
    #     s.add([ADJ_Matrix[n_x][n_y] == If(node_level_list[n_x] == node_level_list[n_y], 0, ADJ_Matrix[n_x][n_y]) for
    #            n_y in range(n_x + 1, n)])

    # for n_x in range(1, n-1):
    #     m.addConstr(AM[x, x + 1:] == 1, name=f"row{x}")
    #     s.add(node_level_list[n_x] < k, node_level_list[n_x] > 1)
        # s.add(node_level_list[n_x] >= node_level_list[n_x - 1], node_level_list[n_x] <= node_level_list[n_x + 1])  # 层数顺序递增

    # for x in range(n):
    #     for y in range(n):
    #         if x == 3 and y == 1:
    #             m.addConstr(AM[x, y] == 1, name=f"row(x)_(y)")
    #         else:
    #             m.addConstr(AM[x, y] == 0, name=f"row(x)_(y)")

    # # (1) 上三角基本数据约束
    # for x in range(n):
    #     for y in range(x):
    #         m.addConstr(AM[x, y] == 1, name=f"col(x)_(y)")

    # Optimize model
    # 开始优化模型
    m.optimize()

    print(AM.X)
    print(test.X)
    print(Shape_List.X)
    print(Node_Level_List.X)
    print('Queens placed: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')

# #### DAG generator mine 算法  #### #
# def __gen_mine_new(Param_Dict):
    # assert (Param_Dict['Node_Num'] > 3)
    # assert (Param_Dict['Critic_Path'] > 3)
    # assert (Param_Dict['Jump_level'] >= 1)
    # assert (Param_Dict['Max_in_degree'] >= 1)
    # assert (Param_Dict['Max_out_degree'] >= 1)
    # assert (Param_Dict['Max_Shape'] >= Param_Dict['Min_Shape'])
    # assert (Param_Dict['Min_Shape'] >= 1)
    # assert (Param_Dict['Width'] >= Param_Dict['Max_Shape'])
    # assert ((Param_Dict['Node_Num'] - 2) <= Param_Dict['Max_Shape'] * (Param_Dict['Critic_Path'] - 2))
    # assert ((Param_Dict['Node_Num'] - 2) >= Param_Dict['Min_Shape'] * (Param_Dict['Critic_Path'] - 2))
    # # assert (len(sample_list) > 0)
    # # for sample_list_x in sample_list:
    # #     assert (sum(sample_list_x) == n)
    # #     assert (sum(sample_list_x) == n)
    # #     assert (len(sample_list_x) == k)
    # #     assert (max(sample_list_x) <= width)
    # #     assert (max(sample_list_x[1:-1]) <= max_shape)
    # #     assert (min(sample_list_x[1:-1]) >= min_shape)
    #
    # # 参数定义：
    # n = Param_Dict['Node_Num']
    # k = Param_Dict['Critic_Path']
    # max_shape = Param_Dict['Max_Shape']
    # min_shape = Param_Dict['Min_Shape']
    # max_out_degree = Param_Dict['Max_out_degree']
    # max_in_degree = Param_Dict['Max_in_degree']
    # width = Param_Dict['Width']
    # jl = Param_Dict['Jump_level']
    # connection_ratio = Param_Dict['Conn_ratio']
    # DAG_Num = Param_Dict['DAG_Num']

