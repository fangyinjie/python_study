import numpy as np
import matplotlib.pyplot as plt

# 创建一个x值的数组
x = np.linspace(0.1, 100, 400)

# 创建y值数组，这里我们用对数函数
y = 25 * np.log(x)
y1 = 5 * x
# 创建一个新的图形
plt.figure()

# 在当前图形中添加一个新的坐标轴
plt.plot(x, y)
plt.plot(x, y1)

# 设置x轴的标签
plt.xlabel('x')

# 设置y轴的标签
plt.ylabel('log(x)')

# 设置图形的标题
plt.title('Logarithmic Function')

# 显示图形
plt.grid(True)
plt.show()

print(50 * np.log10(10))