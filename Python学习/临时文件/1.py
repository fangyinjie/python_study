"""
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
"""


#####################################
# todo Section_0: DAG Basic function
#####################################
# #### Gets the nodes in the ready state of the DAG #### #
# def get_ready_node_list(temp_DAG_list, run_list, ready_list):
#     temp_ready_list = [(ready_node_x[0], ready_node_x[1][0])for ready_node_x in ready_list]
#     ret_list = []
#     for temp_DAG_x in temp_DAG_list:
#         ret_list += [(temp_DAG_x.graph['DAG_ID'], x) for x in temp_DAG_x.nodes(data=True) if
#                      (len(list(temp_DAG_x.predecessors(x[0]))) == 0) and
#                      ((temp_DAG_x.graph['DAG_ID'], x[0]) not in run_list) and
#                      ((temp_DAG_x.graph['DAG_ID'], x[0]) not in temp_ready_list)]
#     return ret_list

