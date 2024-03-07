from deap import base
from deap import creator
from deap import tools
import random
import matplotlib.pyplot as plt
import numpy as np
import time

P_MUTATION = 0.1  # 变异的概率
P_CROSSOVER = 0.9  # 交叉的概率
MAX_GENERATION = 500  # 停止条件中的最大迭代次数
ONE_MAX_LENGTH = 15  # 优化的bit字符串的长度
POPULATION_SIZE = 200  # 种群中的个体数量(越大越平滑)


def time_val(dec):
    def time_inner(*args, **kwargs):
        st = time.time()
        get_str = dec(*args, **kwargs)
        et = time.time()
        print(f'\n函数总共耗时：{et - st}')
        return get_str

    return time_inner

def oneMaxFitness(individual):
    matrix = np.array(individual).reshape((ONE_MAX_LENGTH, ONE_MAX_LENGTH))
    return np.sum(matrix),

@time_val
def main():
    population = toolbox.populationCreator(n=POPULATION_SIZE)        # （1）通过populationCreator操作创建初始种群（POPULATION_SIZE）：
    fitnessValues = list(map(toolbox.evaluate, population))          # （2）计算初始种群中个体的适应度，map()函数将evaluate操作应用于种群中的每个个体。
    for individual, fitnessValue in zip(population, fitnessValues):  # （3）将适应度值分配给每个个体的适应度元组：
        individual.fitness.values = fitnessValue
    # fitnessValues = [individual.fitness.values[0] for individual in population]
    fitnessValues = list(next(zip(*fitnessValues)))  # 第一次 [0]
    maxFitnessValues = []       # 最大适应度
    meanFitnessValues = []      # 平均适应度

    Gen_Counter = 0
    # np.max
    while max(fitnessValues) < ONE_MAX_LENGTH * ONE_MAX_LENGTH and (Gen_Counter := Gen_Counter + 1) < MAX_GENERATION:
        offspring = toolbox.select(population, len(population))   # 遗传运算符1——selection运算符（toolbox.select定义的锦标赛选择），将物种及其长度作为参数传递给选择运算符
        offspring = list(map(toolbox.clone, offspring))
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < P_CROSSOVER:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < P_MUTATION:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        freshIndividuals = [ind for ind in offspring if not ind.fitness.valid]
        freshFitnessValues = list(map(toolbox.evaluate, freshIndividuals))
        for individual, fitnessValue in zip(freshIndividuals, freshFitnessValues):
            individual.fitness.values = fitnessValue

        population[:] = offspring

        fitnessValues = [ind.fitness.values[0] for ind in population]

        maxFitnessValue = max(fitnessValues)
        meanFitnessValue = sum(fitnessValues) / len(population)
        maxFitnessValues.append(maxFitnessValue)
        meanFitnessValues.append(meanFitnessValue)
        print("- Generation {}: Max Fitness = {}, Avg Fitness = {}".format(Gen_Counter, maxFitnessValue,
                                                                           meanFitnessValue))

        best_index = fitnessValues.index(max(fitnessValues))
        # print("Best Indivadual = ", *population[best_index], "\n")

    plt.plot(maxFitnessValues, color="red")
    plt.plot(meanFitnessValues, color="green")
    plt.xlabel("Generation")
    plt.ylabel("Max / Average Fitness")
    plt.title("Max and Average fitness over Generation")
    plt.show()


if __name__ == "__main__":
    # (1) Obj create
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    # creator.create("Individual", np.ndarray, fitness=creator.FitnessMax)  # 定义个体类型

    # (2) Tool create
    toolbox = base.Toolbox()  # 定义toolbox变量
    toolbox.register("zeroOrOne", random.randint, 0, 1)  # 注册zeroOrOne运算
    # toolbox.register("zeroOrOne", np.random.choice, a=[1, 0], size=ONE_MAX_LENGTH)  # 注册zeroOrOne运算
    toolbox.register("individualCreator", tools.initRepeat,
                     creator.Individual,                       # (1) 将creator.Individual类作为放置结果对象的容器类型
                     toolbox.zeroOrOne,                              # (2) zeroOrOne操作是生成对象的函数
                     ONE_MAX_LENGTH * ONE_MAX_LENGTH)                # (3) 常量ONE_MAX_LENGTH作为要生成的对象数目

    toolbox.register("populationCreator", tools.initRepeat, list,  # (1) 将列表类作为容器类型
                     toolbox.individualCreator)  # (2) 用于生成列表中对象的函数——personalCreator运算符
    # toolbox.register("populationCreator", tools.initRepeat, list,  # (1) 将列表类作为容器类型
    #                  toolbox.zeroOrOne)  # (2) 用于生成列表中对象的函数——personalCreator运算符
    toolbox.register("evaluate", oneMaxFitness)

    toolbox.register("select", tools.selTournament, tournsize=3)  # (1) 创建遗传算子1-选择运算符;
    toolbox.register("mate", tools.cxOnePoint)  # (2) 创建遗传算子2-交叉运算符;
    toolbox.register("mutate", tools.mutFlipBit, indpb=1.0 / ONE_MAX_LENGTH)  # (3) 创建遗传算子3-变异运算符;

    main()
