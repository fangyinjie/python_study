# bar(x, height) / barh(y, width)
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
# make data:
np.random.seed(3)

x1 = 0.5 + np.arange(8)
y1 = np.random.uniform(2, 7, len(x1))

# plot
fig, ax = plt.subplots(1,2)
ax[0].bar(x1, y1, width=1, edgecolor="white", linewidth=0.7)
ax[0].set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
ax[0].title()                 #设置标题，这里只能显示英文，中文显示乱码

# fig2, ax2 = plt.subplots(1,2)
x2 = [1,2,3,4,5,6]     #x轴的坐标
y2 = [1,2,3,4,5,6]     #y轴的值
ax[1].bar(x2, y2)         #构建柱状图
# ax[1].bar(x1, y1, width=1, edgecolor="white", linewidth=0.7)
for x,y in zip(x2, y2):  #在柱子上添加数值
    plt.text(x + 0.1, y, '%.2f' % y, ha='center', va='bottom')



# f = plt.figure()  #创建空图

# plt.ylabel("y_label")            #设置y轴名称
# plt.xlabel("x_label")            #设置x轴名称
plt.show()                       #将图形显示出来