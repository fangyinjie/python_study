import time
import threading

import numpy as np
from Src.DAG_Scheduler import Core


import threading
import time

def test():
    for i in range(5):
        print('test ',i)
        time.sleep(1)

thread = threading.Thread(target=test)
thread.start()
thread.join()

core_test = Core.Core_Obj(0)
print(core_test.Core_ID)
print('test')

'''
自定义线程：继承threading.Thread来定义线程类，其本质是重构Thread类中的run方法
'''
class MyThread(threading.Thread):  # 重写threading.Thread类，加入获取返回值的函数
    def __init__(self, param):
        super(MyThread, self).__init__()  # (2) 重构run函数必须写
        self.param  = param
        self.result = 0

    def run(self):
        self.Exam_function(self.param)

    def Exam_function(self, param):
        time.sleep(int(param) / 10)
        self.result = param


if __name__ == '__main__':
    starrttime1 = time.time()
    for x in range(10):
        time.sleep(x / 10)
        print(x)
    endtime1 = time.time()

    starrttime2 = time.time()

    for x in range(10):
        exec(f"test{x} = MyThread(str(x))")

    for x in range(10):
        exec(f"test{x}.start()")

    for x in range(10):
        exec(f"test{x}.join()")

    print("***************************")

    for x in range(10):
        exec(f"print(format(test{x}.result))")
    endtime2 = time.time()

    print("***************************")
    print(f"runningtime1:{endtime1 - starrttime1}")
    print(f"runningtime2:{endtime2 - starrttime2}")



# def Core_Data_Output(Ret_Core_Data_List, address, running_type: str, DAG_id:str):
#     os.makedirs(address, mode=0o777, exist_ok=True)
#     writer = pd.ExcelWriter(address + running_type + '_' + DAG_id +'__CoreData.xlsx')
#     for core_data_x in Ret_Core_Data_List:
#         colums_list = []
#         data_dict = {}
#         for task_data_id, task_data_x in enumerate(core_data_x.Core_Running_Task):
#             colums_list.append(task_data_id)
#             data_dict[task_data_id] = {'dag_ID': task_data_x['dag_ID'],
#                                        'dag_NUM': task_data_x['dag_ID'],
#                                        'node_id': task_data_x['node'][1]['Node_ID'],
#                                        'node_Index': task_data_x['node'][1]['Node_Index'],
#                                        'start_time': task_data_x['start_time'],
#                                        'end_time': task_data_x['end_time'],
#                                        'excution_time': task_data_x['end_time'] - task_data_x['start_time']}
#         df = pd.DataFrame(data_dict, index=['dag_ID', 'dag_NUM', 'node_id', 'node_Index', 'start_time', 'end_time', 'excution_time'], columns=colums_list).T
#         df.to_excel(writer, sheet_name=str(core_data_x.Core_ID), index=False, header=True)
#     writer.save()
#
#
# def Core_Data_CSV_Output(Ret_Core_Data_List, address, running_type: str, DAG_id: str):
#     os.makedirs(address, mode=0o777, exist_ok=True)
#     out_data = {}
#     out_data_id = 0
#     for core_data_x in Ret_Core_Data_List:
#         for task_data_id, task_data_x in enumerate(core_data_x.Core_Running_Task):
#             out_data[out_data_id] = { 'dag_ID': task_data_x['dag_ID'],
#                                       'dag_NUM': task_data_x['dag_ID'],
#                                       'node_id': task_data_x['node'][1]['Node_ID'],
#                                       # 'node_id': task_data_x['node'][1]['JobTypeID'],
#                                       'node_Index': task_data_x['node'][1]['Node_Index'],
#                                       'start_time': task_data_x['start_time'],
#                                       'end_time': task_data_x['end_time'],
#                                       'excution_time': task_data_x['end_time'] - task_data_x['start_time'],
#                                       'core_id': core_data_x.Core_ID}
#             out_data_id += 1
#     df = pd.DataFrame(out_data, index=['dag_ID', 'dag_NUM', 'node_id', 'node_Index', 'start_time', 'end_time', 'excution_time', 'core_id']).T
#     df.to_csv(address + running_type + DAG_id +'_core.csv')
#
#
#
# def Core_Data_Input(address, file_type):
#     if file_type == 'XLSX':
#         Ret_Core_Data_List = []
#         with pd.ExcelFile(address) as data:
#             all_sheet_names = data.sheet_names
#             for Core_ID_x in all_sheet_names:
#                 core = Core_Obj(Core_ID_x)
#                 df = pd.read_excel(data, Core_ID_x, index_col=None, na_values=["NA"])
#                 for row in df.index:
#                     core.Insert_Task_Info(df.loc[row]['dag_ID'], df.loc[row]['dag_NUM'],
#                                           (df.loc[row]['node_id'], {'Node_ID': df.loc[row]['node_Index'], 'Node_Index': df.loc[row]['node_id']}),
#                                           df.loc[row]['start_time'], df.loc[row]['end_time'])
#                 Ret_Core_Data_List.append(core)
#         return Ret_Core_Data_List
#     elif file_type == 'CSV':
#         df = pd.read_csv(address, index_col=None, na_values=["NA"])
#         core_id_list = list(set(df['core_id']))
#         Ret_Core_Data_dict = {Core_ID_x: Core_Obj(Core_ID_x) for Core_ID_x in core_id_list}
#         for row in df.index:
#             Ret_Core_Data_dict[ df.loc[row]['core_id'] ].Insert_Task_Info(
#                     df.loc[row]['dag_ID'], df.loc[row]['dag_NUM'],
#                     (df.loc[row]['node_id'], {'Node_ID': df.loc[row]['node_id']}),
#                     df.loc[row]['start_time'], df.loc[row]['end_time'])
#         Ret_Core_Data_List = [core_data_x for core_data_id, core_data_x in Ret_Core_Data_dict.items()]
#         return Ret_Core_Data_List
#     else:
#         os.error('file tpye error!')


