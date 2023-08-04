# 光谱聚类是一类通用的聚类方法，取自线性线性代数。
# 最近在许多领域出现的一个有希望的替代方案是使用聚类的光谱方法。这里，使用从点之间的距离导出的矩阵的顶部特征向量。
#       —源自：《关于光谱聚类：分析和算法》，2002年
# 它是通过 Spectral 聚类类实现的，而主要的 Spectral 聚类是一个由聚类方法组成的通用类，
# 取自线性线性代数。要优化的是“ n _ clusters ”超参数，用于指定数据中的估计群集数量。下面列出了完整的示例。
# spectral clustering
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import SpectralClustering
from matplotlib import pyplot
# 定义数据集
X, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4)
# 定义模型
model = SpectralClustering(n_clusters=2)
# 模型拟合与聚类预测
yhat = model.fit_predict(X)
# 检索唯一群集
clusters = unique(yhat)
# 为每个群集的样本创建散点图
for cluster in clusters:
# 获取此群集的示例的行索引
    row_ix = where(yhat == cluster)
# 创建这些样本的散布
pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# 绘制散点图
pyplot.show()