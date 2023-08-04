# pyinstaller -F -w .\Python学习\exe文件qt\main.py

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from PyQt5.QtWidgets import ( QApplication, QWidget, QLabel, QPushButton, QSlider,
                              QFormLayout, QMessageBox, QComboBox, QLineEdit, QCheckBox,
                              QDesktopWidget, QHBoxLayout, QFileDialog, QDialog)
import pandas as pd
import networkx as nx
import xlwt
# import graphviz as gz
import pygraphviz as pgv
import os
# import DAG

# import sys  # 系统参数操作
# from PyQt5.QtWidgets import *  # 模块包含创造经典桌面风格的用户界面提供了一套UI元素的类
# from PyQt5.QtCore import *  # 此模块用于处理时间、文件和目录、各种数据类型、流、URL、MIME类型、线程或进程
# from PyQt5.QtGui import *  # 含类窗口系统集成、事件处理、二维图形、基本成像、字体和文本

#
# class LoginDialog(QDialog):
#     def __init__(self, *args, **kwargs):
#         '''
#         构造函数，初始化登录对话框的内容
#         :param args:
#         :param kwargs:
#         '''
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle('欢迎登录')  # 设置标题
#         self.resize(150, 160)  # 设置宽、高
#         self.setFixedSize(self.width(), self.height())
#         self.setWindowFlags(Qt.WindowCloseButtonHint)  # 设置隐藏关闭X的按钮
#
#         '''
#         定义界面控件设置
#         '''
#         self.frame = QFrame(self)  # 初始化 Frame对象
#         self.verticalLayout = QVBoxLayout(self.frame)  # 设置横向布局
#         # self.verticalLayout
#
#         self.login_id = QLineEdit()  # 定义用户名输入框
#         self.login_id.setPlaceholderText("请输入登录账号")  # 设置默认显示的提示语
#         self.verticalLayout.addWidget(self.login_id)  # 将该登录账户设置添加到页面控件
#
#         self.passwd = QLineEdit()  # 定义密码输入框
#         self.passwd.setPlaceholderText("请输入登录密码")  # 设置默认显示的提示语
#         self.verticalLayout.addWidget(self.passwd)  # 将该登录密码设置添加到页面控件
#
#         self.button_enter = QPushButton()  # 定义登录按钮
#         self.button_enter.setText("登录")  # 按钮显示值为登录
#         self.verticalLayout.addWidget(self.button_enter)  # 将按钮添加到页面控件
#
#         self.button_quit = QPushButton()  # 定义返回按钮
#         self.button_quit.setText("退出")  # 按钮显示值为返回
#         self.verticalLayout.addWidget(self.button_quit)  # 将按钮添加到页面控件
#
#         # 绑定按钮事件
#         self.button_enter.clicked.connect(self.button_enter_verify)
#         self.button_quit.clicked.connect( QCoreApplication.instance().quit)  # 返回按钮绑定到退出
#
#     def button_enter_verify(self):
#         # 校验账号是否正确
#         if self.login_id.text() != "admin":
#             print("test1")
#             return
#         # 校验密码是否正确
#         if self.passwd.text() != "admin@1234":
#             print("test2")
#             return
#         # 验证通过，设置QDialog对象状态为允许
#         self.accept()


