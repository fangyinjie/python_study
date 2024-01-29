import networkx as nx  # 导入 NetworkX 工具包

# 创建 图
G1 = nx.Graph()         # 创建：空的 无向图
G2 = nx.DiGraph()       # 创建：空的 有向图
G3 = nx.MultiGraph()    # 创建：空的 多图
G4 = nx.MultiDiGraph()  # 创建：空的 有向多图

# 顶点(node)的操作
G1.add_node(1, name='n1', weight=1.0)  # 添加顶点 1，定义 name, weight 属性
# G1.add_nodes_from([3, 0, 6], dist=1)  # 添加多个顶点：3，0，6
print(G1.nodes())  # 查看顶点和顶点属性  # [1, 2, 3, 0, 6]
# {1: {'name': 'n1', 'weight': 1.0}, 2: {'date': 'May-16'}, 3: {'dist': 1}, 0: {'dist': 1}, 6: {'dist': 1}}
G1.add_nodes_from(range(10, 15))  # 向图 G1 添加顶点 10～14
print(G1.nodes())  # 查看顶点
# G1.remove_nodes_from([1, 11, 13, 14])  # 通过顶点标签的 list 删除多个顶点 # 从图中删除顶点

