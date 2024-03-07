import simpy
from numba import jit

# 使用Numba JIT装饰器来优化仿真函数
@jit
def simulate(env):
    while True:
        # 仿真逻辑代码
        yield env.timeout(1)

# 创建仿真环境
env = simpy.Environment()

# 运行优化后的仿真程序
env.process(simulate(env))
env.run(until=10)