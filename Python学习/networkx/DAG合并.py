import networkx as nx

# 创建两个互相独立的图形
U = nx.Graph()
G1 = nx.Graph()
G1.add_node(0, id=0, DI=1)
G1.add_node(1, id=1, DI=1)
G1.add_node(2, id=2, DI=1)
G1.add_edges_from([(0, 1), (1, 2)])

G2 = nx.Graph()
G2.add_node(0, id=0, DI=2)
G2.add_node(1, id=1, DI=2)
G2.add_node(2, id=2, DI=2)
G2.add_edges_from([(0, 1), (1, 2)])

G3 = nx.Graph()
G3.add_node(0, id=0, DI=3)
G3.add_node(1, id=1, DI=3)
G3.add_node(2, id=2, DI=3)
G3.add_edges_from([(0, 1), (1, 2)])


G4 = nx.Graph()
G4.add_node(0, id=0, DI=4)
G4.add_node(1, id=1, DI=4)
G4.add_node(2, id=2, DI=4)
G4.add_edges_from([(0, 1), (1, 2)])

G5 = nx.Graph()
G5.add_node(0, id=0, DI=5)
G5.add_node(1, id=1, DI=5)
G5.add_node(2, id=2, DI=5)
G5.add_edges_from([(0, 1), (1, 2)])
# 将两个图形结合到一起
U = nx.disjoint_union(U, G1)
U = nx.disjoint_union(U, G2)
U = nx.disjoint_union(U, G3)
U = nx.disjoint_union(U, G4)
U = nx.disjoint_union(U, G5)

# 打印输出结果
for node_x in U.nodes(data=True):
    print(node_x)           # 输出 [0, 1, 2, 3, 4, 5]
print(U.edges())            # 输出 [(0, 1), (1, 2), (3, 4), (4, 5)]