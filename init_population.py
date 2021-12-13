import random
from objectfun import *
import numpy as np
from objectfun import *
import matplotlib.pyplot as plt
#初始化种群
def init_population(population_size,ratmatrix,predictedlist,rem_length):
    population = []
    user_num = len(predictedlist)
    for i in range(population_size):
        #初始化个体
        if population_size < population_size - 1:
           individual = np.array([random.sample(predictedlist[j], rem_length) for j in range(user_num)])  # 存放个体,随机选取电影编号
        else:
           individual = np.array([sorted (predictedlist[k], key=lambda m: ratmatrix[i][m], reverse=True)[:rem_length] for k in range (user_num)])
        temp_individual = objectfun(individual, ratmatrix, user_num, rem_length)
        population.append(temp_individual)
    return population