# if __name__ == "__main__":
#     DAG_type = 'DAG2_M'
#     # DAG_addr = 'D:/github/DAG_Scheduling_Summary/Exam_Input_data/xlsx_data/wireless/DAG_Data.xlsx'
#     rootdir = "D:/github/DAG_Scheduling_Summary/DAG_Scheduling/Exma_code/2023-2-13-/Result_data/test/Importent_file/"
#     DAG_addr = DAG_type + '/core_data/'
#     # parent:父目录; dirnames:所有文件夹名字（不含路径）; filenames:所有文件名字;
#     file_list = os.listdir(rootdir + DAG_addr)
#     FIFO_Core_Data_list_Summary = {}
#     SELF_Core_Data_list_Summary = {}
#     for file_x in file_list:
#         if os.path.splitext(file_x)[1] == '.xlsx':
#             # print(file_x)
#             Core_Data_list = Core_Data_Input(rootdir + DAG_addr + file_x, 'XLSX')
#             file_data_list = file_x.split('_')
#             if file_data_list[0] == 'FIFO':
#                 FIFO_Core_Data_list_Summary[file_data_list[1]] = Core_Data_list
#             elif file_data_list[0] == 'SELF':
#                 SELF_Core_Data_list_Summary[file_data_list[1]] = Core_Data_list
#             else:
#                 os.error('file name error!')
#     data_dict = {}
#     for key_x, value_x in FIFO_Core_Data_list_Summary.items():
#         value_y = SELF_Core_Data_list_Summary[key_x]
#         fifo_makespan = ret_makespan(value_x)
#         self_makespan = ret_makespan(value_y)
#         data_dict[key_x] = {'dag_id': key_x, 'fifo': fifo_makespan, 'self': self_makespan, 'performance': 100 * (fifo_makespan - self_makespan) / fifo_makespan}
#     data_list = sorted(data_dict.items(), key=lambda x: x[1]['performance'], reverse=True)
#     print(data_list[0][0])
#     print(data_list[0][1])
#
#     R_fifo = FIFO_Core_Data_list_Summary[data_list[0][0]]
#     R_self = SELF_Core_Data_list_Summary[data_list[0][0]]
#
#     df = pd.DataFrame({data_x[0]: {"performance": data_x[1]['performance'],
#                                    'core_num': 5,
#                                    'dag_type': DAG_type} for data_x in data_list},
#                       index=["performance", 'core_num', 'dag_type'],
#                       columns=[data_x[0] for data_x in data_list]).T
#     df.to_csv('./' + DAG_type + '.csv')
#
#     fig = plt.figure()
#     FontSize = 12
#
#     ax = plt.subplot(2, 1, 1)
#     print("FIFO:{0}_makespan:{1}={2}".format(data_list[0][0], ret_makespan(R_fifo), ret_makespan(R_fifo)/2.26))
#     SRS.show_single_dag_and_makespan_random(R_fifo, 1 * ret_makespan(R_fifo), ax, 'NS', font_size=FontSize, DAG_T=DAG_type)
#
#     ax = plt.subplot(2, 1, 2)
#     print("FIFO:{0}_makespan:{1}={2}".format(data_list[0][0], ret_makespan(R_self), ret_makespan(R_self)/2.26))
#     SRS.show_single_dag_and_makespan_random(R_self, 1 * ret_makespan(R_self), ax, 'NS', font_size=FontSize, DAG_T=DAG_type)


