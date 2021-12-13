#非支配排序
import matplotlib.pyplot as plt
import numpy
class Entity:
    def __init__(self):
        self.Sp = set()  #被p支配的个体的集合
        self.np = 0   #支配p的个体的数目

def fast_non_dominated_sort(population, object_num, ):
    Front = []  #存放分级的非支配集
    population_size = len(population)
    dom_list = [Entity() for i in range(population_size)]
    Front1 = []
    for i in range(population_size):
        for j in range(population_size):
            less, more, equal = 0, 0, 0
            for k in range(object_num):
                if population[i][k+1] > population[j][k+1]: #f(a) >= f(b),则a支配b
                    more += 1
                elif population[i][k+1] == population[j][k+1]:
                    equal += 1
                else:
                    less += 1
            if more == 0 and equal != object_num:  # j支配i，相应的np+1
                dom_list[i].np += 1
            elif less == 0 and equal != object_num:  # i支配j,将q加入到Sp中
                dom_list[i].Sp.add(j)
        if dom_list[i].np == 0:  # 若np=0,该个体设为pareto第一级
            rank = 1
            population[i].append(rank) #将等级存放入个体中
            Front1.append(i)
    Front.append(Front1)
    t = 0
    while len(Front[t]) > 0:
        Q = []
        for m in Front[t]:#循环当前支配解集中的个体
            if len(dom_list[m].Sp) > 0:
                for n in dom_list[m].Sp:#个体n中所支配解集的个体
                    dom_list[n].np -= 1
                    if dom_list[n].np == 0: #如果n是非支配解集
                        rank = t+2
                        population[n].append(rank)
                        Q.append(n)
        Front.append(Q)
        t += 1
    population = sorted(population,key = lambda x:x[object_num+1])
    return population,Front

