import numpy as np
import matplotlib.pyplot as plt


# 定义函数
def f(x1):
    return (1 + x1) / (1 - x1)


# 生成一组x值
# x1 = np.arange(-1, 1, 0.1)

x2 = np.arange(-1, 1, 0.1)
# 根据函数计算一组y值
y = f(x2)

# 绘制函数曲线图
plt.plot(x2, y)

# 展示图像
plt.show()