class GUI:
    def __init__(self):
        self.app = QApplication(sys.argv)  # 1.1 获取命令行参数
        # ######### 操作区 ########
        """     create layout      """
        self.formLayout = QFormLayout()
        # 1. 标题
        self.label = QLabel("DAG Critical Features Abstract")
        self.formLayout.addRow(self.label)

        # 2. 建立清单文本
        # parameter_1-DAG的并行度
        self.edit_parallism_input_path = QLineEdit()
        self.button_input_file = QPushButton('input file address')
        self.button_input_file.clicked.connect(self.Input_Data_Inject)
        hlayout_first = QHBoxLayout()  # 水平
        hlayout_first.addWidget(self.edit_parallism_input_path)
        hlayout_first.addWidget(self.button_input_file)
        self.formLayout.addRow("输入Excel文件路径:", hlayout_first)

        self.edit_parallism_output_path = QLineEdit()
        self.button_output_file = QPushButton('output file address')
        self.button_output_file.clicked.connect(self.Output_Data_Path)
        hlayout_second = QHBoxLayout()  # 水平
        hlayout_second.addWidget(self.edit_parallism_output_path)
        hlayout_second.addWidget(self.button_output_file)
        self.formLayout.addRow("输出数据文件夹路径:", hlayout_second)

        self.button_gen = QPushButton('Generate DAGs Critical Features Data')
        self.formLayout.addRow(self.button_gen)
        self.button_gen.clicked.connect(self.Data_transition)

        # create window
        self.window = QWidget()
        self.window.resize(600, 130)  # 2.1 设置窗口的尺寸 # 宽，高
        center_pointer = QDesktopWidget().availableGeometry().center()  # 3.1 获取屏幕中央坐标,调整窗口在屏幕中央显示
        self.window.move(center_pointer.x(), center_pointer.y())        # 3.2 移动到中央(窗口左上角坐标)
        # print (window. frameGeometry())                               # 3.3 获取窗口坐标
        self.window.setWindowTitle('DAG Critical Features Abstract')
        self.window.setLayout(self.formLayout)
        self.window.show()
        self.app.exec_()

    def Input_Data_Inject(self):
        download_path = QFileDialog.getOpenFileName(None)
        self.edit_parallism_input_path.setText(download_path[0])
        print( download_path )

    def Output_Data_Path(self):
        download_path = QFileDialog.getExistingDirectory(None)
        self.edit_parallism_output_path.setText(download_path)
        print( download_path )

    # E:\房银杰个人文件\读博文件\项目文件\华为项目\2021-10华为无线\Tianjiqing_java_code\123\HUAWEI_output.xlsx
    # E:\房银杰个人文件\读博文件\项目文件\华为项目\2021-10华为无线\Tianjiqing_java_code\123\HUAWEI_input.xlsx
    # todo 利用excel表格数据生成DAG
    def Data_transition(self):
        print("Hello World")
        output_path = self.edit_parallism_output_path.text()
        input_path = self.edit_parallism_input_path.text()

        if (output_path == '') or (not os.path.exists(input_path)) or (".xls" not in input_path) or (".xlsx" not in input_path):
            QMessageBox.critical(self.window,  '错误',  "输入文件不存在", QMessageBox.Cancel | QMessageBox.Close, QMessageBox.Cancel)
            return False

        if (output_path == '') or (not os.path.exists(input_path)) or (input_path == output_path):
            QMessageBox.critical(self.window, '错误', "输出文件格式不正确", QMessageBox.Cancel | QMessageBox.Close, QMessageBox.Cancel)
            return False

        DAG_list = []
        # todo 1.录入DAG数据
        with pd.ExcelFile(input_path) as data:
            all_sheet_names = data.sheet_names  # 获取所有sheet名字；
            for DAG_ID in all_sheet_names:
                temp_DAG = nx.DiGraph()
                temp_DAG.graph['DAG_ID'] = DAG_ID
                df = pd.read_excel(data, DAG_ID, index_col=None, na_values=["NA"])
                # title_list = df.dtypes
                temp_node_index = 0
                self_node_dict = {}
                for row in df.index:
                    node_list_ID = df.loc[row]['JobTypeID']
                    if node_list_ID != node_list_ID:
                        continue
                    else:
                        node_list_ID = int(node_list_ID)
                    node_temp_num = int(df.loc[row]['InstanceNumber'])
                    node_precursor_list = df.loc[row]['TriggerJobTypeIDSet']
                    if node_precursor_list != node_precursor_list:
                        node_precursor_list = []
                    elif type(node_precursor_list) == str:
                        node_precursor_list = node_precursor_list.split(',')
                    else:
                        node_precursor_list = [node_precursor_list]
                    node_execution_time = df.loc[row]['ExecutionTime']
                    node_priority = int(df.loc[row]['QoS'])
                    self_node_dict[node_list_ID] = []
                    for x in range(node_temp_num):
                        temp_node_index += 1
                        node_temp_id = 'Job_' + str(node_list_ID) + '_' + str(x+1)
                        temp_DAG.add_node(temp_node_index, Node_Index=temp_node_index, Node_ID=node_temp_id, WCET=node_execution_time, Prio=node_priority)
                        self_node_dict[node_list_ID] .append(temp_node_index)
                        for node_precursor in node_precursor_list:
                            for u in self_node_dict[int(node_precursor)]:
                                temp_DAG.add_edge(u, temp_node_index)
                DAG_list.append(temp_DAG)
        # QMessageBox.question(self.window, "123", "123！", QMessageBox.Yes)
        # with pd.ExcelFile(input_path) as data:
        #     all_sheet_names = data.sheet_names  # 获取所有sheet名字；
        #     for DAG_ID in all_sheet_names:
        #         temp_DAG = nx.DiGraph()
        #         temp_DAG.graph['DAG_ID'] = DAG_ID
        #         df = pd.read_excel(data, DAG_ID, index_col=None, na_values=["NA"])
        #         title_list = df.dtypes
        #         for row in df.index:
        #             t_self_node = df.loc[row]['Node_Index']
        #             # temp_DAG.add_node(df.loc[row]['Node_Index'])
        #             temp_DAG.add_node(t_self_node)
        #             for title_id, data_type in title_list.items():
        #                 row_data = df.loc[row][title_id]
        #                 if title_id == 'Edges_List':
        #                     if type(row_data) == float:
        #                         continue
        #                     row_data = row_data.split(',')
        #                     for edge_data in row_data:
        #                         if edge_data == '':
        #                             continue
        #                         # edge_list = edge_data[1:-1].split(',')
        #                         # temp_DAG.add_edge(int(edge_list[0]), int(edge_list[1]))
        #                         temp_DAG.add_edge(t_self_node, int(edge_data))
        #                 else:
        #                     temp_DAG.node[df.loc[row]['Node_Index']][title_id] = row_data
        #         DAG_list.append(temp_DAG)
        # todo 2 生成DAG图
        # for DAG_x in DAG_list:
        #     dot = gz.Digraph()
        #     for node_x in DAG_x.nodes(data=True):
        #         temp_label = ''
        #         temp_label += 'Node_ID:' + str(node_x[1]['Node_ID']) + '\n'
        #         temp_label += 'WCET:' + str(node_x[1]['WCET']) + '\n'
        #         temp_label += 'Prio:' + str(node_x[1]['Prio']) + '\n'
        #         dot.node('%s' % node_x[0], temp_label)
        #     for edge_x in DAG_x.edges(data=True):
        #         dot.edge(str(edge_x[0]), str(edge_x[1]))
        for DAG_x in DAG_list:
            gvd = pgv.AGraph(directed=True, rankdir="LR")
            for node_x in DAG_x.nodes(data=True):
                temp_label = ''
                temp_label += str(node_x[0]) + '\n'
                temp_label += 'Node_ID:' + str(node_x[1]['Node_ID']) + '\n'
                temp_label += 'WCET:' + str(node_x[1]['WCET']) + '\n'
                temp_label += 'Prio:' + str(node_x[1]['Prio']) + '\n'
                gvd.add_node(node_x[0], label=temp_label)
                # dot.node('%s' % node_x[0], temp_label)
            for edge_x in DAG_x.edges(data=True):
                gvd.add_edge(edge_x[0], edge_x[1])

            gvd.layout(prog='dot')          # 要有，否则会出现log文件
            gvd.draw(path=output_path + '/' + DAG_x.graph['DAG_ID'] + '.png', format='png')

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # dot.save('{0}/{1}.png'.format(grapg_path, DAG_x.graph['DAG_ID']))
            # dot.render(view=False, directory=output_path, format="png", filename=DAG_x.graph['DAG_ID'])
            # graph.render(view=True, format="pdf", filename="decisiontree_pdf")
        # QMessageBox.question(self.window, "234", "234！", QMessageBox.Yes)
        # todo 3.抽象DAG特性
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet("DAG_Critical_Features")
        Features_Tytle = ["DAG_ID", "Number_Of_Nodes",  "Number_Of_Edges",  "Number_Of_Level",
                          # "Shape_List",
                          "Max_Shape",    "Min_Shape",    "Ave_Shape", "Std_Shape",
                          # "Re_Shape_List",
                          "Max_Re_Shape", "Min_Re_Shape", "Ave_Re_Shape", "Std_Re_Shape",
                          "Width", "Max_Degree", "Min_Degree", "Ave_Degree", "Std_Degree",
                          "Max_In_Degree", "Min_In_Degree", "Ave_In_Degree", "Std_In_Degree",
                          "Max_Out_Degree", "Min_Out_Degree", "Ave_Out_Degree", "Std_Out_Degree",
                          "Connection_Rate", "DAG_volume", "Max_WCET", "Min_WCET", "Ave_WCET", "Std_WCET", 'Jump_Level']
        for i, feature_i in enumerate(Features_Tytle):
            worksheet.write(i, 0, feature_i)
        for x, DAG_x in enumerate(DAG_list):
            self.dag_param_critical_update(DAG_x, x)
            for i, feature_i in enumerate(Features_Tytle):
                worksheet.write(i, x + 1, DAG_x.graph[feature_i])
        workbook.save(output_path + '/DAG_Features.xls')
        QMessageBox.question(self.window, "Success", "DAG特性抽象完成！", QMessageBox.Yes)
        return True

    #####################################
    #   Section_5: DAG的关键参数分析
    #####################################
    def dag_param_critical_update(self, DAG_obj, i):
        """, worksheet"""
        # "DAG_ID", # "Number_Of_Nodes", # "Number_Of_Edges",
        # "Max_Shape", # "Min_Shape", # "Ave_Shape", # "Std_Shape",
        # "Max_re_shape", # "Min_re_shape", # "Ave_re_shape", # "Std_re_shape",
        # "Width", "Max_Degree", "Min_Degree", "Ave_Degree", "Std_Degree",
        # "Max_In_Degree", "Min_In_Degree", "Ave_In_Degree", "Std_In_Degree",
        # "Max_Out_Degree", "Max_Out_Degree", "Ave_Out_Degree", "Std_Out_Degree",
        # "Connection_Rate"
        # "DAG_volume" "Max_WCET", # "Min_WCET", # "Ave_WCET", # "Std_WCET"
        # #### 0.DAG检测及基本参数 #### #
        assert format(nx.is_directed_acyclic_graph(DAG_obj))
        DAG_obj.graph['DAG_ID'] = str(i)
        DAG_obj.graph['Number_Of_Nodes'] = DAG_obj.number_of_nodes()
        DAG_obj.graph['Number_Of_Edges'] = DAG_obj.number_of_edges()
        # print("DAG_ID:", DAG_obj.graph['DAG_ID'])
        # print("Number of Nodes:", DAG_obj.graph['Number_Of_Nodes'])
        # print("Number of Edges:", DAG_obj.graph['Number_Of_Edges'])
        # section1. 获取DAG的结构相关参数
        # #### 1.关键路径 #### #
        # node_list = nx.dag_longest_path(self.G, weight='weight')  # 关键路径
        # print('关键路径：{0}'.format(node_list))
        # #### 2.最短路径 #### #
        # shortest_path = list(nx.all_shortest_paths(self.G, 0, self.G.number_of_nodes() - 1, weight='weight'))
        # print('DAG的最短路径{0}条：'.format(len(shortest_path)))
        # [print(path) for path in shortest_path]
        # #### 3.获取拓扑分层 shape #### #
        # 3.1 正向shape
        rank_list = [sorted(generation) for generation in nx.topological_generations(DAG_obj)]
        for l, rank_l in enumerate(rank_list):
            for rank_x in rank_l:
                DAG_obj.nodes[rank_x]['rank'] = l

        rank_num_list = [len(x) for x in rank_list]

        DAG_obj.graph['Number_Of_Level'] = len(rank_num_list)
        DAG_obj.graph['Shape_List'] = rank_num_list
        DAG_obj.graph['Max_Shape'] = max(rank_num_list)
        DAG_obj.graph['Min_Shape'] = min(rank_num_list)
        DAG_obj.graph['Ave_Shape'] = np.mean(rank_num_list)
        DAG_obj.graph['Std_Shape'] = np.std(rank_num_list)

        # print('拓扑分层：{0}'.format(rank_list))
        # print('拓扑分层节点数量分布：{0}'.format(rank_num_list))
        # print("Max_Shape:{0}".format( max(rank_num_list) ))
        # print("Min_Shape:{0}".format( min(rank_num_list) ))
        # print("Ave_Shape:{0:0.2f}".format( np.mean(rank_num_list) ))
        # print("Std_Shape:{0:0.2f}".format( np.std(rank_num_list) ))

        # 3.2 反向shape
        re_rank_list = [sorted(generation) for generation in nx.topological_generations(nx.DiGraph.reverse(DAG_obj))]
        re_rank_list.reverse()
        re_rank_num_list = [len(x) for x in re_rank_list]
        DAG_obj.graph['Re_Shape_List'] = re_rank_num_list
        DAG_obj.graph['Max_Re_Shape'] = max(re_rank_num_list)
        DAG_obj.graph['Min_Re_Shape'] = min(re_rank_num_list)
        DAG_obj.graph['Ave_Re_Shape'] = np.mean(re_rank_num_list)  # ave-shape；
        DAG_obj.graph['Std_Re_Shape'] = np.std(re_rank_num_list)   # std-shape；

        # print('反向拓扑分层：{0}'.format(re_rank_list))
        # print('反向拓扑分层节点数量分布：{0}'.format(re_rank_num_list))
        # print("Max_re_shape:{0}".format( max(re_rank_num_list) ))
        # print("Min_re_shape:{0}".format( min(re_rank_num_list) ))
        # print("Ave_re_shape:{0:0.2f}".format( np.mean(re_rank_num_list) ))
        # print("Std_re_shape:{0:0.2f}".format( np.std(re_rank_num_list) ))

        # #### 5.antichains #### #
        # "Width"
        anti_chains_list = list(nx.antichains(DAG_obj, topo_order=None))
        anti_chains_num_list = [len(x) for x in anti_chains_list]
        DAG_obj.graph['Width'] = max(anti_chains_num_list)
        # print("anti-chains:", anti_chains_list)  # 从DAG中生成antichains；
        # print("max anti-chains (Width):", max(anti_chains_num_list) )  # 从DAG中生成antichains；

        # #### 6.degree #### #
        # "Max_Degree", "Min_Degree", "Ave_Degree", "Std_Degree",
        degree_list = [nx.degree(DAG_obj, self_node[0]) for self_node in DAG_obj.nodes(data=True)]
        DAG_obj.graph['Max_Degree'] = max(degree_list)  # max-degree；
        DAG_obj.graph['Min_Degree'] = min(degree_list)  # max-degree；
        DAG_obj.graph['Ave_Degree'] = np.mean(degree_list)  # ave-degree；
        DAG_obj.graph['Std_Degree'] = np.std(degree_list)  # std-degree；
        # print("Max_Degree:{0}".format( max(degree_list) ))
        # print("Min_Degree:{0}".format( min(degree_list) ))
        # print("Ave_Degree:{0:0.2f}".format( np.mean(degree_list) ))
        # print("Std_Degree:{0:0.2f}".format( np.std(degree_list) ))

        degree_in_list = [DAG_obj.in_degree(self_node[0]) for self_node in DAG_obj.nodes(data=True)]
        # "Max_In_Degree", "Min_In_Degree", "Ave_In_Degree", "Std_In_Degree",
        DAG_obj.graph['Max_In_Degree'] = max(degree_in_list)  # max-degree；
        DAG_obj.graph['Min_In_Degree'] = min(degree_in_list)  # max-degree；
        DAG_obj.graph['Ave_In_Degree'] = np.mean(degree_in_list)  # ave-degree；
        DAG_obj.graph['Std_In_Degree'] = np.std(degree_in_list)  # std-degree；
        # print("Max_In_Degree:{0}".format( max(degree_in_list) ))
        # print("Min_In_Degree:{0} —— 均为0".format( min(degree_in_list) ))
        # print("Ave_In_Degree:{0:0.2f}".format( np.mean(degree_in_list) ))
        # print("Std_In_Degree:{0:0.2f}".format( np.std(degree_in_list) ))

        # "Max_Out_Degree", "Max_Out_Degree", "Ave_Out_Degree", "Std_Out_Degree",
        degree_out_list = [DAG_obj.out_degree(self_node[0]) for self_node in DAG_obj.nodes(data=True)]
        DAG_obj.graph['Max_Out_Degree'] = max(degree_out_list)        # max-degree；
        DAG_obj.graph['Min_Out_Degree'] = min(degree_out_list)        # max-degree；
        DAG_obj.graph['Ave_Out_Degree'] = np.mean(degree_out_list)    # ave-degree；
        DAG_obj.graph['Std_Out_Degree'] = np.std(degree_out_list)     # std-degree；
        # print("Max_Out_Degree:{0}".format( max(degree_out_list) ))
        # print("Max_Out_Degree:{0} —— 均为0".format( min(degree_out_list) ))
        # print("Ave_Out_Degree:{0:0.2f}".format( np.mean(degree_out_list) ))
        # print("Std_Out_Degree:{0:0.2f}".format( np.std(degree_out_list) ))

        # #### 7.DAG的稠密度 Density  #### #
        # "Connection_Rate"
        Dag_density = (2 * DAG_obj.number_of_edges()) / (DAG_obj.number_of_nodes() * (DAG_obj.number_of_nodes()-1))
        DAG_obj.graph['Connection_Rate'] = Dag_density

        # #### 8.DAG最差执行时间list  #### #
        WCET_list = [x[1]['WCET'] for x in DAG_obj.nodes.data(data=True)]
        DAG_obj.graph['DAG_volume'] = int(np.sum(WCET_list))
        DAG_obj.graph['Max_WCET'] = float(max(WCET_list))
        DAG_obj.graph['Min_WCET'] = float(min(WCET_list))
        DAG_obj.graph['Ave_WCET'] = float(np.mean(WCET_list))
        DAG_obj.graph['Std_WCET'] = float(np.std(WCET_list))
        # "DAG_volume" "Max_WCET", # "Min_WCET", # "Ave_WCET", # "Std_WCET"
        # print("WCET_list：{0}".format(WCET_list))
        # print("DAG_Volume：{0}".format( np.sum(WCET_list) ))
        # print("Max_WCET：{0}".format( max(WCET_list) ))
        # print("Min_WCET：{0}".format( min(WCET_list) ))
        # print("Ave_WCET：{0:0.2f}".format( np.mean(WCET_list) ))
        # print("Std_WCET：{0:0.2f}".format( np.std(WCET_list) ))

        # #### 9.最大跳层  #### #
        Edges_Jump_List = [DAG_obj.nodes[x[1]]['rank'] - DAG_obj.nodes[x[0]]['rank'] for x in DAG_obj.edges.data()]
        DAG_obj.graph['Jump_Level'] = max(Edges_Jump_List)
        # print("Jump_Level：{0}".format( self.Jump_Level ))


if __name__ == '__main__':
    # # 创建应用
    # window_application = QApplication(sys.argv)
    # # 设置登录窗口
    # login_ui = LoginDialog()
    # # 校验是否验证通过
    # if login_ui.exec_() == QDialog.Accepted:
    G = GUI()
