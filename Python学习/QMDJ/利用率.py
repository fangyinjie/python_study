import sys
import math

# def utilization(core_num):
#     return (core_num + 1) * 0.414213562373095

def utilization(core_num, vol, makespan):
    return 100 * vol / (core_num * makespan)


def time_improforme(HUAWEI_TIME, SELF_TIME):
    return 100 * (HUAWEI_TIME - SELF_TIME) / HUAWEI_TIME

if __name__ == '__main__':
    # Core_Num = 5)
    # print(utilization(Core_Num)
    # Time_data = (93436, 93436)
    # Time_data = (93436, 72012)
    # Time_data = (93436, 85776)
    # Time_data = (93436, 120208)
    #
    # Time_data = (950512, 908756)
    # Time_data = (1553416, 1157548)
    # Time_data = (950512, 763312)
    Time_data = (250000, 130000)
    print("time imporforment = {0:.4f}%".format(
        time_improforme(Time_data[0], Time_data[1])     ))

    # c_data = [10, 10464420, 1553416]
    # c_data = [10, 10464420, 1157548]
    # c_data = [5, 3290012, 950512]
    # c_data = [5, 3290012, 763312 ]
    # c_data = [10, 1046260, 250000]
    c_data = [3, 316260, 115060 ]
    print("utilization = {0:.4f}%\n".format(
        utilization(c_data[0], c_data[1], c_data[2])    ))