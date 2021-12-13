from tournament_selection import *
import numpy as np
import math
import heapq
def select_parent(population,object_num,tournament_size,a,b):
    temp1,temp2 = [],[]
    for i in range(a):
        temp1.append(tournament_selection(population,object_num,tournament_size))
    mean_object1 = np.mean(np.array(temp1)[:,object_num-1])
    mean_object2 = np.mean(np.array(temp1)[:,object_num])
    similiarity1 = [math.pow(indiv[object_num-1] - mean_object1,2) + math.pow(indiv[object_num] - mean_object2,2) for indiv in temp1]
    besta = temp1[similiarity1.index(max(similiarity1))]
    for i in range(b):
        individual = tournament_selection(population,object_num,tournament_size)
        while individual[object_num-1] == besta[object_num-1] and individual[object_num] == besta[object_num]:
            individual = tournament_selection(population, object_num, tournament_size)
        temp2.append(individual)
    similiarity2 = [math.pow(indiv[object_num-1] - besta[object_num-1],2) + math.pow(indiv[object_num] - besta[object_num],2) for indiv in temp2]
    bestb = temp2[similiarity2.index(min(similiarity2))]
    #print(similiarity)
    #si_index = sorted(range(b),key = lambda k :similiarity2[k])
    #bestb = temp2[similiarity2.index(min(similiarity2))]
    #min_similar = list(map(similiarity2.index,heapq.nsmallest(2,similiarity2)))
    #print(min_similar)
    #bestb = temp2[si_index[0]]
    #bestc = temp2[si_index[1]]
    #bestd = temp2[si_index[2]]
    return besta,bestb



