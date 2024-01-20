import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn import preprocessing
import numpy as np


def Normalize(array):
    '''Normalize the array'''
    mx = np.nanmax(array)
    mn = np.nanmin(array)
    t = (array-mn)/(mx-mn)
    return t


sns.set()
iris = sns.load_dataset('iris', data_home='.')
iris.head(2)
# axesSub = sns.boxplot(x='species', y='sepal_length', data=iris)
# axesSub = sns.stripplot(x='species', y='sepal_length', data=iris, ax=axesSub)  # ax=axesSub，指定坐标性, 在之前箱型图基础上，继续绘制条带图
# axesSub = sns.lineplot(x='species', y='sepal_length', data=iris, ax=axesSub)  # ax=axesSub，指定坐标性, 在之前箱型图基础上，继续绘制折线图
# plt.show()

fig, ax =plt.subplots(1,3,constrained_layout=True, figsize=(12, 3))
axesSub = sns.boxplot(x="species", y="sepal_length", data=iris, ax=ax[0])
axesSub.set_title('boxplot')
axesSub = sns.stripplot(x="species", y="sepal_length", data=iris, ax=ax[1])
axesSub.set_title('stripplot')
axesSub = sns.histplot(x="sepal_length", data=iris, ax=ax[2])
_ = axesSub.set_title('histplot')
plt.show()


# file = 'data.txt'
# data1 = pd.read_csv(file, sep=",")
data1 = pd.read_csv('data_real.csv')
plt.figure()
# data1.makespan = Normalize(data1.makespan)

# sns.boxplot(y='makespan', x='Core', hue="names", data=data1, dodge=False, width=0.2)
# sns.boxplot(x="makespan", y="Core", data=data1)

# sns.boxplot(y='makespan', x='Core',hue="names",data=data1, linewidth=1.5, showfliers=False)
# sns.boxplot(y='makespan', x='Parallelism',hue="names",data=data1, linewidth=1.5, showfliers=False)
sns.boxplot(y='makespan', x='Core', hue="names", data=data1, linewidth=1.5, showfliers=True)
plt.title("Core_test")      # 图形标题
plt.xlabel("x Core")        # x 轴名称
plt.ylabel("y makespan")    # y 轴名称
# sns.boxplot(x="age", y="cost", data=data, hue="sex", width=0.5, linewidth=1.0, palette="Set3")
plt.show()

