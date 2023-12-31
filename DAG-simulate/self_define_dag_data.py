import networkx as nx
import DAG
#####################################
#   自定义 DAG 数据
#   节点号； 节点名； 节点优权重； 节点优先级
#####################################

# 一.何庆强 2019 测试数据
# 1.1 测试数据1(简单数据)
def he_2019_DAG1():
    HE_2019_DAG = nx.DiGraph()
    HE_2019_nodes = [[1, 'V1', 1, 1],
                     [2, 'V2', 7, 5],
                     [3, 'V3', 3, 6],
                     [4, 'V4', 3, 7],
                     [5, 'V5', 6, 2],
                     [6, 'V6', 9, 3],
                     [7, 'V7', 2, 4],
                     [8, 'V8', 1, 8]]

    for node_x in HE_2019_nodes:
        HE_2019_DAG.add_node(node_x[0], Node_ID=node_x[1], critic=False, WCET=node_x[2], priority=node_x[3])

    HE_2019_edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (5, 7), (6, 7), (2, 8), (3, 8), (4, 8), (7, 8)]
    for edge_x in HE_2019_edges:
        HE_2019_DAG.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = HE_2019_DAG
    G.DAG_ID = "he_2019_DAG1"
    G.critical_path_config()
    return G


# 1.2 测试数据2(复杂数据)
def he_2019_DAG2():
    HE_2019_DAG = nx.DiGraph()
    HE_2019_nodes = [[1,  'V1',  15120, 0],
                     [2,  'V2',  14861, 2],
                     [3,  'V3',  14824, 5],
                     [4,  'V4',  8848,  1],
                     [5,  'V5',  8153,  3],
                     [6,  'V6',  8315,  7],
                     [7,  'V7',  4546,  4],
                     [8,  'V8',  5667,  6],
                     [9,  'V9',  3320,  8],
                     [10, 'V10', 24346, 9]]
    for node_x in HE_2019_nodes:
        HE_2019_DAG.add_node(
            node_x[0], Node_ID=node_x[1], rank=0, critic=False, WCET=node_x[2], priority=node_x[3])

    HE_2019_edges = [(1, 2), (2, 3), (2, 4), (2, 5), (3, 6), (3, 8),
             (4, 6), (4, 8), (4, 9), (5, 7), (5, 9), (6, 10), (7, 10), (8, 10), (9, 10) ]
    for edge_x in HE_2019_edges:
        HE_2019_DAG.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = HE_2019_DAG
    G.DAG_ID = "he_2019_DAG2"
    G.critical_path_config()
    return G


# 二.华为无线测试数据
# 2.1 模块1
# 2.1.1 情况1
# (1) 场景1——2核1流:
HuaWei_M1_S1_C1 = {
    'Job-29-1':    2,
    'Job-29-2':    2,
    'Job-36':      2,
    'Job-4-1':     2,
    'Job-35':      1,
    'Job-10':      1,
    'Job-4-2':     2,
    'Job-4-3':     2,
    'Job-4-4':     2,
    'Job-11':      1,
    'Job-4-5':     2,
    'Job-4-6':     2,
    'Job-12':      1,
    'Job-4-7':     2,
}


def mode1_scene1_case1_2c1f():
    Temp_Dag = nx.DiGraph()
    # [0] node_num; [1]node_ID; [2]AVET; [3]BCET; [4]WCET; [5]priority;
    node_list = [[1,  'Job-29-1', 569,       50,         1500,   1],
                 [2,  'Job-29-2', 13507,     10000,      23232,  13],
                 [3,  'Job-36',   14110,     6732,       30000,  12],
                 [4,  'Job-4-1',  36169,     29656,      45936,  2],
                 [5,  'Job-35',   3619,      572,        16772,  14],
                 [6,  'Job-10',   40229,     37752,      46548,  4],
                 [7,  'Job-4-2',  45409,     42724,      51348,  3],
                 [8,  'Job-4-3',  252370,    240724,     269720, 5],
                 [9,  'Job-4-4',  103897,    95612,      123376, 6],
                 [10, 'Job-11',   99335,     89976,      117972, 7],
                 [11, 'Job-4-5',  17699,     16676,      19316,  8],
                 [12, 'Job-4-6',  32609,     30008,      37048,  9],
                 [13, 'Job-12',  29889,      27672,      33424,  10],
                 [14, 'Job-4-7',   24250,    19712,      31812,  11] ]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')

    edge_list = [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6), (4, 7), (7, 8), (6, 8), (8, 9), (8, 10), (9, 11), (10, 11),
                 (11, 12), (11, 13), (13, 14), (12, 14)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M1_S1_C1"
    G.critical_path_config()
    return G


