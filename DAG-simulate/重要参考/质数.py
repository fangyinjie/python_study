# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
# Filename : test1.py
# author by : www.runoob.com

# Python 程序用于检测用户输入的数字是否为质数

def prime_number_judge(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False


if __name__ == "__main__":
    p = 100
    y = []
    h = []
    for x in range(100):
        if prime_number_judge(x):
            print(x)
            y.append(x)
            h.append(x)

        #     ax = self.fig.add_subplot(111)
        #     x = np.linspace(0, 100, 100)
        #     y = np.random.random(100)
        #     ax.cla() # TODO:删除原图，让画布上只有新的一次的图
        #     ax.plot(x, y)
        #     self.canvas.draw() # TODO:这里开始绘制
        # except Exception as e:
        #     print(e)

    # for x in range(p):

    # h = range(100)
    # x = [1, 2, 3]
    # y = [1, 2, 3]
    # y = x
    plt.plot(h, y, 'g-.o')
    plt.show()