import numpy as np


def caculate(a, b, c):
    return c % 6, b % 8, a % 8


if __name__ == "__main__":
    # cc = np.full(shape=(5), fill_value=False)
    # for id, x in enumerate(cc):
    #     print(f'value:{x}_id:{id}')
    # # cc[1][1] = True
    # print('')
    # # print(cc[:, :])
    # print(cc) 1231
    a1 = 313  # 第一个数字 下卦
    b1 = 644  # 第一个数字 上挂
    c1 = 522  # 第一个数字 爻位3
    print(caculate(a1, b1, c1))

