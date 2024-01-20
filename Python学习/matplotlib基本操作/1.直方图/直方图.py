# bar(x, height) / barh(y, width)
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()  #创建空图
# plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(nrows=2, ncols=2)
# (1)
ax[0, 0].set(title='Upper Left')
# ax[0,0].set_title('bar1')  #设置标题，这里只能显示英文，中文显示乱码
x1 = 0.5 + np.arange(8)
y1 = np.random.uniform(2, 7, len(x1))
ax[0,0].bar(x1, y1, width=1, edgecolor="white", linewidth=0.7)
ax[0,0].set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

# (2)
ax[0, 1].set(title='Upper Right')
# ax[0,1].set_title('bar2')   # 设置标题，这里只能显示英文，中文显示乱码
x = [1,2,3,4,5,6]          # x轴的坐标
y = [1,2,3,4,5,6]          # y轴的值
ax[0,1].bar(x, y)         # 构建柱状图
for x,y in zip(x, y):     # 在柱子上添加数值
    ax[0,1].text(x + 0.1, y, '%.2f' % y, ha='center', va='bottom')

# (3)
ax[1, 0].set(title='Lower Left')
x = 4 + np.random.normal(0, 1.5, 200)
ax[1, 0].hist(x, bins=8, linewidth=0.5, edgecolor="white")
ax[1, 0].set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 56), yticks=np.linspace(0, 56, 9))

# (4)
ax[1, 1].set(title='Lower Right')
x = np.random.randn(5000)
y = 1.2 * x + np.random.randn(5000) / 3
ax[1, 1].hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))
ax[1, 1].set(xlim=(-2, 2), ylim=(-3, 3))

for c1 in range(2):
    for c2 in range(2):
        ax[c1,c2].set_ylabel("y_label")            # 设置y轴名称
        ax[c1,c2].set_xlabel("x_label")            # 设置x轴名称

plt.show()                             # 将图形显示出来

