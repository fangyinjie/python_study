#!/usr/bin/python3
# -*- coding: utf-8 -*-

################################################################################
# Randomized DAG Generator
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
################################################################################
import math
from random import randint, random, uniform
import random as rand
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import graphviz as gz
import xlwt
# Class: DAG (Directed Acyclic Graph Task)
# Section_0: DAG basic function
# Section_1: DAG  随机生成算法
# Section_2: ETC  随机生成算法
# Section_3: 优先级配置算法
# Section_4: 响应时间分析算法
# Section_5: DAG的关键参数分析
# Show DAG


class DAG:
    #####################################
    #   DAG parameter
    #####################################
    def __init__(self):
        # todo DAG Basic parameter
        self.DAG_ID = ''            # DAG的名称
        self.G = nx.DiGraph()       # DAG:-networkX struct

        # todo Generator input parameter
        self.p = 0
        self.n = 0
        self.m = 0

        self.Width = 0                  # 最大anti-chain数量；
        self.Jump_Level = 0             # DAG 中两个节点之间的边的最大长度；
        self.Critical_Path_Length = 0   # 关键路径长度，DAG的长度；(结点个数来给你)
        self.parallelism = 1
        self.Critical_path = 3

        # todo (1)shape relevant
        self.Max_Shape = 0      # max-shape；
        self.Min_Shape = 0      # min-shape；
        self.Ave_Shape = 0      # ave-shape；
        self.Std_Shape = 0      # std-shape；

        self.Max_Reverse_Shape = 0  # max-shape；
        self.Min_Reverse_Shape = 0  # min-shape；
        self.Ave_Reverse_Shape = 0  # ave-shape；
        self.Std_Reverse_Shape = 0  # std-shape；

        # todo (2)shape relevant
        self.Max_In_Degree = 0   # max-degree；
        self.Min_In_Degree = 0   # max-degree；
        self.Ave_In_Degree = 0   # ave-degree；
        self.Std_In_Degree = 0   # std-degree；

        self.Max_Out_Degree = 0  # max-degree；
        self.Min_Out_Degree = 0  # max-degree；
        self.Ave_Out_Degree = 0  # ave-degree；
        self.Std_Out_Degree = 0  # std-degree；

        self.Max_Degree = 0      # max-degree；
        self.Min_Degree = 0      # max-degree；
        self.Ave_Degree = 0      # ave-degree；
        self.Std_Degree = 0      # std-degree；

        # todo (3)shape relevant
        self.Max_WCET = 0
        self.Min_WCET = 0
        self.Ave_WCET = 0
        self.Std_WCET = 0
        self.DAG_volume = 0

        # self.Priority = 1              # DAG的优先级，默认越小等级越高
        # self.Start_Time = 0            # 第一个DAG的到达时间（默认为0）
        # self.Deadline = 0              # DAG的相对截止时间
        # self.Cycle_Time = 0            # 周期DAG的循环时间、零散DAG的最短时间间隔
        # self.status = 'unfinish'       # 分为 'finish' 和 'unfinish'
        # self.DAG_name = 'Tau_{null}'   # DAG save的名称
        # self.Periodically = 'APERIODIC'# 'PERIODIC'：周期任务；'SPORADIC'：零星任务；'APERIODIC'：非周期任务(只运行一次)
        # self.Real_Time = 'HRT'         # 'HRT'：硬实时, 'SRT'：软实时, 'FRT'：固实时

    #####################################
    #   Section_0: DAG Basic function
    #####################################
    # #### Gets the nodes in the ready state of the DAG #### #
    def get_ready_node_list(self):
        return [x for x in self.G.nodes(data=True) if (x[1].get('state') == 'ready')]

    # #### get the amount of node in the DAG #### #
    def get_node_num(self):
        return self.G.number_of_nodes()

    # #### get the volume of DAG (workload)#### #
    def get_dag_volume(self):
        volume = 0
        for node_x in self.G.nodes(data=True):
            volume += node_x[1]['WCET']
        return volume

    # #### get the median of DAG (中位数)#### #
    def get_dag_median(self):
        node_c = self.get_node_num()
        wcet_list = []
        for node_x in self.G.nodes(data=True):
            wcet_list.append(node_x[1]['WCET'])
        l = sorted(wcet_list)  # sorted(a)对列表进行排序，结果返回一个列表
        index = (int) (node_c / 2)  # 获取中间值索引（分两种情况）
        if len(l) % 2 == 0:     # 偶数
            return (l[index] + l[index - 1]) / 2
        else:                   # 基数
            return l[index]

    # #### 设置DAG的shape level或rank #### #
    def set_DAG_shape_level(self):
        # #### 3.获取拓扑分层 shape #### #
        rank_list = [sorted(generation) for generation in nx.topological_generations(self.G)]
        rank_num_list = [len(x) for x in rank_list]
        for x in range(len(rank_list)):
            for y in rank_list[x]:
                node_temp = self.G.nodes[y]
                node_temp['rank'] = x

    # #### Transitive reduction Function #### #
    #   param:  matrix: Adjacency Matrix
    #   return: A matrix that has been reduced in transitive
    def transitive_reduction_matrix(self):
        matrix = np.array(nx.adjacency_matrix(self.G).todense())
        row, columns = matrix.shape
        assert (row == self.task_num)
        assert (columns == self.task_num)
        print("matrix shape is ({0},{1})".format(row, columns))
        i_test = np.eye(self.task_num).astype(bool)
        i_matrix = matrix.astype(bool)
        D = np.power((i_matrix | i_test), self.task_num)  # (M | I)^n
        D = D.astype(bool) & (~i_test)
        TR = matrix & (~(np.dot(i_matrix, D)))  # Tr = T ∩ （-（T . D））
        return nx.DiGraph(TR)

    # #### critical path configuration #### #
    def critical_path_config(self):
        WCET = nx.get_node_attributes(self.G, 'WCET')
        for edge_x in self.G.edges(data=True):
            edge_x[2]['weight'] = WCET[edge_x[1]]
        node_list = nx.dag_longest_path(self.G, weight='weight')  # 关键路径
        for node_xx in self.G.nodes(data=True):
            if node_xx[0] in node_list:  # 判断是否在关键路径里
                node_xx[1]['critic'] = True
        # print('关键路径：{0}'.format(node_list))

    #####################################
    #   Section_1: DAG 随机生成函数
    #####################################
    def DAG_Generator(self, DAG_Generator_algorithm):
        if DAG_Generator_algorithm == "mine":
            self.gen_mine()
        elif DAG_Generator_algorithm == "GNM":
            self.gen_gnm(n=self.n, m=self.m)
        elif DAG_Generator_algorithm == "GNP":
            self.gen_gnp(n=self.n, p=self.p)       # 将所有前驱为0的和source连接，后继为0的和sink连接
        elif DAG_Generator_algorithm == "Layer_By_Layer":
            pass
        elif DAG_Generator_algorithm == "Fan_in_Fan_out":
            pass
        elif DAG_Generator_algorithm == "Random_Order":
            pass
        else:
            return False
        return 0

    # #### DAG generator mine 算法  #### #
    def gen_mine(self):
        assert (self.parallelism >= 1)
        assert (self.Critical_Path_Length >= 3)
        # 步骤一：initial a new graph G               # e.g. G = nx.DiGraph(Index=self.task_num)
        #   添加节点；确定rank的节点
        self_critical_path  = self.Critical_Path_Length    # 关键路径长度
        self_parallelism    = self.parallelism      # 图的并行度
        self_Node_num       = 0                     # DAG的节点数量
        self.G.add_node(0, Node_ID='souce', rank=0, critic=False, WCET=1, priority=1, state='blocked')  # 起始节点（1）；rank=0

        for x in range(1, self_critical_path - 1):
            m = randint(1, self_parallelism)        # 随机每层的节点数量（不能大于并行度）
            for y in range(1, m + 1):
                self_Node_num += 1
                self.G.add_node(self_Node_num, Node_ID='job{}'.format(self_Node_num), rank=x, critic=False, WCET=1, priority=1, state='blocked')
        self.G.add_node(self_Node_num + 1, Node_ID='sink', rank=self_critical_path - 1, critic=False, WCET=1, priority=1, state='blocked')
        self.task_num = self_Node_num + 2  # +2算上source和sink
        self.G.add_edge(0, 1)
        for x in range(1, self_critical_path - 1):  # 从第2层开始到倒数第二层
            ancestors_list      = [node_x for node_x in self.G.nodes(data=True) if (node_x[1].get('rank') < x)]
            descendants_list    = [node_x for node_x in self.G.nodes(data=True) if (node_x[1].get('rank') > x)]
            self_list           = [node_x for node_x in self.G.nodes(data=True) if (node_x[1].get('rank') == x)]
            successors_list     = [node_x for node_x in self.G.nodes(data=True) if (node_x[1].get('rank') == (x + 1))]
            for y in self_list:
                k1 = randint(1, len(ancestors_list))                    # 在祖先节点中随机几个节点作为前驱
                ancestors_group = rand.sample(ancestors_list, k1)
                k2 = randint(1, len(descendants_list))                  # 在后代节点中随机几个节点作为后继
                descendants_group = rand.sample(descendants_list, k2)
                for z in ancestors_group:
                    self.G.add_edge(z[0], y[0])
                for z in descendants_group:
                    self.G.add_edge(y[0], z[0])
            self.G.add_edge(self_list[0][0], successors_list[0][0])
        self.name = 'Tau_{:d}'.format(self.task_num)
        # self.G = nx.DiGraph(self.Matrix)                  # 邻接矩阵生成一个有向图netWorkX；属性全无；
        """ 
        # ## transitive reduction 传递约简； ## #
        # lp = list(nx.DiGraph(self.transitive_reduction_matrix()).edges())     # 1.networkx包
        lp = list(nx.transitive_reduction(self.G).edges())                  # 2.networkx包
        self.G.clear_edges()
        self.G.add_edges_from(lp)
        # print(np.array(nx.adjacency_matrix(self.G).todense()))
        """

    # #### DAG generator GNP 算法  #### #
    def gen_gnp(self, n, p):
        Temp_Matrix = np.zeros((n, n), dtype=bool)
        for x in range(1, n-1):
            for y in range(x+1, n-1):
                if random() < p:
                    Temp_Matrix[x][y] = True
        self.G = nx.from_numpy_matrix(np.array(Temp_Matrix), create_using=nx.DiGraph)
        while True:
            # self.G = nx.fast_gnp_random_graph(n=n, p=p, seed=None, directed=True)
            for x in self.G.nodes(data=True):
                x[1]['Node_ID']     = 'Job_{0}'.format(x[0])
                x[1]['rank']        = 0
                x[1]['critic']      = False
                x[1]['WCET']        = 1
                x[1]['priority']    = 1
                x[1]['state']       = 'blocked'
                # 无前驱节点的连接到0
                if len(list(self.G.predecessors(x[0]))) == 0:
                    if x[0] != 0:
                        self.G.add_edge(0, x[0])
                # 无前后继点的连接到n-1
                if len(list(self.G.successors(x[0]))) == 0:
                    if x[0] != n-1:
                        self.G.add_edge(x[0], n-1)
            if nx.is_directed_acyclic_graph(self.G):
                break
            else:
                print("GNP Failed")

    # #### DAG generator GNM 算法  #### #
    def gen_gnm(self, n, m):
        assert n * (n - 1) >= m >= n - 1
        All_edges_list = []
        for x in range(n):
            for y in range(x + 1, n):
                All_edges_list.append((x, y))
        Temp_edges_list = rand.sample(All_edges_list, m)
        self.G.add_edges_from(Temp_edges_list)
        for x in self.G.nodes(data=True):
            x[1]['Node_ID']     = 'Job_{0}'.format(x[0])
            x[1]['rank']        = 0
            x[1]['critic']      = False
            x[1]['WCET']        = 1
            x[1]['priority']    = 1
            x[1]['state']       = 'blocked'
            if (len(list(self.G.predecessors(x[0]))) == 0) and (x[0] != 0):
                self.G.add_edge(0, x[0])
            if (len(list(self.G.successors(x[0]))) == 0) and (x[0] != n-1):
                self.G.add_edge(x[0], n-1)
        assert nx.is_directed_acyclic_graph(self.G)

    # #### DAG generator Layer_By_Layer 算法  #### #
    def gen_layer_by_layer(self, n, m):
        pass

    # #### DAG generator Fan_in_Fan_out 算法  #### #
    def gen_fan_in_fan_out(self, n, m):
        pass

    # #### DAG generator Random_Order 算法  #### #
    def gen_random_order(self, n, m):
        pass

    #####################################
    #   Section_2: WCET 配置算法 #
    #   参数a： 均匀分布的最小值、高斯分布的均值
    #   参数b： 均匀分布的最大值、高斯分布的方差
    #####################################
    def WCET_Config(self, WCET_Config_type, a, b):
        # 方式1（均匀分布）：在区间[a, b]中均匀分布方式生成 WCET
        if WCET_Config_type == "random":
            for x in self.G.nodes(data=True):
                x[1]['WCET'] = math.ceil(np.random.uniform(a, b))
                x[1]['BCET'] = x[1]['WCET']
                x[1]['ACET'] = x[1]['WCET']
        # 方式2（正态分布）：以loc=a为均值，以scale=b为方差 # size:输出形式 / 维度
        elif WCET_Config_type == "normal":
            for x in self.G.nodes(data=True):
                while True:
                    x[1]['WCET'] = math.ceil(np.random.normal(loc=a, scale=b, size=None))
                    if x[1]['WCET'] > 0:
                        x[1]['BCET'] = x[1]['WCET']
                        x[1]['ACET'] = x[1]['WCET']
                        break
        # 方式3（高斯分布，gauss）以均值为mu=a，标准偏差为sigma=b的方式生成 WCET
        elif WCET_Config_type == "gauss":
            for x in self.G.nodes(data=True):
                while True:
                    x[1]['WCET'] = math.ceil(rand.gauss(a, b))
                    if x[1]['WCET'] > 0:
                        x[1]['BCET'] = x[1]['WCET']
                        x[1]['ACET'] = x[1]['WCET']
                        break
        else:
            pass

    #####################################
    #   Section_3: 优先级 配置算法 #
    #####################################
    def Priority_Config(self, Priority_Config_type):
        if Priority_Config_type == "random":
            self.priority_random_config()
        elif Priority_Config_type == "Zhao":
            self.priority_Zhao_config()
        elif Priority_Config_type == "He2019":
            self.priority_He2019_config()
        elif Priority_Config_type == "He2021":
            self.priority_He2021_config()
        elif Priority_Config_type == "Chen":
            self.priority_Chen_config()
        elif Priority_Config_type == "Mine":
            self.priority_Mine_config()
        elif Priority_Config_type == "WCET":
            self.priority_WCET_config()
        else:
            print("priority config error!\n")

    def priority_random_config(self):
        priority_random_list = list(range(0, self.G.number_of_nodes()))
        np.random.shuffle(priority_random_list)
        for x in self.G.nodes(data=True):
            x[1]['priority'] = priority_random_list.pop()

    def priority_Zhao_config(self):
        pass

    def priority_He2019_config(self):
        pass

    def priority_He2021_config(self):
        pass

    def priority_Chen_config(self):
        # 1. 关键路径分组；
        node_list = nx.dag_longest_path(self.G, weight='weight')  # 关键路径
        for x in node_list:
            temp_c_node = self.G.node[x]
        print('关键路径：{0}'.format(node_list))
        # 2. 到sink的路径最长者优先；
        # 3. wcet优先；
        # 4. 关键路径优先；
        pass

    def priority_Mine_config(self):

        pass

    def priority_WCET_config(self):
        temp_node_wcet = nx.get_node_attributes(self.G, 'WCET')
        temp_node_wcet = dict(sorted(temp_node_wcet.items(), key=lambda x: x[1], reverse=True))
        Temp_1 = 1
        for k, v in temp_node_wcet.items():
            self.G.node[k]['priority'] = Temp_1
            Temp_1 += 1
        return False

    #####################################
    #   Section_4: response time analysis arithmetic #
    #####################################
    def Response_Time_analysis(self, RTA_Type, core_num):
        if RTA_Type == "non-preemptive":
            return self.rta_basics_non_preemptive(core_num)
        elif RTA_Type == "preemptive":
            return self.rta_basics_preemptive(core_num)
        else:
            print("RTA_Type input error!")

    def rta_basics_non_preemptive(self, core_num):
        node_list = list(self.G.nodes())
        paths = list(nx.all_simple_paths(self.G, node_list[0], node_list[-1]))

        interference_node_list = []
        ret_path_and_rta = [0, 0, 0, [], []]
        for x in paths:
            temp_interference_node_list = []
            temp_path_weight = 0
            for y in x:
                temp_all_node = self.G.nodes(data=True)
                temp_ance = list(nx.ancestors(self.G, y))
                temp_desc = list(nx.descendants(self.G, y))
                temp_self = x
                sub_node = self.G.nodes[y]
                for z in temp_all_node:
                    if (z[0] not in temp_ance) and (z[0] not in temp_desc) and (z[0] not in temp_self):  # 判断z是否是干扰节点
                        if z[1]['priority'] < sub_node.get('priority'):             # 判断此z的优先级是否大于y
                            if z not in temp_interference_node_list:            # 判断此z是否已经加入
                                temp_interference_node_list.append(z)
                temp_path_weight += sub_node.get('WCET')
                # 每个节点的非前驱和非后继节点
            temp_inter_weight = 0
            for y in temp_interference_node_list:
                temp_inter_weight += y[1]['WCET']
            interference_node_list.append(temp_interference_node_list)
            temp_rta = temp_path_weight + temp_inter_weight/core_num
            # 计算此路径的RTA
            # ret_path_and_rta.append((temp_rta, temp_path_weight, temp_inter_weight, x, temp_interference_node_list))
            if temp_rta > ret_path_and_rta[0]:
                ret_path_and_rta[0] = temp_rta
                ret_path_and_rta[1] = temp_path_weight
                ret_path_and_rta[2] = temp_inter_weight
                ret_path_and_rta[3] = x
                ret_path_and_rta[4] = temp_interference_node_list
        return math.ceil(ret_path_and_rta[0])

    def rta_basics_preemptive(self, core_num):
        node_list = list(self.G.nodes())
        paths = list(nx.all_simple_paths(self.G, node_list[0], node_list[-1]))

        interference_node_list = []
        ret_path_and_rta = [0, 0, 0, [], []]
        for x in paths:
            temp_interference_node_list = []
            reserve_node_list = {}
            temp_path_weight = 0
            temp_WCET = []
            for y in x:
                temp_all_node = self.G.nodes(data=True)
                temp_ance = list(nx.ancestors(self.G, y))
                temp_desc = list(nx.descendants(self.G, y))
                temp_self = x
                sub_node = self.G.nodes[y]
                temp_path_weight += sub_node.get('WCET')
                temp_WCET.append(sub_node.get('WCET'))
                for z in temp_all_node:
                    if (z[0] not in temp_ance) and (z[0] not in temp_desc) and (z[0] not in temp_self):  # 判断z是否是干扰节点
                        if z[1]['priority'] < sub_node.get('priority'):   # 判断此z的优先级是否大于y
                            if z not in temp_interference_node_list:            # 判断此z是否已经加入
                                temp_interference_node_list.append(z)
                        else:
                            reserve_node_list[z[0]] = z[1]['WCET']
            t_reserve_list = sorted(reserve_node_list.items(), key=lambda x: x[1])
            add_reserve = 0
            for y in range(0, min(core_num, len(t_reserve_list))):
                add_reserve += t_reserve_list[y][1]
            temp_inter_weight = 0
            for y in temp_interference_node_list:
                temp_inter_weight += y[1]['WCET']
            interference_node_list.append(temp_interference_node_list)
            temp_rta = temp_path_weight + (temp_inter_weight+add_reserve)/core_num
            # 计算此路径的RTA
            if temp_rta > ret_path_and_rta[0]:
                ret_path_and_rta[0] = temp_rta
                ret_path_and_rta[1] = temp_path_weight
                ret_path_and_rta[2] = temp_inter_weight
                ret_path_and_rta[3] = x
                ret_path_and_rta[4] = temp_interference_node_list
        return math.ceil(ret_path_and_rta[0])

    #####################################
    #   Section_5: DAG的关键参数分析
    #####################################
    def dag_param_critical_update(self, i, worksheet):
        # #### 0.DAG检测及基本参数 #### #
        assert format(nx.is_directed_acyclic_graph(self.G))     # 检测是否是有向无环图
        print("DAG_ID:", self.DAG_ID)                           # 1.打印DAG的ID
        print("Number of Nodes:", self.G.number_of_nodes())
        print("Number of Edges:", self.G.number_of_edges())
        #####################################
        #   section1. 获取DAG的结构相关参数
        #####################################
        # #### 1.关键路径 #### #
        # node_list = nx.dag_longest_path(self.G, weight='weight')  # 关键路径
        # print('关键路径：{0}'.format(node_list))
        # #### 2.最短路径 #### #
        # shortest_path = list(nx.all_shortest_paths(self.G, 0, self.G.number_of_nodes() - 1, weight='weight'))
        # print('DAG的最短路径{0}条：'.format(len(shortest_path)))
        # [print(path) for path in shortest_path]
        # #### 3.获取拓扑分层 shape #### #
        # 3.1 正向shape
        rank_list = [sorted(generation) for generation in nx.topological_generations(self.G)]
        rank_num_list = [len(x) for x in rank_list]
        print('拓扑分层：{0}'.format(rank_list))
        print('拓扑分层节点数量分布：{0}'.format(rank_num_list))
        print("Max_Shape:{0}".format( max(rank_num_list) ))
        print("Min_Shape:{0}".format( min(rank_num_list) ))
        print("Ave_Shape:{0:0.2f}".format( np.mean(rank_num_list) ))
        print("Std_Shape:{0:0.2f}".format( np.std(rank_num_list) ))

        self.Max_Shape = max(rank_num_list)      # max-shape；
        self.Min_Shape = min(rank_num_list)      # min-shape；
        self.Ave_Shape = np.mean(rank_num_list)  # ave-shape；
        self.Std_Shape = np.std(rank_num_list)   # std-shape；

        # 3.2 反向shape
        re_rank_list = [sorted(generation) for generation in nx.topological_generations(nx.DiGraph.reverse(self.G))]
        re_rank_list.reverse()
        re_rank_num_list = [len(x) for x in re_rank_list]
        print('反向拓扑分层：{0}'.format(re_rank_list))
        print('反向拓扑分层节点数量分布：{0}'.format(re_rank_num_list))
        print("Max_re_shape:{0}".format( max(re_rank_num_list) ))
        print("Min_re_shape:{0}".format( min(re_rank_num_list) ))
        print("Ave_re_shape:{0:0.2f}".format( np.mean(re_rank_num_list) ))
        print("Std_re_shape:{0:0.2f}".format( np.std(re_rank_num_list) ))

        self.Max_Reverse_Shape = max(re_rank_num_list)      # max-shape；
        self.Min_Reverse_Shape = min(re_rank_num_list)      # min-shape；
        self.Ave_Reverse_Shape = np.mean(re_rank_num_list)  # ave-shape；
        self.Std_Reverse_Shape = np.std(re_rank_num_list)   # std-shape；

        # #### 5.antichains #### #
        # print("anti-chains", list(nx.antichains(self.G, topo_order=None)))  # 从DAG中生成antichains；
        anti_chains_list = list(nx.antichains(self.G, topo_order=None))
        print("anti-chains:", anti_chains_list)  # 从DAG中生成antichains；
        anti_chains_num_list = [len(x) for x in anti_chains_list]
        print("max anti-chains (Width):", max(anti_chains_num_list) )  # 从DAG中生成antichains；

        # #### 6.degree #### #
        degree_list = [nx.degree(self.G, self_node[0]) for self_node in self.G.nodes(data=True)]
        print("Max_Degree:{0}".format( max(degree_list) ))
        print("Min_Degree:{0}".format( min(degree_list) ))
        print("Ave_Degree:{0:0.2f}".format( np.mean(degree_list) ))
        print("Std_Degree:{0:0.2f}".format( np.std(degree_list) ))

        self.Max_Degree = max(degree_list)      # max-degree；
        self.Min_Degree = min(degree_list)      # max-degree；
        self.Ave_Degree = np.mean(degree_list)  # ave-degree；
        self.Std_Degree = np.std(degree_list)   # std-degree；

        degree_in_list = [self.G.in_degree(self_node[0]) for self_node in self.G.nodes(data=True)]
        print("Max_In_Degree:{0}".format( max(degree_in_list) ))
        print("Min_In_Degree:{0} —— 均为0".format( min(degree_in_list) ))
        print("Ave_In_Degree:{0:0.2f}".format( np.mean(degree_in_list) ))
        print("Std_In_Degree:{0:0.2f}".format( np.std(degree_in_list) ))
        self.Max_In_Degree = max(degree_in_list)      # max-degree；
        self.Min_In_Degree = min(degree_in_list)      # max-degree；
        self.Ave_In_Degree = np.mean(degree_in_list)  # ave-degree；
        self.Std_In_Degree = np.std(degree_in_list)   # std-degree；

        degree_out_list = [self.G.out_degree(self_node[0]) for self_node in self.G.nodes(data=True)]
        print("Max_Out_Degree:{0}".format( max(degree_out_list) ))
        print("Max_Out_Degree:{0} —— 均为0".format( min(degree_out_list) ))
        print("Ave_Out_Degree:{0:0.2f}".format( np.mean(degree_out_list) ))
        print("Std_Out_Degree:{0:0.2f}".format( np.std(degree_out_list) ))
        self.Max_Out_Degree = max(degree_out_list)  # max-degree；
        self.Min_Out_Degree = min(degree_out_list)  # max-degree；
        self.Ave_Out_Degree = np.mean(degree_out_list)  # ave-degree；
        self.Std_Out_Degree = np.std(degree_out_list)  # std-degree；

        # #### 7.DAG的稠密度 Density  #### #
        Dag_density = (2 * self.G.number_of_edges()) / (self.G.number_of_nodes() * (self.G.number_of_nodes()-1))
        print("稠密度：{0:2f}".format(Dag_density))

        # Edges_Jump_List = [(self.G.nodes[x[0]], self.G.nodes[x[1]]) for x in self.G.edges.data(data=True)]
        Edges_Jump_List = [self.G.nodes[x[1]]['rank'] - self.G.nodes[x[0]]['rank'] for x in self.G.edges.data(data=True)]

        self.Jump_Level = max(Edges_Jump_List)
        print("Jump_Level：{0}".format( self.Jump_Level ))
        #####################################
        #   section2. 获取DAG的时间相关参数
        #####################################
        # #### 1.DAG最差执行时间list  #### #
        WCET_list = [x[1]['WCET'] for x in self.G.nodes.data(data=True)]
        print("WCET_list：{0}".format(WCET_list))
        print("DAG_Volume：{0}".format( np.sum(WCET_list) ))
        print("Max_WCET：{0}".format( max(WCET_list) ))
        print("Min_WCET：{0}".format( min(WCET_list) ))
        print("Ave_WCET：{0:0.2f}".format( np.mean(WCET_list) ))
        print("Std_WCET：{0:0.2f}".format( np.std(WCET_list) ))

        self.DAG_volume = np.sum(WCET_list)
        self.Max_WCET = max(WCET_list)
        self.Min_WCET = min(WCET_list)
        self.Ave_WCET = np.mean(WCET_list)
        self.Std_WCET = np.std(WCET_list)

        worksheet.write(i, 0, i)
        worksheet.write(i, 1, self.G.number_of_nodes())
        worksheet.write(i, 2, self.G.number_of_edges())

        worksheet.write(i, 3, self.Max_Shape)
        worksheet.write(i, 4, self.Min_Shape)
        worksheet.write(i, 5, int(self.Ave_Shape))
        worksheet.write(i, 6, self.Std_Shape)

        worksheet.write(i, 7, self.Max_Reverse_Shape)
        worksheet.write(i, 8, self.Min_Reverse_Shape)
        worksheet.write(i, 9, self.Ave_Reverse_Shape)
        worksheet.write(i, 10, self.Std_Reverse_Shape)

        worksheet.write(i, 11, max(anti_chains_num_list) )

        worksheet.write(i, 12, self.Max_Degree)
        worksheet.write(i, 13, self.Min_Degree)
        worksheet.write(i, 14, self.Ave_Degree)
        worksheet.write(i, 15, self.Std_Degree)

        worksheet.write(i, 16, self.Max_In_Degree)
        worksheet.write(i, 17, self.Min_In_Degree)
        worksheet.write(i, 18, self.Ave_In_Degree)
        worksheet.write(i, 19, self.Std_In_Degree)

        worksheet.write(i, 20, self.Max_Out_Degree)
        worksheet.write(i, 21, self.Min_Out_Degree)
        worksheet.write(i, 22, self.Ave_Out_Degree)
        worksheet.write(i, 23, self.Std_Out_Degree)

        worksheet.write(i, 24, Dag_density)

    #########################################
    #   Show DAG
    #   DAG graph_node_position_determine
    #########################################
    def graphviz_DAG_show(self):
        dot = gz.Digraph()
        for node_x in self.G.nodes(data=True):
            temp_label = ''
            temp_label += 'Node_ID:' + str(node_x[1]['Node_ID']) + '\n'
            temp_label += 'rank:' + str(node_x[1]['rank']) + '\n'
            temp_label += 'WCET:' + str(node_x[1]['WCET']) + '\n'
            if node_x[1]['critic']:
                color_t = 'red'
            else:
                color_t = 'green'
            dot.node('%s' % node_x[0], temp_label, color=color_t)
        for edge_x in self.G.edges(data=True):
            dot.edge(str(edge_x[0]), str(edge_x[1]))
        # print(dot.source)
        # dot.view()


