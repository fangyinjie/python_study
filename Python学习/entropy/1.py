#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # 
# entropy
# Create Time: 2023/8/71:32
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
import math


# word_dict = {(xi:p(xi))}
# (*) 希望值计算
def expectation(word_dict):
    return sum([word_i * word_p for word_i, word_p in word_dict.items()])

# (*) 欧式距离
def Euclidean_Distance(word_dict, word_dict1, bit):
    ret = 0
    for word_i, word_p in word_dict.items():
        ret += pow(abs(word_dict1[word_i] - word_p), bit)
    return pow(ret, (1/bit))

# 结论：logb(1/p(x)) 中 b的值为x的数量最好
# (1) 信息熵
def entropy1(word_dict, bit):
    ret = 0
    for word_i, word_p in word_dict.items():
        ret -= word_p * math.log(word_p, bit)
    return ret


# (2) 交叉熵  L(p, q)
def entropy2(word_dict_p, word_dict_q, bit):
    ret = 0
    for word_i, word_p in word_dict_p.items():
        # ret -= word_p * math.log2(word_dict_q[word_i])
        ret -= word_p * math.log(word_dict_q[word_i], bit)
    return ret


if __name__ == "__main__":
    """
    word_dict = {1:0.5, 2:0.5}
    word_dict1 = {1:0.1, 2:0.9}
    word_dict2 = {1:0.2, 2:0.8}
    word_dict3 = {1:0.3, 2:0.7}
    word_dict4 = {1:0.4, 2:0.6}
    """


    word_dict  = {1:0.1, 2:0.1, 3:0.1, 4:0.1, 5:0.1, 6:0.1, 7:0.1, 8:0.1, 9:0.1, 0:0.1}
    word_dict1 = {1:0.01, 2:0.03, 3:0.05, 4:0.07, 5:0.09, 6:0.11, 7:0.13, 8:0.15, 9:0.17, 0:0.19}
    word_dict2 = {1:0.01, 2:0.03, 3:0.05, 4:0.07, 5:0.09, 6:0.11, 7:0.13, 8:0.15, 9:0.17, 0:0.19}



    print(expectation(word_dict))
    print(entropy1(word_dict, 2))
    print(entropy1(word_dict, math.e))
    print()

    for bit_x in [2, math.e, 10]:
        print(entropy2(word_dict, word_dict1, bit_x))
        # print(entropy2(word_dict, word_dict2, bit_x))
        # print(entropy2(word_dict, word_dict3, bit_x))
        # print(entropy2(word_dict, word_dict4, bit_x))
        print(entropy2(word_dict, word_dict, bit_x))
        print()
    pass

    word_c1  = {1:1, 2:1}
    word_c2  = {1:4, 2:5}
    print(Euclidean_Distance(word_c1, word_c2, 2))