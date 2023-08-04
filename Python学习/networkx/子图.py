import networkx as nx

# 创建一个空的无向图
G = nx.Graph()

# 添加节点
G.add_nodes_from([(1, {'node_id': 1}),
                  (2, {'node_id': 2}),
                  (3, {'node_id': 3}),
                  (4, {'node_id': 4}) ])

# 添加边
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

sub_G = G.subgraph([2, 3, 4])
print(sub_G.nodes[2])
sub_G.nodes[2]['node_id']  = 3
print(sub_G.nodes[2])
# 打印图形信息
print("原始图形的节点：", sub_G.nodes(data=True))
print("原始图形的边：", sub_G.edges())
sub_G.nodes_number