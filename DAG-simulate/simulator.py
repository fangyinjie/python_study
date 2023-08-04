import random
import simpy
import networkx as nx
import DAG_Set
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import copy
import os
# import xlwt

global maxp


class Dispatcher_Workspace(object):
    """ 一个处理器（Processor），拥有特定数量的资源（core，内存，缓存等）。
    一个客户首先申请服务。在对应服务时间完成后结束并离开工作站 """
    def __init__(self, env, Dag_Set, core_num, Main_Event):
        self.is_heterogeneou = False    # 默认为同构系统
        self.is_preemptive   = False    # 默认为不可抢占   'non-preemptive' 'non-preemptive'

        self.env             = env  # simpy实体
        self.Dag_Set         = Dag_Set
        self.core_num        = core_num
        self.core_Set        = simpy.Resource(env, core_num)
        self.Dag_Set.Status_Data_Up()
        self.makespan_dict   = {}
        self.Temp_DAG_Set    = copy.deepcopy(self.Dag_Set)
        self.main_event      = Main_Event

    # 每个core的运作，系统中有几个core就有几个Core_act进程
    def Core_act(self, environment, core_ID):
        while self.Temp_DAG_Set.get_node_num() > 0:
            with self.core_Set.request() as request:
                yield request
                # step1.有core资源的情况下，搜索当前的Dag_Set中处于就绪态的节点list。
                # 获取优先级最高的DAG以及此DAG中进入就绪状态的node list
                DAG_ID, ready_high_node = self.Temp_DAG_Set.get_priorituy_ready_node()
                if not ready_high_node:
                    yield env.timeout(1)
                    continue
                # step2.将此list中优先级最高的节点上处理器，状态进入运行态；并记录开始时间
                start_time = environment.now
                ready_high_node[1]['state'] = 'running'
                # step3.运行节点，timeout = WCET / ET
                # ET = ready_high_node[1].get('ET')
                ET = ready_high_node[1].get('WCET')
                yield environment.process(self.Node_run(ET))
                # step4.记录终止时间
                end_time = environment.now
                self.Temp_DAG_Set.delet_DAG_Node(DAG_ID, ready_high_node[0])
                self.Temp_DAG_Set.Status_Data_Up()
                # step5.打印，core_ID;
                # print("Core_ID:{0}, DAG_ID:{1}, node_ID:{2}, start_time:{3}, end_time：{4}".format(
                #     core_ID, DAG_ID, ready_high_node[1].get('Node_ID'), start_time, end_time))
                if self.makespan_dict.get(core_ID) is None:
                    self.makespan_dict[core_ID] = [(DAG_ID, ready_high_node[1].get('Node_ID'), start_time, end_time)]
                else:
                    self.makespan_dict[core_ID].append((DAG_ID, ready_high_node[1].get('Node_ID'), start_time, end_time))
        self.main_event.succeed('task_finish')
        self.main_event = self.env.event()

    def Node_run(self, run_time):
        yield env.timeout(run_time)

    def CPU_uilization(self, makespan_dict, makespan):
            core_num = len(makespan_dict)
            all_execution_time = 0
            for x in makespan_dict.items():
                for y in x[1]:
                    all_execution_time += y[3]-y[2]
            return all_execution_time / (core_num * makespan)

    def makespan_compute(self):
        temp_endtime_list = []
        for k, v in self.makespan_dict.items():
            for x in v:
                temp_endtime_list.append(x[3])
        temp_endtime_list.sort()
        return temp_endtime_list[-1]


def setup(environment, Dag, core_num):
    """ 创建一个工作站，几个初始客户，然后持续有客户到达. 每隔 t_inter - 2, t_inter + 3分钟（可以自定义）. """
    main_event = environment.event()    # 构建调度器事件，该事件确定各core（进程的状态）
    Dispatcher = Dispatcher_Workspace(environment, Dag, core_num, main_event)   # 分配器建立资源，只要有资源就开始运行
    for i in range(core_num):                                                   # 每个核分配一个进程；
        env.process(Dispatcher.Core_act(env, "core_{0}".format(i)))             # 创建clientNumber个初始客户
    while True:
        value = yield main_event
        if value == 'task_finish':
            Dispatcher.show_dag_and_makespan()
            break


if __name__ == "__main__":
    # 1. 是否可抢占
    # 2. 是否为混合关键调度
    # 3. 是否为异构环境
    Core_Num = 3
    # 获取DAG
    #（1）python 文件
    DAG_Set_Obj = DAG_Set.DAG_Set()
    DAG_Set_Obj.user_defined_priority()
    #（2）sav文件
    env = simpy.Environment()                               # 创建一个环境并开始仿真
    proc = env.process(setup(env, DAG_Set_Obj, core_num=Core_Num))
    env.run(until=proc)

