import networkx as nx
import pygraphviz as pgv
import matplotlib.pyplot as ppt

edgelist = [(1,2),(1,9),(3,2),(3,9),(4,5),(4,6),(4,9),(5,9),(7,8),(7,9)]

nxd = nx.DiGraph()
nxu = nx.Graph()
gvd = pgv.AGraph(directed=True, rankdir="LR")
gvu = pgv.AGraph()

nxd.add_edges_from(edgelist)
nxu.add_edges_from(edgelist)

gvd.add_node(1, label=12)
gvd.add_node(2, wcet=12)
gvd.add_node(3, wcet=12)
gvd.add_node(4, wcet=12)
gvd.add_node(5, wcet=12)
gvd.add_node(6, wcet=12)
gvd.add_node(7, wcet=12)
gvd.add_node(8, wcet=12)
gvd.add_node(9, wcet=12)
# gvd.add_node(10, '23')

gvd.add_edges_from(edgelist)
gvu.add_edges_from(edgelist)

# pos1 = nx.spring_layout(nxd)
# nx.draw_networkx(nxd, pos1)
# ppt.show()
    # savefig('1_networkx_directed.png')
# ppt.clf()

pos2 = nx.spring_layout(nxu)
nx.draw_networkx(nxu, pos2)
ppt.savefig('2_networkx_undirected.png')
ppt.clf()

# prog = ['neato' | 'dot' | 'twopi' | 'circo' | 'fdp' | 'nop']
gvd.layout(prog='dot')
gvd.draw('3_pygraphviz_directed.png')

gvu.layout(prog='dot')
gvu.draw('4_pygraphviz_undirected.png')

# for DAG_x in DAG_list:
#     # dot = gz.Digraph()
#     gvd = pgv.AGraph(directed=True)
#     for node_x in DAG_x.nodes(data=True):
#         temp_label = ''
#         temp_label += str(node_x[0]) + '\n'
#         temp_label += 'Node_ID:' + str(node_x[1]['Node_ID']) + '\n'
#         temp_label += 'WCET:' + str(node_x[1]['WCET']) + '\n'
#         temp_label += 'Prio:' + str(node_x[1]['Prio']) + '\n'
#         gvd.add_node(node_x[0], label=temp_label)
#         # dot.node('%s' % node_x[0], temp_label)
#     for edge_x in DAG_x.edges(data=True):
#         gvd.add_edge(edge_x[0], edge_x[1])
#         # dot.edge(str(edge_x[0]), str(edge_x[1]))
#     if not os.path.exists(output_path):
#         os.makedirs(output_path)