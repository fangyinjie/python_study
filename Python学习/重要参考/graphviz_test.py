import graphviz as gz
import random


"""
绘制简易神经网络图（有向图）
  :param inp: 输入神经元个数
  :param hide: 隐藏层神经元个数, 可迭代数组
  :param outp: 输出神经元个数
  :param inp_label: 输入名称显示
  :param hide_label: 隐藏层名称显示
  :param outp_label: 输出名称显示
  :param dropout: 是否全连接
  :param style: 水平或垂直显示， 可选项为 'h', 'v'
  :param size: 图像显示大小
  :return: 有向图
  """

# dot = gz.Digraph()
# dot.node('1', 'Test1')
# dot.node('2', 'Test2')
# dot.node('3', 'Test3')
# dot.node('4', 'Test4')
# dot.edges(['12', '23', '34', '24'])

dot = gz.Digraph()
for i in range(10):
    dot.node('%s' % i, 'Test\n%s' % i)

dot.edges([str(random.randint(10, 99)) for i in range(10)])

print(dot.source)
dot.view()