# import numpy as np


def caculate(a, b, c):
    return c % 6, b % 8, a % 8


if __name__ == "__main__":
    # cc = np.full(shape=(5), fill_value=False)
    # for id, x in enumerate(cc):
    #     print(f'value:{x}_id:{id}')
    # # cc[1][1] = True
    # print('')
    # # print(cc[:, :])
    # print(cc)
    a1 = 651  # 第一个数字 下卦
    b1 = 237  # 第一个数字 上挂
    c1 = 859  # 第一个数字 爻位
    print(caculate(a1, b1, c1))
