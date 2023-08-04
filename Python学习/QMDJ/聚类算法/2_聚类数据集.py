from numpy import where
from sklearn.datasets import make_classification
from matplotlib import pyplot
import sklearn
print(sklearn.__version__)

# 使用make _ classification()函数创建一个测试二分类数据集。
# 这将有助于了解，至少在测试问题上，群集的识别能力如何。该测试问题中的群集基于多变量高斯，并非所有聚类算法都能有效地识别这些类型的群集。
# 因此，本教程中的结果不应用作比较一般方法的基础。下面列出了创建和汇总合成聚类数据集的示例。
# 综合分类数据集
# 定义数据集
X, y = make_classification(
    n_samples=1000,             # 数据集有1000个示例；
    n_features=2,               # 每个类有2个输入要素；
    n_informative=2,
    n_redundant=0,
    n_classes=3,                # 分类问题的类(或标签)的数量。
    n_clusters_per_class=1,     # 一个群集；
    random_state=4)
# 为每个类的样本创建散点图
for class_value in range(2):
    row_ix = where(y == class_value)            # 获取此类的示例的行索引
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])  # 创建这些样本的散布

pyplot.show()       # 绘制散点图
# 运行该示例将创建合成的聚类数据集，然后创建输入数据的散点图，其中点由类标签（理想化的群集）着色。
# 我们可以清楚地看到两个不同的数据组在两个维度，并希望一个自动的聚类算法可以检测这些分组。
