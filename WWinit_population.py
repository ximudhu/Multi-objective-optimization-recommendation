import random
from math import *
from objectfun import *
import numpy as np
import matplotlib.pyplot as plt
from copy import *
#初始化种群
def WWinit_population(population_size,wtrainrating,ratmatrix,wratmatrix,rem_length,predictedlist):
    population,population1 = [],[]
    [user_num,item_num] = ratmatrix.shape
    N = round(sqrt(item_num * rem_length))
    location = np.nonzero(wtrainrating)
    ratmatrix[location] = -1000
    wratmatrix[location] = -1000
    temp_ratmatrix = [sorted(range(item_num),key = lambda m:ratmatrix[i][m],reverse=True)[:N] for i in range(user_num)]
    temp_wratmatrix = [sorted(range(item_num),key = lambda m:wratmatrix[i][m],reverse=True)[:N] for i in range(user_num)]
    #T = [0 for i in range(user_num)]
    #D = deepcopy(T)
    #for i in range(user_num):
        #com_location = [[j,temp_wratmatrix[i].index(temp_ratmatrix[i][j])] for j in range(N)]
        #D[i] = [temp_ratmatrix[i][location[0]] for location in com_location if (location[1] - location[0])]#排名落后
        #T[i] = [temp_ratmatrix[i][location[0]] for location in com_location if location[1] < location[0]] # 排名提前
        #candidate[i] = [k for k in range(item_num) if k not in T[i] and k not in D[i] and k not in np.nonzero(trainrating[i])[0]]
    jiao_set = [list(set (temp_ratmatrix[i]) & set (temp_wratmatrix[i])) for i in range(user_num)]
    cha_set = [list (set (temp_ratmatrix[i]) | set (temp_wratmatrix[i]) - set(jiao_set[i])) for i in range(user_num)]
        #set(temp_ratmatrix[i]).union(set(temp_wratmatrix[i]))
    bing_set = [list (set (temp_ratmatrix[i]) | set (temp_wratmatrix[i])) for i in range (user_num)]
    #nozero_list = [np.nonzero(trainrating[i])[0] for i in range(user_num)]
    #flag = [True if 0 <= len(T[i]) <= int(rem_length/2) and isinstance(T[i],list) else False for i in range(user_num)]
    temp_ratmatrix = np.zeros ((user_num, item_num))
    for i in range (user_num):
        rmax, rmin = max (wratmatrix[i]), min (wratmatrix[i])
        temp_ratmatrix[i] = [(rating - rmin) / (rmax - rmin) for rating in wratmatrix[i]]
    for i in range(population_size):
        #初始化个体
        if i < population_size - 1:
            individual = np.zeros((user_num,rem_length))
            for j in range(user_num):
                temp_list = []
                if len(jiao_set[j]) <= int(rem_length/2):
                    temp_list.extend(jiao_set[j])
                else:
                    temp_list.extend(random.sample(jiao_set[j],int(rem_length/2)))
            #candidate = [k for k in predictedlist[j] if k not in temp_list]
                if random.random() < 0.5:
                    temp_list.extend (random.sample (cha_set[j], rem_length-len(temp_list)))
                else:
                    candidate = [k for k in predictedlist[j] if k not in bing_set[j]]
                    temp_list.extend(random.sample (candidate, rem_length - len (temp_list)))
               # while len(temp_list) < rem_length:
                    #item_id = random.choice(predictedlist[j])
                   # while item_id in temp_list:
                       #item_id = random.choice (predictedlist[j])
                    #if random.random () < temp_ratmatrix[i][item_id]:
                        #temp_list.append (item_id)
                individual[j] = temp_list
            #candidate = [k for k in predictedlist[j] if k not in temp_list]
            #temp_list.extend(random.sample(candidate,rem_length - len(temp_list)))
        else:
            individual = np.array ([sorted (predictedlist[k], key=lambda m: wratmatrix[i][m], reverse=True)[:rem_length] for k in range (user_num)])
        #individual = np.array([random.sample(predictedlist[j], rem_length) for j in range(user_num)])  # 存放个体,随机选取电影编号
        temp_individual = objectfun(individual,wratmatrix,user_num,rem_length)
        temp_individual1 = objectfun (individual, ratmatrix, user_num, rem_length)
        population.append(temp_individual)
        population1.append (temp_individual1)
    return population,population1