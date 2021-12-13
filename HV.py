from math import *

def cal_hypervolume(population,object_num):
    temp_population = [individual for individual in population if individual[object_num + 1] == 1]
    temp_population = sorted(temp_population,key = lambda x:x[1])
    population_size = len(temp_population)
    hv = 0.0
    for i in range(population_size):
        if i == 0:
            hv = temp_population[i][1] * temp_population[i][2]  #参考点为原点
        else:
            hv += temp_population[i][2] * abs(temp_population[i][1]-temp_population[i-1][1])
    return hv




