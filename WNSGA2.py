from loadData import *
from Probs import *
from init_population import *
from fast_non_dominated_sort import *
from tournament_selection import *
from Winit_population import *
from genetic_operator import *
from elitism import *
from cal_accuracy import *
from HV import *
from plot import *
import time
import numpy as np
import matplotlib.pyplot as plt
from Wgenetic_operator import *
from objectfun import *
from Winit_population import *
from WWinit_population import *
from _pydecimal import Decimal,Context,ROUND_HALF_UP
def WNSGA2(predictedlist, wtrainrating,ratmatrix,wratmatrix, proberating, object_num,population_size, rem_length,gmax, pc, pm):#trainrating
    #object_num:目标函数
    #population_size：种群大小
    #rem_lengt：推荐长度
    #pc：交叉算子
    #gmax：最大迭代次数
    #pm = 1/rem_length         #变异算子
    #initpopulation,population1 = WWinit_population (population_size,wtrainrating,ratmatrix,wratmatrix,rem_length,predictedlist)
    #initpopulation,initpopulation1 = init_population(population_size, wratmatrix, predictedlist, rem_length)
    initpopulation,population1 = Winit_population (population_size,ratmatrix,wratmatrix,predictedlist,rem_length)
    #population = WWWinit_population (population_size, wratmatrix, predictedlist, rem_length)
    population,new_Front = fast_non_dominated_sort(initpopulation, object_num)
    print(4)
    #population = elitism(population, new_Front, object_num, population_size)
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
        if gen < 1000:
           a = b = 10
        else:
           a , b = 1,10
            #a = Context(prec=1,rounding=ROUND_HALF_UP).create_decimal(ratio * 10)
            #print(a)
            #a = b = 1 if a < 1 else a
            #b = Context(prec=1, rounding=ROUND_HALF_UP).create_decimal ('ratio * 10')
        #else:
            #a,b = 10,1
            #if ratio > 0 :#rgen < 300

        #elif 0.1 < ratio < 0.2:
            #a = b = int(Context(prec=1,rounding=ROUND_HALF_UP).create_decimal(ratio * 20))
        #elif 200 <= gen < 500:
            #a,b = 1,10
            #else:
                #a,b = 1,10
        offspring_population = Wgenetic_operator(population, pc, pm, wratmatrix, object_num, tournament_size,predictedlist,a,b)
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
        #if (gen+1) % 500 == 0:
           # Pareto1 = [[population[i][object_num - 1], population[i][object_num]] for i in range (population_size) if
                      # population[i][object_num + 1] == 1]
            #plt.scatter (np.array(Pareto1)[:,0],np.array(Pareto1)[:,1], c='r', marker='.')
            #plt.show()
            #plt.plot (range (100, gen + 2, 100), hypervolume, 'g.-')
            #plt.show()
        #pre_population = population
    #f3 = open ('file\\3.txt', 'w')
    #for i in range(population_size):
        #f3.write(str(population) + "\n")
    #f3.close()
    accuracy = cal_accuracy(population, proberating,object_num)
    print(population)
    Pareto1 = [[population[i][object_num-1],population[i][object_num]]for i in range(population_size) if population[i][object_num+1] == 1]
    result = np.zeros((len(Pareto1), object_num))
    result[:,0] = np.array(Pareto1)[:,0]
    result[:,1] = np.array(Pareto1)[:,1]

    return hypervolume,result,accuracy,gen,initpopulation,population1