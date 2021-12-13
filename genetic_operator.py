import random
import numpy as np
from itertools import product
from objectfun import *
from tournament_selection import *
from numba import jit
#@jit
def genetic_operator(population, pc, pm, ratmatrix,object_num,tournament_size,predictedlist):#candidate,T
    [user_num, rem_num] = population[0][0].shape
    population_size = len(population)
    offspring = []
    pool_size = int(population_size / 2)
    a = np.random.random((1, pool_size))[0]
    for n in range(pool_size):
        parent1 = tournament_selection(population, object_num, tournament_size)[0]  # 随机选取两个个体作为父类
        parent2 = parent1
        while (parent1 - parent2).any () == False:
            parent2 = tournament_selection(population, object_num, tournament_size)[0]
        if a[n] < pc:
            child1,child2 = parent1.copy(),parent2.copy() #深拷贝
            for i in range(user_num):
                child1_list = [j for j in range(rem_num) if parent1[i][j] not in parent2[i]]
                child2_list = [j for j in range(rem_num) if parent2[i][j] not in parent1[i]]
                number = np.random.random((1, len(child1_list)))[0]
                length = len(child1_list)
                for k in range(length):
                    if number[k] > 0.5:
                        child1[i][child1_list[k]] = parent1[i][child1_list[k]]
                        child2[i][child2_list[k]] = parent2[i][child2_list[k]]
                    else:
                        child1[i][child1_list[k]] = parent2[i][child2_list[k]]
                        child2[i][child2_list[k]] = parent1[i][child1_list[k]]
        else:
            child1,child2 = parent1,parent2
        #mu_child = random.sample([child1, child2], 1)[0]
        for mu_child in [child1,child2]:
            child = mu_child.copy()
            mu_array = np.random.random((user_num, rem_num))
            mu_location = np.argwhere(mu_array < pm) #变异
            if len(mu_location):
                for location in mu_location:
                    mutation = random.choice(predictedlist[location[0]])
                    while mutation in mu_child[location[0]] or mutation in child[location[0]]:  # and letter < 1000:#防止卡死
                            mutation = random.choice(predictedlist[location[0]])
                    child[location[0]][location[1]] = mutation
                child_individual = objectfun(child, ratmatrix,user_num,rem_num)
                offspring.append(child_individual)
            else:
                continue
    return offspring