# (2) 场景2——3核2流:
HuaWei_M1_S2_C1 = {   'Job-29-1'   :  2,
                      'Job-29-2'   :  2,
                      'Job-36(1)'  :  2,
                      'Job-36(2)'  :  2,
                      'Job-4-1(1)' :  2,
                      'Job-4-1(2)' :  2,
                      'Job-35(1)'  :  1,
                      'Job-35(2)'  :  1,
                      'Job-10(1)' :   1,
                      'Job-10(2)' :   1,
                      'Job-10(3)' :   1,
                      'Job-10(4)' :   1,
                      'Job-4-2(1)' :  2,
                      'Job-4-2(2)' :  2,
                      'Job-4-3(1)' :  2,
                      'Job-4-3(2)' :  2,
                      'Job-4-4(1)' :  2,
                      'Job-4-4(2)' :  2,
                      'Job-11(1)' :   1,
                      'Job-11(2)' :   1,
                      'Job-11(3)' :   1,
                      'Job-11(4)' :   1,
                      'Job-4-5(1)' :  2,
                      'Job-4-5(2)' :  2,
                      'Job-4-6(1)' :  2,
                      'Job-4-6(2)' :  2,
                      'Job-12(1)' :   1,
                      'Job-12(2)' :   1,
                      'Job-12(3)' :   1,
                      'Job-12(4)' :   1,
                      'Job-4-7(1)' :  2,
                      'Job-4-7(2)' :  2}

def mode1_scene2_case1_3c2f():
    Temp_Dag = nx.DiGraph()
    # [0] node_num; [1]node_ID; [2]AVET; [3]BCET; [4]WCET; [5]priority;
    node_list = [[1, 'Job-29-1',     569,       50,        1500,     1],
                 [2, 'Job-29-2',     23226,     20000,     34276,    26],
                 [3, 'Job-36(1)',    13730,     5744,      32220,    29],
                 [4, 'Job-36(2)',    13730,     5744,      32220,    30],
                 [5, 'Job-4-1(1)',   34908,     29348,     40920,    2],
                 [6, 'Job-4-1(2)',   34908,     29348,     40920,    14],
                 [7, 'Job-35(1)',    5066,      624,       20000,    31],
                 [8, 'Job-35(2)',    5066,      624,       20000,    32],
                 [9, 'Job-10(1)',    26492,     23088,     36392,    4],
                 [10, 'Job-10(2)',   26492,     23088,     36392,    5],
                 [11, 'Job-10(3)',   26492,     23088,     36392,    16],
                 [12, 'Job-10(4)',   26492,     23088,     36392,    17],
                 [13, 'Job-4-2(1)',  76423,     56672,     36392,   3],
                 [14, 'Job-4-2(2)',  76423,     56672,     36392,   15],
                 [15, 'Job-4-3(1)',  275809,    255508,    292952,   6],
                 [16, 'Job-4-3(2)',  275809,    255508,    292952,   18],
                 [17, 'Job-4-4(1)',  144060,    129390,    90936,   7],
                 [18, 'Job-4-4(2)',  144060,    129390,    90936,   19],
                 [19, 'Job-11(1)',   67942,     55300,     90936,    8],
                 [20, 'Job-11(2)',   67942,     55300,     90936,    9],
                 [21, 'Job-11(3)',   67942,     55300,     90936,    20],
                 [22, 'Job-11(4)',   67942,     55300,     90936,    21],
                 [23, 'Job-4-5(1)',  18491,     17116,     22264,    10],
                 [24, 'Job-4-5(2)',  18491,     17116,     22264,    22],
                 [25, 'Job-4-6(1)',  94332,     24288,     32136,   11],
                 [26, 'Job-4-6(2)',  94332,     24288,     32136,   23],
                 [27, 'Job-12(1)',   18484,     11624,     32136,    12],
                 [28, 'Job-12(2)',   18484,     11624,     32136,    13],
                 [29, 'Job-12(3)',   18484,     11624,     32136,    24],
                 [30, 'Job-12(4)',   18484,     11624,     32136,    25],
                 [31, 'Job-4-7(1)',  24471,     8712,      34056,    27],
                 [32, 'Job-4-7(2)',  24471,     8712,      34056,    28]]

    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2],
                          BCET=node_x[3], WCET=node_x[4], priority=node_x[5], state='blocked')

    edge_list = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
                 (5, 9), (5, 10), (5, 13), (6, 11), (6, 12), (6, 14), (9, 15),
                 (10, 15), (13, 15), (11, 16), (12, 16), (14, 16), (15, 17), (15, 19), (15, 20),
                 (16, 18), (16, 21), (16, 22), (17, 23), (18, 24), (19, 23), (20, 23), (21, 24),
                 (22, 24), (23, 25), (23, 27), (23, 28), (24, 26), (24, 29),
                 (24, 30), (25, 31), (27, 31), (28, 31), (26, 32), (29, 32), (30, 32)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M1_S2_C1"
    G.critical_path_config()
    return G


