#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Real-Time Systems Group
Hunan University HNU
Created by Fang YJ on 2023/10/25.
"""
import time
import random
import numpy as np
from threading import Thread
import matplotlib.pyplot as plt
from deap import base, creator, tools
from multiprocessing import Process, Manager, Event, Pool
hi_node_num, lo_node_num = 15, 15

P_MUTATION = 0.1  # 变异的概率
P_CROSSOVER = 0.9  # 交叉的概率
MAX_GENERATION = 500  # 停止条件中的最大迭代次数
POPULATION_SIZE = 96  # 种群中的个体数量(越大越平滑)

def Frame_Init():
    # (1) Obj create
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    # (2) Tool create
    toolbox = base.Toolbox()  # 定义toolbox变量
    # toolbox.register("zeroOrOne", random.randint, 0, 1)  # 注册zeroOrOne运算
    toolbox.register("zeroOrOne", random.choice, [True, False])  # 注册zeroOrOne运算


    toolbox.register("individualCreator", tools.initRepeat,
                     creator.Individual,                       # (1) 将creator.Individual类作为放置结果对象的容器类型
                     toolbox.zeroOrOne,                              # (2) zeroOrOne操作是生成对象的函数
                     hi_node_num * lo_node_num)                      # (3) 常量ONE_MAX_LENGTH作为要生成的对象数目

    toolbox.register("populationCreator", tools.initRepeat, list,  # (1) 将列表类作为容器类型
                     toolbox.individualCreator)  # (2) 用于生成列表中对象的函数——personalCreator运算符
    # toolbox.register("populationCreator", tools.initRepeat, list,  # (1) 将列表类作为容器类型
    #                  toolbox.zeroOrOne)  # (2) 用于生成列表中对象的函数——personalCreator运算符
    toolbox.register("evaluate", oneMaxFitness)

    toolbox.register("select", tools.selTournament, tournsize=3)   # (1) 创建遗传算子1-选择运算符;
    toolbox.register("mate", tools.cxOnePoint)                     # (2) 创建遗传算子2-交叉运算符;
    toolbox.register("mutate", tools.mutFlipBit, indpb=1.0 / (hi_node_num * lo_node_num))  # (3) 创建遗传算子3-变异运算符;
    return toolbox



def oneMaxFitness(individual):
    return sum(individual) #  / (100 * hi_node_num * lo_node_num)


def Main(toolbox, event, sd, pt):
    print(f"\nsetp 0. population init:")    # （1） 种群初始化
    offspring = toolbox.populationCreator(n=POPULATION_SIZE)

    # for x in range(hi_node_num * lo_node_num):
    #     offspring[0][x] = True

    for Gen_Counter in range(MAX_GENERATION):
        print(f"\n# ######## Generation:{Gen_Counter}- Population:{len(offspring)}- "
              f"Run at:{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} ######## # ")

        print(f"\nsetp 1. individual evaluation:", end='\t')
        st = time.time()
        freshIndividuals = [ind for ind in offspring if not ind.fitness.valid]

        # with Pool(processes=cpu_count()) as pool:
        #     fitnessValues = pool.map(toolbox.evaluate, freshIndividuals)
        fitnessValues = map(toolbox.evaluate, freshIndividuals)

        for individual, fitnessValue in zip(freshIndividuals, fitnessValues):
            individual.fitness.values = (fitnessValue,)

        fitnessValues = [ind.fitness.values[0] for ind in offspring]

        maxFitnessValue, meanFitnessValue, minFitnessValue = max(fitnessValues), np.mean(fitnessValues),  min(fitnessValues)

        sd.append((maxFitnessValue, meanFitnessValue, minFitnessValue))
        best_Id = np.argmax([Individual_x.fitness.values[0] for Individual_x in offspring])
        for id in range(hi_node_num * lo_node_num):
            pt[id] = offspring[best_Id][id]

        et = time.time()
        print(f"cost time : {et-st}")
        print(f"Max Fitness = {maxFitnessValue}, Avg Fitness = {meanFitnessValue}, Min Fitness = {minFitnessValue}", end='\t')

        event.set()
        if maxFitnessValue > hi_node_num * lo_node_num:
            break

        print(f"\nsetp 2. individual select :", end='\t')
        st = time.time()
        offspring = toolbox.select(offspring, len(offspring))   # 遗传运算符1——selection运算符（toolbox.select定义的锦标赛选择），将物种及其长度作为参数传递给选择运算符
        offspring = list(map(toolbox.clone, offspring))
        et = time.time()
        print(f"cost time : {et-st}", end='\n')

        print(f"\nsetp 3. group recombination:", end='\t')
        st = time.time()
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < P_CROSSOVER:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < P_MUTATION:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        et = time.time()
        print(f"cost time : {et-st}")


def threadStart(event, sd, ls, pt, pp):
    while True:
        event.wait()
        event.clear()
        print(f'update')
        # pt = np.random.choice(a=[True, False], size=(hi_node_num, lo_node_num))
        # pp.set_array(np.random.choice(a=[True, False], size=(hi_node_num, lo_node_num)))
        pp.set_array(np.array(pt).reshape(hi_node_num, lo_node_num))

        print(pt)
        for s, l in zip(zip(*sd), ls):
            l.set_xdata(list(range(len(s[1:]))))
            l.set_ydata(s[1:])
        plt.draw()

def Syn_View(event, sd, pt):
    # plt.xlabel("Generation")
    # plt.ylabel("Max / Average Fitness")
    # plt.title("Max and Average fitness over Generation")

    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].clear()
    axes[0].set(title='Preemption Table', xlabel='X-Axis', ylabel='Y-Axis')

    # pt = np.random.choice(a=[True, False], size=(hi_node_num, lo_node_num))
    # pp = axes[0].imshow(np.array(pt).reshape(hi_node_num, lo_node_num))
    pp = axes[0].imshow(np.random.choice(a=[True, False], size=(hi_node_num, lo_node_num)))

    axes[1].set(title='Fitness curve', xlabel='X-Axis', ylabel='Y-Axis')
    ls = []
    for sdx in zip(*sd):
        lt, = axes[1].plot(sdx[1:], lw=2)
        ls.append(lt)
        # plt.plot(maxFitnessValues, color="red")
        # plt.plot(meanFitnessValues, color="green")
    axes[1].set_yticks(np.arange(0, 300, 30))
    axes[1].set_xticks(np.arange(0, MAX_GENERATION, MAX_GENERATION / 10))
    t = Thread(target=threadStart, args=(event, sd, ls, pt, pp, ))
    t.start()

    plt.show()
    # plt.savefig(save_addr + f"{cn}_{itera_id}.pdf")


if __name__ == "__main__":
    print(f'Code running start at:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 1. source data input and initialization
    with Manager() as manager:
        # 2. GA launch
        e = Event()
        sd = manager.list([(0, 0, 0)])
        pt = manager.list([False for _ in range(hi_node_num * lo_node_num)])
        tb = Frame_Init()

        p_main = Process(target=Main, args=(tb, e, sd, pt, ))
        p_view = Process(target=Syn_View, args=(e, sd, pt, ))

        p_main.start()
        p_view.start()

        p_main.join()
        p_view.join()
