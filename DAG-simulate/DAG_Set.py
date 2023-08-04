#!/usr/bin/python3
# -*- coding: utf-8 -*-

################################################################################
# Dag set
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
################################################################################

import networkx as nx
import DAG
import self_define_dag_data
import simpy
import numpy as np
import random


class DAG_Set:
    def __init__(self):
        self.Dag_Set = []
        self.priority_type = ''

    #####################################
    #  随机生成执行时间
    #####################################
    def Random_DAG_Set_ET(self):
        for x in self.Dag_Set:
            for y in x.G.nodes(data=True):
                y[1]['ET'] = np.random.randint(low=y[1].get('BCET'), high=y[1].get('WCET'))

    #####################################
    #   随机生成一组DAG
    #####################################
    def Random_DAG_Set(self, DAG_count, parallelism_list, critical_path_list):
        for x in range(0, DAG_count):
            Temp_DAG = DAG.DAG()
            Temp_DAG.DAG_ID = "DAG_{}".format(x)
            Temp_DAG.Priority = x + 1
            Temp_DAG.parallelism = parallelism_list[x]
            Temp_DAG.Critical_path = critical_path_list[x]
            # step1. DAG结构生成
            Temp_DAG.gen("mine")
            # step2. DAG WCET配置；
            Temp_DAG.WCET_Config("random")
            # step3. DAG 优先级配置；
            Temp_DAG.Priority_Config("random")
            # step4. DAG 关键路径配置；
            Temp_DAG.critical_path_config()
            # stpe5. 加入DAG 集合
            self.Add_DAG(Temp_DAG)

    def Add_DAG(self, Dag):
        self.Dag_Set.append(Dag)

    #####################################
    #   更新DAG集合中所有DAG节点的状态，
    #   即将所有前驱节点为0，状态为阻塞态的节点
    #   转换为的就绪态状态
    #####################################
    def Status_Data_Up(self):
        for x in self.Dag_Set:
            for y in x.G.nodes(data=True):
                if (len(list(x.G.predecessors(y[0]))) == 0) and (y[1].get('state') == 'blocked'):
                    y[1]['state'] = 'ready'

    def Status_Data_Up_Store(self, store):
        for x in self.Dag_Set:
            for y in x.G.nodes(data=True):
                if (len(list(x.G.predecessors(y[0]))) == 0) and (y[1].get('state') == 'blocked'):
                    store.put(simpy.PriorityItem(y[1].get('priority'), (x.DAG_ID,y)))
                    y[1]['state'] = 'ready'

    #####################################
    #   DAG的优先级配置
    #####################################
    def Single_DAG_Priority_Config_WCET(self, insert_DAG):
        temp_node_wcet_1 = nx.get_node_attributes(insert_DAG, 'WCET')
        temp_node_wcet_2 = dict(sorted(temp_node_wcet_1.items(), key=lambda x: x[1], reverse=True))
        Temp_1 = 1
        for k, v in temp_node_wcet_2.items():
            insert_DAG.node[k]['priority'] = Temp_1
            Temp_1 += 1
        return False

    def Single_DAG_Priority_Config_HUAWEI_new(self, insert_DAG):
        dag_id = insert_DAG.DAG_ID
        prio = []
        for x in insert_DAG.G.nodes(data=True):
            x[1]['priority'] = False
        if dag_id == 'M1_S1_C1':
            prio = HuaWei_M1_S1_C1
        elif dag_id == 'M1_S2_C1':
            prio = HuaWei_M1_S2_C1
        elif dag_id == 'M1_S1_C2':
            prio = HuaWei_M1_S1_C2
        elif dag_id == 'M1_S2_C2':
            prio = HuaWei_M1_S2_C2
        elif dag_id == 'M2_S1_C1':
            prio = HuaWei_M2_S1_C1
        elif dag_id == 'M2_S2_C1':
            prio = HuaWei_M2_S2_C1
        elif dag_id == 'M2_S3_C1':
            prio = HuaWei_M2_S3_C1
        elif dag_id == 'M2_S1_C2':
            prio = HuaWei_M2_S1_C2
        elif dag_id == 'M2_S2_C2':
            prio = HuaWei_M2_S2_C2
        elif dag_id == 'M2_S3_C2':
            prio = HuaWei_M2_S3_C2
        print(dag_id)
        # for x in prio:
        #     insert_DAG.G.node[x[0]]['priority'] = x[1]
        for x in insert_DAG.G.nodes(data=True):
            Node_ID = x[1]['Node_ID']
            PP =  prio[Node_ID]
            x[1]['priority'] = prio[Node_ID]
        return True

    def Single_DAG_Priority_Config_HUAWEI(self, insert_DAG):
        dag_id = insert_DAG.DAG_ID
        prio=[]
        for x in insert_DAG.G.nodes(data=True):
            x[1]['priority'] = False
        if dag_id == 'M1_S1_C1':
            prio = [(1, 1),  (2, 3),  (3, 5), (4, 4),  (5, 2),  (6, 6), (7, 7),  (8, 8),  (9, 10), (10, 9),  (11, 11),
                    (12, 13), (13, 12), (14, 14)]
        elif dag_id == 'M1_S2_C1':
            prio = [(1, 1), (2, 4), (3, 7), (4, 12), (5, 5), (6, 6), (7, 2), (8, 3), (9, 8), (10, 9), (11, 10), (12, 11),
                    (13, 13), (14, 14), (15, 15), (16, 16), (17, 21), (18, 22), (19, 17), (20, 18), (21, 19), (22, 20),
                    (23, 23), (24, 24), (25, 29), (26, 30), (27, 25), (28, 26), (29, 27), (30, 28), (31, 31), (32, 32)]
        elif dag_id == 'M1_S1_C2':
            prio = [(1, 1), (2, 3), (3, 5), (4, 4), (5, 2)]
        elif dag_id == 'M1_S2_C2':
            prio = [(1, 1), (2, 4), (3, 7), (4, 8), (5, 2), (6, 3), (7, 5), (8, 6)]
        elif dag_id == 'M2_S1_C1':
            prio = [(1,  1), (2,  2), (3,  3), (4,  4), (5,  5), (6,  6), (7,  7), (8,  9), (9,  10), (10,  11),
                    (11,  12), (12,  8)]
        elif dag_id == 'M2_S2_C1':
            prio = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8),
                    (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15),
                    (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21),
                    (22, 22), (23, 23)]
        elif dag_id == 'M2_S3_C1':
            prio = [[1, 1], [2, 2],[3, 8],[4, 9],[5, 10],[6, 11],[7, 32],[8, 3],[9, 4],
                    [10, 5], [11,  6],[12,  7], [13,  12],[14,  13],[15, 14],[16, 15],[17, 16],
                    [18, 17], [19, 18],[20, 19],[21, 20],[22, 21],[23,  22],[24,  23],[25, 24],
                    [26,  25], [27,  26],[28, 27],[29, 28],[30,  29],[31, 30],[32,  31],[33, 33],
                    [34, 34], [35, 35],[36, 36],[37, 37],[38, 44],[39, 45],[40,  46],[41,  47],
                    [42,  48],[43,  49],[44,  50],[45,  51],[46,  52],[47,  53],[48,  54],[49,  55],
                    [50,  56],[51, 57],[52, 58],[53, 59],[54, 60],[55, 61],[56,  62],[57, 63],
                    [58,  64],[59,  65],[60,  66],[61,  67],[62, 38],[63, 39],[64,  40],[65, 41],
                    [66, 42],[67, 43]]

        elif dag_id == 'M2_S1_C2':
            prio = [(1, 1), (2, 2)]
        elif dag_id == 'M2_S2_C2':
            prio = [(1, 1), (2, 2), (3, 3)]
        elif dag_id == 'M2_S3_C2':
            prio = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
        print(dag_id)
        for x in prio:
            insert_DAG.G.node[x[0]]['priority'] = x[1]
        return True

    def Single_DAG_Priority_Config_SELF(self, insert_DAG):
        dag_id = insert_DAG.DAG_ID
        prio = []
        for x in insert_DAG.G.nodes(data=True):
            x[1]['priority'] = False
        if dag_id == 'M1_S1_C1':
            prio = [[1, 1], [2, 13], [3, 12], [4, 2], [5, 14], [6, 4], [7, 3], [8, 5],
                    [9, 6], [10, 7], [11, 8], [12, 9], [13, 10], [14, 11]]
        elif dag_id == 'M1_S2_C1':
            prio = [[1, 1], [2, 26], [3, 29], [4, 30], [5, 2], [6, 14], [7, 31], [8, 32],
                    [9, 4], [10, 5], [11, 16], [12, 17], [13, 3], [14, 15], [15, 6], [16, 18],
                    [17, 7], [18, 19], [19, 8], [20, 9], [21, 20], [22, 21], [23, 10], [24, 22],
                    [25, 11], [26, 23], [27, 12], [28, 13], [29, 24], [30, 25], [31, 27], [32, 28]]
        elif dag_id == 'M1_S1_C2':
            prio = [[1, 1], [2, 4], [3, 3], [4, 2], [5, 5]]
        elif dag_id == 'M1_S2_C2':
            prio = [[1, 1], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 2], [8, 3]]
        elif dag_id == 'M2_S1_C1':
            prio = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6],
                    [7, 7], [8, 8], [9, 9], [10, 10], [11, 11], [12, 12]]
        elif dag_id == 'M2_S2_C1':
            prio = [[1, 1],
                    [2, 2], [3, 8], [4, 3], [5, 4], [6, 5], [7, 6], [8, 9], [9, 10],
                    [10, 11], [11, 12], [12, 7], [13, 13], [14, 14], [15, 15], [16, 15],
                    [17, 17], [18, 18], [19, 19], [20, 20], [21, 21], [22, 22], [23, 23]]
        elif dag_id == 'M2_S3_C1':
            prio = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8],
                    [9, 9], [10, 10], [11, 11], [12, 12], [13, 13], [14, 14], [15, 15], [16, 16],
                    [17, 17], [18, 18], [19, 19], [20, 20], [21, 21], [22, 22], [23, 23], [24, 24],
                    [25, 25], [26, 26], [27, 27], [28, 28], [29, 29], [30, 30], [31, 31], [32, 32],
                    [33, 33], [34, 34], [35, 35], [36, 36], [37, 37], [38, 38], [39, 39], [40, 40],
                    [41, 41], [42, 42], [43, 43], [44, 44], [45, 45], [46, 46], [47, 47], [48, 48],
                    [49, 49], [50, 50], [51, 51], [52, 52], [53, 53], [54, 54], [55, 55], [56, 56],
                    [57, 57], [58, 58], [59, 59], [60, 60], [61, 61], [62, 62], [63, 63], [64, 64],
                    [65, 65], [66, 66], [67, 67]]
        elif dag_id == 'M2_S1_C2':
            prio = [[1, 1], [2, 2]]
        elif dag_id == 'M2_S2_C2':
            prio = [[1, 1], [2, 2], [3, 3]]
        elif dag_id == 'M2_S3_C2':
            prio = [[1, 1], [2, 2], [3, 5], [4, 4], [5, 3], [6, 6], [7, 7]]
        print(dag_id)
        for x in prio:
            insert_DAG.G.nodes[x[0]]['priority'] = x[1]
        return True

    def Mulit_DAG_Priority_Config(self):
        DAG_list = []
        for x in self.Dag_Set:
            DAG_list.append([x, x.get_dag_median()])
        DAG_list = sorted(DAG_list, key=lambda x: x[1], reverse=True)  # 拟序（大的优先）
        for x in range(len(DAG_list)):
            t_node = DAG_list[x][0]
            t_node.Priority = x + 1


    # def Mulit_DAG_Priority_Config(self):
    #     if len(self.Dag_Set) > 1:
    #         node_num_list = []
    #         for x in self.Dag_Set:
    #             node_num_list.append(x.get_node_num())
    #         max_node_num = max(node_num_list)
    #         for x in self.Dag_Set:
    #             temp_pri = x.Priority
    #             for y in x.G.nodes(data=True):
    #                 y[1]['priority'] = y[1]['priority'] + temp_pri * max_node_num

    #####################################
    #   获取DAG集合的数量#
    #####################################
    def get_dag_num(self):
        return len(self.Dag_Set)

    def get_DAG_Set_ID(self):
        if len(self.Dag_Set) == 0:
            print('Dag_Set is null!\n')
            return False
        elif len(self.Dag_Set) == 1:
            Dag_Set_ID = self.Dag_Set[0].DAG_ID
            return Dag_Set_ID
        elif len(self.Dag_Set) > 1:
            Dag_Set_ID = self.Dag_Set[0].DAG_ID
            for x in range(1, len(self.Dag_Set)):
                Dag_Set_ID += '-AND-' + self.Dag_Set[x].DAG_ID
            return Dag_Set_ID
        else:
            print('Dag_Set is error!\n')

    def DAG_Set_volume(self):
        vol = 0
        for x in self.Dag_Set:
            vol += x.get_dag_volume()
        return vol

    #####################################
    #   根据DAG_ID 获取DAG
    #####################################
    def get_dag(self, DAG_ID):
        for x in self.Dag_Set:
            if x.DAG_ID == DAG_ID:
                return x
        return False

    # #####################################
    # #   根据DAG_ID, Node_ID 获取对应的node
    # #####################################
    # def get_node(self, DAG_ID, Node_ID):
    #     for x in self.Dag_Set:
    #         if x.DAG_ID == DAG_ID:
    #             return x.G.node[Node_ID]
    #     return False

    #####################################
    #   获取DAG集合中所有节点的数量#
    #####################################
    def get_node_num(self):
        temp_node_num = 0
        for x in self.Dag_Set:
            temp_node_num += x.get_node_num()
        return temp_node_num

    #####################################
    #   获取DAG集合中所有就绪节点
    #####################################
    def get_ready_node(self):
        temp_list = []
        for x in self.Dag_Set:
            temp_ready_list = x.get_ready_node_list()
            for y in temp_ready_list:
                temp_list.append((x.DAG_ID, y))
        return temp_list

    # def get_priorituy_ready_node(self):
    #     temp_dict = {}
    #     for x in self.Dag_Set:
    #         temp_dict[x] = x.Priority
    #     temp_dict = sorted(temp_dict.items(), key=lambda x: x[1])
    #     for k, v in temp_dict:
    #         DAG_ID = k.DAG_ID
    #         temp_ready_list = k.get_ready_node_list()
    #         if len(temp_ready_list) > 0:
    #             run_node = temp_ready_list[0]
    #             for x in temp_ready_list:
    #                 if x[1].get('priority') < run_node[1].get('priority'):
    #                     run_node = x
    #             return DAG_ID, run_node
    #     return False, False

    def get_priorituy_ready_node(self):
        temp_list = []
        # 1.SELF 严格根据
        if self.priority_type == 'SELF':
            for x in self.Dag_Set:
                temp_list.append( (x, x.Priority) )
            temp_list = sorted(temp_list, key=lambda x: x[1])
            for k, v in temp_list:
                DAG_ID = k.DAG_ID
                temp_ready_list = k.get_ready_node_list()       # 获取DAG中就绪节点
                if len(temp_ready_list) > 0:                    # 如果有就绪节点
                    temp_ready_list = sorted(temp_ready_list, key=lambda x: x[1]['priority'])
                    return DAG_ID, temp_ready_list[0]
        elif self.priority_type == 'HUAWEI':
            temp_ready_list = []
            for x in self.Dag_Set:
                tt = x.get_ready_node_list()
                for y in tt:
                    temp_ready_list.append([x.DAG_ID, y])
            if len(temp_ready_list) > 0:
                # 1.WCET最小优先
                # temp_ready_list = sorted(temp_ready_list, key=lambda x: x[1][1]['WCET'], reverse=False) # False是顺序
                # 2.优先级高优先
                temp_ready_list = sorted(temp_ready_list, key=lambda x: x[1][1]['priority'])
                # 3.符合条件元素中随机选择
                temp_ready_list = [x for x in temp_ready_list if x[1][1]['priority'] == temp_ready_list[0][1][1]['priority']]
                random.shuffle(temp_ready_list)
                return temp_ready_list[0][0], temp_ready_list[0][1]
        return False, False


    def get_priorituy_ready_node_list(self):
        temp_dict = {}
        r_dict = {}
        ret_list = []
        for x in self.Dag_Set:
            temp_dict[x] = x.Priority
        temp_dict = sorted(temp_dict.items(), key=lambda x: x[1])
        for k, v in temp_dict:
            DAG_ID = k.DAG_ID
            temp_ready_list = k.get_ready_node_list()
            if len(temp_ready_list) == 0:
                continue
            ret_list.append((DAG_ID, temp_ready_list))
        return ret_list
        # return False, False

    def delet_DAG_Node(self, DAG_ID, Node_ID):
        for x in self.Dag_Set:
            if x.DAG_ID == DAG_ID:
                x.G.remove_node(Node_ID)

    #####################################
    #   Show_DAG_Set
    #####################################
    def Show_DAG_Set(self):
        print("DAG_num:", len(self.Dag_Set))
        print("")
        # for x in self.Dag_Set:
        #     x.show_dag()

    #####################################
    #   自定义 DAG 算法#
    #####################################
    def user_defined_priority(self):
        # self.priority_type = priority_type
        if self.priority_type == 'WCET':
            for x in self.Dag_Set:
                self.Single_DAG_Priority_Config_WCET(x.G)
        elif self.priority_type == 'SELF':
            for x in self.Dag_Set:
                self.Single_DAG_Priority_Config_SELF(x)
        elif self.priority_type == 'HUAWEI':
            for x in self.Dag_Set:
                # self.Single_DAG_Priority_Config_HUAWEI(x)
                self.Single_DAG_Priority_Config_HUAWEI_new(x)
        else:
            print('priority_type error!\n')

    def user_defined_dag(self, DAG_Set_ID_list, algorithm_type):
        self.priority_type = algorithm_type
        G1_1_1_M = mode1_scene1_case1_2c1f()
        G1_2_1_M = mode1_scene2_case1_3c2f()
        G1_1_2_M = mode1_scene1_case2_2c1f()
        G1_2_2_M = mode1_scene2_case2_3c2f()
        G2_1_1_M = mode2_scene1_case1_2c1f()
        G2_2_1_M = mode2_scene2_case1_3c2f()
        G2_3_1_M = mode2_scene3_case1_5c6f()
        G2_1_2_M = mode2_scene1_case2_2c1f()
        G2_2_2_M = mode2_scene2_case2_3c2f()
        G2_3_2_M = mode2_scene3_case2_5c6f()

        # G1_1_1_M.Priority = 2
        # G1_2_1_M.Priority = 1
        #
        # G1_1_2_M.Priority = 2
        # G1_2_2_M.Priority = 1
        #
        # G2_1_1_M.Priority = 3
        # G2_2_1_M.Priority = 2
        # G2_3_1_M.Priority = 1
        #
        # G2_1_2_M.Priority = 3
        # G2_2_2_M.Priority = 2
        # G2_3_2_M.Priority = 1

        for DAG_ID_x in DAG_Set_ID_list:
            if DAG_ID_x == "M1_S1_C1":
                self.Add_DAG(G1_1_1_M)
            elif DAG_ID_x == "M1_S2_C1":
                self.Add_DAG(G1_2_1_M)
            elif DAG_ID_x == "M1_S1_C2":
                self.Add_DAG(G1_1_2_M)
            elif DAG_ID_x == "M1_S2_C2":
                self.Add_DAG(G1_2_2_M)
            elif DAG_ID_x == "M2_S1_C1":
                self.Add_DAG(G2_1_1_M)
            elif DAG_ID_x == "M2_S2_C1":
                self.Add_DAG(G2_2_1_M)
            elif DAG_ID_x == "M2_S3_C1":
                self.Add_DAG(G2_3_1_M)
            elif DAG_ID_x == "M2_S1_C2":
                self.Add_DAG(G2_1_2_M)
            elif DAG_ID_x == "M2_S2_C2":
                self.Add_DAG(G2_2_2_M)
            elif DAG_ID_x == "M2_S3_C2":
                self.Add_DAG(G2_3_2_M)

        if algorithm_type == 'HUAWEI':
            pass
        elif algorithm_type == 'SELF':
            pass
            self.Mulit_DAG_Priority_Config()

    def user_defined_dag_self(self):
        self_DAG = self_make_DAG3()
        self.Add_DAG(self_DAG)
        # self.Random_DAG_Set_ET()


if __name__ == "__main__":
    dagset = DAG_Set()
    dagset.user_defined_dag()
    dagset.Show_DAG_Set()
    """
    # 字典排序
    a = {'a': 3, 'c': 89, 'b': 0, 'd': 34}
    # 按照字典的值进行排序
    a1 = sorted(a.items(), key=lambda x: x[1])
    # 按照字典的键进行排序
    a2 = sorted(a.items(), key=lambda x: x[0])
    print('按值排序后结果', a1)
    print('按键排序后结果', a2)
    print('结果转为字典格式', dict(a1))
    print('结果转为字典格式', dict(a2))
    # # 节点号； 节点名； 节点优权重； 节点优先级
    # plt.subplot()
    # p = Dispatcher()
    # p.user_defined_dag_1()
    # print(p.Mapping([3]))
    # p.Show_Dag()
    # plt.show()
    """