# 2.1.2 情况2
# (1) 场景1——2核1流:
HuaWei_M1_S1_C2 = {
    'Job-29-1': 2,
    'Job-29-2': 2,
    'Job-36':   2,
    'Job-4':    2,
    'Job-35':   1
}
def mode1_scene1_case2_2c1f():
    Temp_Dag = nx.DiGraph()
    # [0] node_num; [1]node_ID; [2]AVET; [3]BCET; [4]WCET; [5]priority;
    node_list = [[1, 'Job-29-1',    569,       50,        1500,     1],
                 [2, 'Job-29-2',    13507,     10000,     23232,    4],
                 [3, 'Job-36',      14110,     6732,      30000,    3],
                 [4, 'Job-4',       8691,      1524,      36236,    2],
                 [5, 'Job-35',      3619,      572,       16772,    5]]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')

    edge_list = [(1, 2), (1, 3), (1, 4), (1, 5)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)

    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M1_S1_C2"
    G.critical_path_config()
    return G


# (2) 场景2——3核2流:
HuaWei_M1_S2_C2 = {
     'Job-29-1' :   2,
     'Job-29-2' :   2,
     'Job-36-1' :   2,
     'Job-36-2' :   2,
     'Job-35-1' :   1,
     'Job-35-2' :   1,
     'Job-4-1' :    2,
     'Job-4-2' :    2
    }

def mode1_scene2_case2_3c2f():
    Temp_Dag = nx.DiGraph()
    # [0] node_num; [1]node_ID; [2]AVET; [3]BCET; [4]WCET; [5]priority;
    node_list = [[1, 'Job-29-1', 569,     50,      1500,    1],
                 [2, 'Job-29-2', 23226,   20000,   34276,   4],
                 [3, 'Job-36-1', 13730,   5744,    32220,   5],
                 [4, 'Job-36-2', 13730,   5744,    32220,   6],
                 [5, 'Job-35-1', 5066,    624,     20000,   7],
                 [6, 'Job-35-2', 5066,    624,     20000,   8],
                 [7, 'Job-4-1',  8571,    1420,    39716,   2],
                 [8, 'Job-4-2',  8571,    1420,    39716,   3]]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')

    edge_list = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)

    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M1_S2_C2"
    G.critical_path_config()
    return G


