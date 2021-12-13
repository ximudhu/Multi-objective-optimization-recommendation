
from fast_non_dominated_sort import *

from elitism import *
from cal_accuracy import *
from HV import *
from objectfun import *
from plot import *
import time
import numpy as np
import matplotlib.pyplot as plt
from genetic_operator import *
from Winit_population import *
from _pydecimal import Decimal,Context,ROUND_HALF_UP
def WNSGA2_cross(predictedlist, trainrating,wratmatrix, proberating, object_num,population_size, rem_length, gmax,pc, pm,initpopulation):
    #object_num:目标函数
    #population_size：种群大小
    #rem_lengt：推荐长度
    #pc：交叉算子
    #gmax：最大迭代次数
    #pm = 1/rem_length         #变异算子
    population,new_Front = fast_non_dominated_sort(initpopulation, object_num)
    print(4)
    current = 0
    temp_population = []
    for i in range(len(new_Front) - 1):
        lgth = len(new_Front[i])
        temp = crowding_distance_assignment(population[current:current + lgth], object_num)
        current += lgth
        temp_population.extend (temp)
    population = temp_population
    hypervolume = []
    tournament_size = 2
    for gen in range(gmax):
        #if gen:
            #a = Context(prec=1,rounding=ROUND_HALF_UP).create_decimal(ratio * 10)
            #print(a)
            #a = b = 1 if a < 1 else a
            #b = Context(prec=1, rounding=ROUND_HALF_UP).create_decimal ('ratio * 10')
        #else:
            #a,b = 10,10
        offspring_population = genetic_operator(population, pc, pm, wratmatrix,object_num,tournament_size,predictedlist)
        combine_population = np.array(population)[:, :object_num + 1].tolist()
        combine_population.extend(offspring_population)  #合并子代和父代种群
        combine_population, Front = fast_non_dominated_sort (combine_population, object_num)  # 对新的种群进行非支配排序
        print(8)
        population = elitism(combine_population, Front, object_num,population_size)  # 选择合并种群的前population_size个个体组成新的种群
        print(9)
        print ("第%d代完成" % gen)
        no_Pareto = [i for i in range (population_size) if population[i][object_num + 1] != 1]
        ratio = len(no_Pareto)/population_size
        print(ratio)
        hv = cal_hypervolume (population, object_num)
        if (gen + 1) % 100 == 0:
            hypervolume.append(hv)
    #f3 = open ('file\\3.txt', 'w')
    #for i in range(population_size):
        #f3.write(str(population) + "\n")
    #f3.close()
    accuracy = cal_accuracy(population, proberating,object_num)
    Pareto1 = [[population[i][object_num-1],population[i][object_num]]for i in range(population_size) if population[i][object_num+1] == 1]
    result = np.zeros((len(Pareto1), object_num))
    result[:,0] = np.array(Pareto1)[:,0]
    result[:,1] = np.array(Pareto1)[:,1]
    return hypervolume,result,accuracy,gen