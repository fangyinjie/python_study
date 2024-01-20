import numpy as np
import matplotlib.pyplot as plt

# pop_size = 10   # 种群数量
# PC = 0.6        # 交叉概率
# PM = 0.01       # 变异概率
# X_max = 5       # 最大值
# X_min = 0       # 最小值
# DNA_SIZE = 10   # DNA长度与保留位数有关,2**10 当前保留3位小数点
# N_GENERATIONS = 1000

##定义全局变量
pop_size = 5    # 种群数量
PC = 0.6        # 交叉概率
PM = 0.01       # 变异概率
X_max = 5       # 最大值
X_min = 0       # 最小值
DNA_SIZE = 10   # DNA长度与保留位数有关,2**10 当前保留3位小数点，这个应该是二进制考虑的问题，保留的规则可以去搜一下，有的实际问题需要实数编码的话，就直接看着所要求的问题设置编码长度就好了
N_GENERATIONS = 100    # 迭代次数

"""
a. 求解的目标表达式为：
y = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
x=[0,5]
"""


def aim(x):
    return 10*np.sin(5*x)+7*np.cos(4*x)


# b.解码函数
def decode(pop):
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) * (X_max-X_min) / float(2**DNA_SIZE-1) + X_min


# c.适应度计算函数
def fitnessget(pred):
    return pred + 1e-3 - np.min(pred)


# d.自然选择函数（轮盘赌）
def select(pop, fitness):
    # print(abs(fitness))
    # print(fitness.sum())
    idx = np.random.choice(np.arange(pop_size), size=pop_size, replace=True,p=fitness/fitness.sum())
    # print(idx)
    return pop[idx]


# e.交叉函数
def change(parent, pop):
    x = np.random.rand()
    print('x:{}'.format(x))
    if x < PC:    #交叉
        i_ = np.random.randint(0, pop_size, size=1)  ##随机找到要与之交叉的某一行，也就是某另一个个体
        print('i_:{}'.format(i_))
        cross_points = np.random.randint(0, 2, size=DNA_SIZE)##生成一个只有0和1的列表，长度等于基因长度
        print('cross_points:{}'.format(cross_points))
        cross_points = cross_points.astype(np.bool)  ##1的地方就是True
        print('cross_points:{}'.format(cross_points))
        print(np.where(cross_points==True))   ##np.where()就是找到True的地方，就是用这种方法来找到1的地方，作为交叉的基因位
        print('cross_points:{}'.format(cross_points))
        print('parent[cross_points]:{}'.format(parent[cross_points]))
        parent[cross_points] = pop[i_, cross_points]
        print('parent:{}'.format(parent))
    return parent


# f.变异函数
def variation(child,pm):                  #变异
    for point in range(DNA_SIZE):
        if np.random.rand() < pm:
            child[point] = 1 if child[point] == 0 else 0
    # print(child)
    return child



##生成初始解，这个初始种群就是一个可行解的集合，在这样的条件下进行选择、交叉和变异操作，选出最适应当前环境的个体，也就得到了我们的最优解
pop = np.random.randint(2, size=(pop_size, DNA_SIZE))  ###得到初始化种群
# print(pop)
X = np.arange(0, N_GENERATIONS, 1)
Y = [None] * N_GENERATIONS  ##先产生一个全部都是0的列表，用于存放每一次迭代的最优值，最后进行画图展示迭代过程
for i in range(N_GENERATIONS):  ##上面写的选择、交叉、变异都是在一次进化中的操作，每一次迭代都要进行
    # 解码
    # print(pop)
    X_value = decode(pop)

    # 获取目标函数值
    F_values = aim(X_value)

    # 获取适应值
    fitness = fitnessget(F_values)
    # print(fitness)
    if (i == 0):
        max = np.max(F_values)
        max_DNA = pop[np.argmax(F_values), :]  ##取取得适应度最大值的那个个体

    if (max < np.max(F_values)):
        max = np.max(F_values)
        max_DNA = pop[np.argmax(F_values), :]

    if (i % 10 == 0):
        print("Most fitted value and X: \n",
              np.max(F_values), decode(pop[np.argmax(F_values), :]))
    # 选择
    pop = select(pop, fitness)
    # print(pop)
    pop_copy = pop.copy()
    # print(pop_copy)
    for index, parent in enumerate(pop):
        # print(parent)
        child = change(parent, pop_copy)
        child = variation(child, PM)
        # print(child)
        pop[index] = child
    Y[i] = max
print("目标函数最大值为：", max)
print("其DNA值为：", max_DNA)
print("其X值为：", decode(max_DNA))
plt.plot(X, Y)
plt.show()