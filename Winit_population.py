import random
from objectfun import *
import numpy as np
import matplotlib.pyplot as plt
#初始化种群
def Winit_population(population_size,ratmatrix,wratmatrix,predictedlist,rem_length):
    population,population1 = [],[]
    [user_num,item_num] = wratmatrix.shape
    temp_ratmatrix = np.zeros((user_num,item_num))
    for i in range(user_num):
        rmax, rmin = max(wratmatrix[i]),min(wratmatrix[i])
        temp_ratmatrix[i] = [(rating - rmin)/(rmax - rmin) for rating in wratmatrix[i]]
    for i in range(population_size):
        #初始化个体
        if i < population_size-1:
            individual = np.zeros((user_num, rem_length))
            for j in range (user_num):
                rem_list = []
                while len (rem_list) < rem_length:
                    item_id = random.choice(predictedlist[j])
                    while item_id in rem_list:
                        item_id = random.choice(predictedlist[j])
                    if random.random () < temp_ratmatrix[i][item_id]:
                        rem_list.append(item_id)
                individual[j] = rem_list
        else:
            individual = np.array([sorted(predictedlist[k], key=lambda m: wratmatrix[i][m], reverse=True)[:rem_length] for k in range (user_num)])
            #individual = np.array([random.sample(predictedlist[j], rem_length) for j in range(user_num)])  # 存放个体,随机选取电影编号
        temp_individual1 = objectfun(individual,ratmatrix,user_num,rem_length)
        temp_individual = objectfun(individual,wratmatrix,user_num,rem_length)
        population.append(temp_individual)
        population1.append(temp_individual1)
    return population,population1