if __name__ == "__main__":
    workbook = xlwt.Workbook(encoding='utf-8')           # 新建一个excel
    Parallelism = 10
    Critical_Path = 10
    worksheet = workbook.add_sheet("CP={0}-PA={1}".format(Parallelism, Critical_Path))  # 新建一个sheet
    worksheet.write(0, 0, "DAG_ID")
    worksheet.write(0, 1, "Number of Nodes")
    worksheet.write(0, 2, "Number of Edges")
    worksheet.write(0, 3, "Max_Shape")
    worksheet.write(0, 4, "Min_Shape")
    worksheet.write(0, 5, "Ave_Shape")
    worksheet.write(0, 6, "Std_Shape")
    worksheet.write(0, 7, "Max_re_shape")
    worksheet.write(0, 8, "Min_re_shape")
    worksheet.write(0, 9, "Ave_re_shape")
    worksheet.write(0, 10, "Std_re_shape")
    worksheet.write(0, 11, "max anti-chains (Width)")
    worksheet.write(0, 12, "Max_Degree")
    worksheet.write(0, 13, "Min_Degree")
    worksheet.write(0, 14, "Ave_Degree")
    worksheet.write(0, 15, "Std_Degree")
    worksheet.write(0, 16, "Max_In_Degree")
    worksheet.write(0, 17, "Min_In_Degree")
    worksheet.write(0, 18, "Ave_In_Degree")
    worksheet.write(0, 19, "Std_In_Degree")
    worksheet.write(0, 20, "Max_Out_Degree")
    worksheet.write(0, 21, "Max_Out_Degree")
    worksheet.write(0, 22, "Ave_Out_Degree")
    worksheet.write(0, 23, "Std_Out_Degree")
    worksheet.write(0, 24, "稠密度")

    # worksheet.write(0, 2, "DAG_VOL")
    for i in range(1, 10000):
        ##############################
        # （0）DAG初始化
        ##############################
        G = DAG()               # 初始化DAG
        ##############################
        # （2）DAG 随机生成
        ##############################

        ##############################
        # step0. DAG参数配置
        ##############################
        G.DAG_ID = "DAG_{0}".format("1")  # 配置DAG的ID

        ##############################
        # step 1. DAG结构生成
        ##############################
        G.parallelism = Parallelism
        G.Critical_Path_Length = Critical_Path
        G.DAG_Generator("mine")
        # G.n = 80
        # G.p = 1
        # G.DAG_Generator("GNP")  # "GNP"、"mine"、"GNM"
        # G.n = 8
        # G.m = 10
        # G.DAG_Generator("GNM")  # "GNP"、"mine"、"GNM"
        ##############################
        # step 2. DAG WCET配置；
        ##############################
        G.WCET_Config("random", 1, 10000)  # gauss # random # normal
        ##############################
        # step 3. DAG 关键路径配置；
        ##############################
        G.critical_path_config()
        ############################
        # #### DAG 关键数据分析；#### #
        ############################
        G.set_DAG_shape_level()
        G.dag_param_critical_update(i, worksheet)       # 关键数据分析
        ##############################
        # step 4. DAG 展示；
        ##############################
        G.graphviz_DAG_show()
    workbook.save(str("result模块1.xls"))