# 2.2 模块2
# 2.2.1 情况1
# (1) 场景1——2核1流:
HuaWei_M2_S1_C1 = {
    'Job-0':     1,
    'Job-1':     2,
    'Job-3-1_1': 4,     #3,
    'Job-3-1_2': 4,     #3,
    'Job-3-1_3': 4,     #3,
    'Job-3-1_4': 4,     #2,
    'Job-3-2':   4,     #2,
    'Job-7_1':   4,     #2,
    'Job-7_2':   4,     #2,
    'Job-7_3':   4,     #2,
    'Job-7_4':   4,     #2,
    'Job-3-3':   4,}    #2}

def mode2_scene1_case1_2c1f():
    Temp_Dag = nx.DiGraph()

    node_list = [[1, 'Job-0',     1763,      992,    3032,   1],
                 [2, 'Job-1',     146511,    121660, 196196, 2],
                 [3, 'Job-3-1_1', 68690,     40120,  89624,  3],
                 [4, 'Job-3-1_2', 68690,     40120,  89624,  4],
                 [5, 'Job-3-1_3', 68690,     40120,  89624,  5],
                 [6, 'Job-3-1_4', 68690,     40120,  89624,  6],
                 [7, 'Job-3-2',   55264,     49192,  89056,  7],
                 [8, 'Job-7_1',   38724,     30108,  52492,  8],
                 [9, 'Job-7_2',   38724,     30108,  52492,  9],
                 [10, 'Job-7_3',  38724,     30108,  52492,  10],
                 [11, 'Job-7_4',  38724,     30108,  52492,  11],
                 [12, 'Job-3-3',  32440,     26532,  39996,  12]]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')

    edge_list = [(1, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 7), (4, 7), (5, 7), (6, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M2_S1_C1"
    G.critical_path_config()
    return G


# (2) 场景2——3核2流:
HuaWei_M2_S2_C1 = {
                 'Job-0' :          1,
                 'Job-1_1' :        2,
                 'Job-1_2' :        2,
                 'Job-3-1_1' :      3,
                 'Job-3-1_2' :      3,
                 'Job-3-1_3' :      3,
                 'Job-3-1_4' :      3,
                 'Job-3-1_5' :      3,
                 'Job-3-1_6' :      3,
                 'Job-3-1_7' :      3,
                 'Job-3-1_8' :      3,
                 'Job-3-2_1' :      3,
                 'Job-3-2_2' :      3,
                 'Job-7_1' :        3,
                 'Job-7_2' :        3,
                 'Job-7_3' :        3,
                 'Job-7_4' :        3,
                 'Job-7_5' :        3,
                 'Job-7_6' :        3,
                 'Job-7_7' :        3,
                 'Job-7_8' :        3,
                 'Job-3-3_1' :      3,
                 'Job-3-3_2' :      3}
def mode2_scene2_case1_3c2f():
    Temp_Dag = nx.DiGraph()
    node_list = [[1, 'Job-0',        2953,   1564,    6732,   1],
                 [2, 'Job-1_1',      162563, 130724,  264088, 2],
                 [3, 'Job-1_2',      162563, 130724,  264088, 8],
                 [4, 'Job-3-1_1',    89405,  51794,   118764, 3],
                 [5, 'Job-3-1_2',    89405,  51794,   118764, 4],
                 [6, 'Job-3-1_3',    89405,  51794,   118764, 5],
                 [7, 'Job-3-1_4',    89405,  51794,   118764, 6],
                 [8, 'Job-3-1_5',    89405,  51794,   118764, 9],
                 [9, 'Job-3-1_6',    89405,  51794,   118764, 10],
                 [10, 'Job-3-1_7',   89405,  51794,   118764, 11],
                 [11, 'Job-3-1_8',   89405,  51794,   118764, 12],
                 [12, 'Job-3-2_1',   61897,  50512,   97020,  7],
                 [13, 'Job-3-2_2',   61897,  50512,   97020,  13],
                 [14, 'Job-7_1',     44442,  28984,   75460,  14],
                 [15, 'Job-7_2',     44442,  28984,   75460,  15],
                 [16, 'Job-7_3',     44442,  28984,   75460,  15],
                 [17, 'Job-7_4',     44442,  28984,   75460,  17],
                 [18, 'Job-7_5',     44442,  28984,   75460,  18],
                 [19, 'Job-7_6',     44442,  28984,   75460,  19],
                 [20, 'Job-7_7',     44442,  28984,   75460,  20],
                 [21, 'Job-7_8',     44442,  28984,   75460,  21],
                 [22, 'Job-3-3_1',   40574,  28864,   55264,  22],
                 [23, 'Job-3-3_2',   40574,  28864,   55264,  23]]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')
    edge_list = [(1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 8), (3, 9), (3, 10), (3, 11), (4, 12), (5, 12),
                 (6, 12), (7, 12), (8, 13), (9, 13), (10, 13), (11, 13), (12, 14), (12, 15), (12, 16), (12, 17),
                 (12, 22), (13, 18), (13, 19), (13, 20), (13, 21), (13, 23)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M2_S2_C1"
    G.critical_path_config()
    return G


# (3) 场景3——5核6流:
HuaWei_M2_S3_C1 = {
    'Job-0':      1,
    'Job-1_1':    2,
    'Job-3-1_1':  3,
    'Job-3-1_2':  3,
    'Job-3-1_3':  3,
    'Job-3-1_4':  3,
    'Job-3-2_1':  3,
    'Job-1_2':    2,
    'Job-1_3':    2,
    'Job-1_4':    2,
    'Job-1_5':    2,
    'Job-1_6':    2,
    'Job-3-1_5':  3,
    'Job-3-1_6':  3,
    'Job-3-1_7':  3,
    'Job-3-1_8':  3,
    'Job-3-1_9':  3,
    'Job-3-1_10': 3,
    'Job-3-1_11': 3,
    'Job-3-1_12': 3,
    'Job-3-1_13': 3,
    'Job-3-1_14': 3,
    'Job-3-1_15': 3,
    'Job-3-1_16': 3,
    'Job-3-1_17': 3,
    'Job-3-1_18': 3,
    'Job-3-1_19': 3,
    'Job-3-1_20': 3,
    'Job-3-1_21': 3,
    'Job-3-1_22': 3,
    'Job-3-1_23': 3,
    'Job-3-1_24': 3,
    'Job-3-2_2':  3,
    'Job-3-2_3':  3,
    'Job-3-2_4':  3,
    'Job-3_2_5':  3,
    'Job-3_2_6':  3,
    'Job 7_1':    3,
    'Job 7_2':    3,
    'Job 7_3':    3,
    'Job 7_4':    3,
    'Job 7_5':    3,
    'Job 7_6':    3,
    'Job 7_7':    3,
    'Job 7_8':    3,
    'Job 7_9':    3,
    'Job 7_10':   3,
    'Job 7_11':   3,
    'Job 7_12':   3,
    'Job 7_13':   3,
    'Job 7_14':   3,
    'Job 7_15':   3,
    'Job 7_16':   3,
    'Job 7_17':   3,
    'Job 7_18':   3,
    'Job 7_19':   3,
    'Job 7_20':   3,
    'Job 7_21':   3,
    'Job 7_22':   3,
    'Job 7_23':   3,
    'Job 7_24':   3,
    'Job 3-3_1':  3,
    'Job 3-3_2':  3,
    'Job 3-3_3':  3,
    'Job 3-3_4':  3,
    'Job 3-3_5':  3,
    'Job 3-3_6':  3}

def mode2_scene3_case1_5c6f():
    Temp_Dag = nx.DiGraph()
    node_list = [[1, 'Job-0',       6809,   4684,   10000,  1],
                 [2, 'Job-1_1',     174703, 129052, 290488, 2],
                 [3, 'Job-3-1_1',   76687,  44784,  100000, 3],
                 [4, 'Job-3-1_2',   76687,  44784,  100000, 4],
                 [5, 'Job-3-1_3',   76687,  44784,  100000, 5],
                 [6, 'Job-3-1_4',   76687,  44784,  100000, 6],
                 [7, 'Job-3-2_1',   57472,  43604,  96008,  7],
                 [8, 'Job-1_2',     174703, 129052, 290488, 8],
                 [9, 'Job-1_3',     174703, 129052, 290488, 9],
                 [10, 'Job-1_4',    174703, 129052, 290488, 10],
                 [11, 'Job-1_5',    174703, 129052, 290488, 11],
                 [12, 'Job-1_6',    174703, 129052, 290488, 12],
                 [13, 'Job-3-1_5',  76687,  44784,  100000, 13],
                 [14, 'Job-3-1_6',  76687,  44784,  100000, 14],
                 [15, 'Job-3-1_7',  76687,  44784,  100000, 15],
                 [16, 'Job-3-1_8',  76687,  44784,  100000, 16],
                 [17, 'Job-3-1_9',  76687,  44784,  100000, 17],
                 [18, 'Job-3-1_10', 76687,  44784,  100000, 18],
                 [19, 'Job-3-1_11', 76687,  44784,  100000, 19],
                 [20, 'Job-3-1_12', 76687,  44784,  100000, 20],
                 [21, 'Job-3-1_13', 76687,  44784,  100000, 21],
                 [22, 'Job-3-1_14', 76687,  44784,  100000, 22],
                 [23, 'Job-3-1_15', 76687,  44784,  100000, 23],
                 [24, 'Job-3-1_16', 76687,  44784,  100000, 24],
                 [25, 'Job-3-1_17', 76687,  44784,  100000, 25],
                 [26, 'Job-3-1_18', 76687,  44784,  100000, 26],
                 [27, 'Job-3-1_19', 76687,  44784,  100000, 27],
                 [28, 'Job-3-1_20', 76687,  44784,  100000, 28],
                 [29, 'Job-3-1_21', 76687,  44784,  100000, 29],
                 [30, 'Job-3-1_22', 76687,  44784,  100000, 30],
                 [31, 'Job-3-1_23', 76687,  44784,  100000, 31],
                 [32, 'Job-3-1_24', 76687,  44784,  100000, 32],
                 [33, 'Job-3-2_2',  57472,  43604,  96008,  33],
                 [34, 'Job-3-2_3',  57472,  43604,  96008,  34],
                 [35, 'Job-3-2_4',  57472,  43604,  96008,  35],
                 [36, 'Job-3_2_5',  57472,  43604,  96008,  36],
                 [37, 'Job-3_2_6',  57472,  43604,  96008,  37],
                 [38, 'Job 7_1',    52837,  34084,  87560,  38],
                 [39, 'Job 7_2',    52837,  34084,  87560,  39],
                 [40, 'Job 7_3',    52837,  34084,  87560,  40],
                 [41, 'Job 7_4',    52837,  34084,  87560,  41],
                 [42, 'Job 7_5',    52837,  34084,  87560,  42],
                 [43, 'Job 7_6',    52837,  34084,  87560,  43],
                 [44, 'Job 7_7',    52837,  34084,  87560,  44],
                 [45, 'Job 7_8',    52837,  34084,  87560,  45],
                 [46, 'Job 7_9',    52837,  34084,  87560,  46],
                 [47, 'Job 7_10',   52837,  34084,  87560,  47],
                 [48, 'Job 7_11',   52837,  34084,  87560,  48],
                 [49, 'Job 7_12',   52837,  34084,  87560,  49],
                 [50, 'Job 7_13',   52837,  34084,  87560,  50],
                 [51, 'Job 7_14',   52837,  34084,  87560,  51],
                 [52, 'Job 7_15',   52837,  34084,  87560,  52],
                 [53, 'Job 7_16',   52837,  34084,  87560,  53],
                 [54, 'Job 7_17',   52837,  34084,  87560,  54],
                 [55, 'Job 7_18',   52837,  34084,  87560,  55],
                 [56, 'Job 7_19',   52837,  34084,  87560,  56],
                 [57, 'Job 7_20',   52837,  34084,  87560,  57],
                 [58, 'Job 7_21',   52837,  34084,  87560,  58],
                 [59, 'Job 7_22',   52837,  34084,  87560,  59],
                 [60, 'Job 7_23',   52837,  34084,  87560,  60],
                 [61, 'Job 7_24',   52837,  34084,  87560,  61],
                 [62, 'Job 3-3_1',  37903,  28336,  57332,  62],
                 [63, 'Job 3-3_2',  37903,  28336,  57332,  63],
                 [64, 'Job 3-3_3',  37903,  28336,  57332,  64],
                 [65, 'Job 3-3_4',  37903,  28336,  57332,  65],
                 [66, 'Job 3-3_5',  37903,  28336,  57332,  66],
                 [67, 'Job 3-3_6',  37903,  28336,  57332,  67]
                 ]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')

    edge_list = [(1, 2), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12),
                 (2, 3), (2, 4), (2, 5), (2, 6),
                 (8, 13), (8, 14), (8, 15), (8, 16),
                 (9, 17), (9, 18), (9, 19), (9, 20),
                 (10, 21), (10, 22), (10, 23), (10, 24),
                 (11, 25), (11, 26), (11, 27), (11, 28),
                 (12, 29), (12, 30), (12, 31), (12, 32),

                 (3, 7), (4, 7), (5, 7), (6, 7),
                 (13, 33), (14, 33), (15, 33), (16, 33),
                 (17, 34), (18, 34), (19, 34), (20, 34),
                 (21, 35), (22, 35), (23, 35), (24, 35),
                 (25, 36), (26, 36), (27, 36), (28, 36),
                 (29, 37), (30, 37), (31, 37), (32, 37),

                 (7, 38), (7, 39), (7, 40), (7, 41), (7, 62),
                 (33, 42), (33, 43), (33, 44), (33, 45), (33, 63),
                 (34, 46), (34, 47), (34, 48), (34, 49), (34, 64),
                 (35, 50), (35, 51), (35, 52), (35, 53), (35, 65),
                 (36, 54), (36, 55), (36, 56), (36, 57), (36, 66),
                 (37, 58), (37, 59), (37, 60), (37, 61), (37, 67)
                 ]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M2_S3_C1"
    G.critical_path_config()
    return G


# 2.2.2 情况2
# (1) 场景1——2核1流:
HuaWei_M2_S1_C2 = { 'Job-0':     1,
                    'Job-3-1':   3}
def mode2_scene1_case2_2c1f():
    Temp_Dag = nx.DiGraph()
    node_list = [[1, 'Job-0',    1763,    992,  3032, 1],
                 [2, 'Job-3-1',  67308, 76583, 89840, 2] ]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')
    edge_list = [(1, 2)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M2_S1_C2"
    G.critical_path_config()
    return G


# (2) 场景2——3核2流:
HuaWei_M2_S2_C2 = { 'Job-0':  1,
                    'Job-1_1':  2,
                    'Job-1_2':  2 }

def mode2_scene2_case2_3c2f():
    Temp_Dag = nx.DiGraph()
    node_list = [[1, 'Job-0',   2953,  1564,  6732,   1],
                 [2, 'Job-1_1', 93574, 78868, 108328, 2],
                 [3, 'Job-1_2', 93574, 78868, 108328, 3]]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')
    edge_list = [(1, 2), (1, 3)]
    for edge_x in edge_list:
        Temp_Dag.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M2_S2_C2"
    G.critical_path_config()
    return G


# (3) 场景3——5核6流:
HuaWei_M2_S3_C2 = {'Job-0':     1,
                   'Job-1_1':   2,
                   'Job-1_2':   2,
                   'Job-1_3':   2,
                   'Job-1_4':   2,
                   'Job-1_5':   2,
                   'Job-1_6':   2}

def mode2_scene3_case2_5c6f():
    Temp_Dag = nx.DiGraph()
    node_list = [[1, 'Job-0',   6809,   4684,  10000,  1],
                 [2, 'Job-1_1', 106631, 73452, 120000, 2],
                 [3, 'Job-1_2', 106631, 73452, 120000, 3],
                 [4, 'Job-1_3', 106631, 73452, 120000, 4],
                 [5, 'Job-1_4', 106631, 73452, 120000, 5],
                 [6, 'Job-1_5', 106631, 73452, 120000, 6],
                 [7, 'Job-1_6', 106631, 73452, 120000, 7]]
    for node_x in node_list:
        Temp_Dag.add_node(node_x[0], Node_ID=node_x[1], critic=False, AVET=node_x[2], BCET=node_x[3], WCET=node_x[4],
                          priority=node_x[5], state='blocked')

    edges = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)]
    for edge in edges:
        Temp_Dag.add_edge(edge[0], edge[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag
    G.DAG_ID = "M2_S3_C2"
    G.critical_path_config()
    return G


# 三.自制的
def self_make_DAG1():
    Temp_Dag_mine = nx.DiGraph()
    node_list = [[1, 'Job-1', 9,  1],
                 [2, 'Job-2', 10, 2],
                 [3, 'Job-3', 4,  5],
                 [4, 'Job-4', 8,  4],
                 [5, 'Job-5', 11, 3],
                 [6, 'Job-6', 6,  6],
                 [7, 'Job-7', 5,  7]]
    for node_x in node_list:
        Temp_Dag_mine.add_node(node_x[0], Node_ID=node_x[1], rank=0, critic=False, WCET=node_x[2], priority=node_x[3], state='blocked')
    edge_list = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (5, 6), (6, 7), (4, 7)]
    for edge_x in edge_list:
        Temp_Dag_mine.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag_mine
    G.DAG_ID = "Self_DAG_1"
    G.critical_path_config()
    return G


def self_make_DAG2():
    Temp_Dag_mine = nx.DiGraph()
    node_list = [[1, 'Job-1', 9,  1],
                 [2, 'Job-2', 10, 2],
                 [3, 'Job-3', 4,  3],
                 [4, 'Job-4', 8,  6],
                 [5, 'Job-5', 11, 4],
                 [6, 'Job-6', 6,  5],
                 [7, 'Job-7', 5,  7]]
    for node_x in node_list:
        Temp_Dag_mine.add_node(node_x[0], Node_ID=node_x[1], rank=0, critic=False, WCET=node_x[2], priority=node_x[3], state='blocked')
    edge_list = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (5, 6), (6, 7), (4, 7)]
    for edge_x in edge_list:
        Temp_Dag_mine.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag_mine
    G.DAG_ID = "Self_DAG_2"
    G.critical_path_config()
    return G

def self_make_DAG3():
    Temp_Dag_mine = nx.DiGraph()
    node_list = [[1, 'Job-1', 32,  32,  32,   7],
                 [2, 'Job-2', 42,  42,  42,   5],
                 [3, 'Job-3', 128, 128, 128,  1],
                 [4, 'Job-4', 74,  74,  74,   3],
                 [5, 'Job-5', 34,  34,  34,   6],
                 [6, 'Job-6', 90,  90,  90,   2],
                 [7, 'Job-7', 47,  47,  47,   4],
                 [8, 'Job-8', 553, 553, 553,  0]
                 ]

    for node_x in node_list:
        Temp_Dag_mine.add_node(node_x[0], Node_ID=node_x[1], rank=0, critic=False, WCET=node_x[2], priority=node_x[3],
                               state='blocked', ET=node_x[2])

    edge_list = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 7), (4, 7), (5, 6), (6, 8), (7, 8)]
    for edge_x in edge_list:
        Temp_Dag_mine.add_edge(edge_x[0], edge_x[1], weight=1)
    G = DAG.DAG()
    G.G = Temp_Dag_mine
    G.DAG_ID = "Self_DAG_3"
    G.critical_path_config()
    return G
