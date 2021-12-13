import random
import numpy as np
from itertools import product
from objectfun import *
from select_parent import *
from collections import Counter
from crowded_operator import *

def Wgenetic_operator1(population, pc, pm, wratmatrix, object_num, tournament_size,predictedlist,a,b):
    [user_num, rem_num] = population[0][0].shape
    population_size = len(population)
    offspring = []
    #item_num = wratmatrix.shape[1]
    #pool_size = int(population_size / 2)
    rand = np.random.random((1, population_size))[0]
    #item_list = [[k for k in range(item_num) if k not in D[i] and k not in nozero_list[i]] for i in range (user_num)]
    for n in range(population_size):
        parent1, parent2 = select_parent (population, object_num, tournament_size, a, b)
        parent3, parent4 = select_parent (population, object_num, tournament_size, a, b)
        if rand[n] < pc :
            parent1, parent2, parent3, parent4 = parent1[0], parent2[0], parent3[0], parent4[0]
            mu_child = np.zeros((user_num, rem_num))
            for i in range(user_num):
                #print(parent1[i],parent2[i])
                com_list = parent1[i].tolist() + parent2[i].tolist() + parent3[i].tolist() + parent4[i].tolist()
                com_count = Counter(com_list)
                count = [k for k in com_count.keys() if com_count[k] > 1]
                count1 = [k for k in com_count.keys() if com_count[k] == 1]
                if len(count) < rem_num:
                    temp_list = count
                    temp_list.extend(random.sample(count1,rem_num - len(count)))
                    #temp_list.append()
                    #temp_list.extend([k for k in count2 if k not in temp_list][:rem_num - len(temp_list)])
                    mu_child[i] = temp_list
                else:
                    mu_child[i] = random.sample(count,rem_num)#count[:rem_num]
        else:
            mu_child = random.choice([parent1[0],parent2[0],parent3[0],parent4[0]])
            #mu_child = random.choice([parent1, parent2])
        #mu_child = random.sample([child1, child2], 1)[0]
        child = mu_child.copy()
        mu_array = np.random.random((user_num, rem_num))
        mu_location = np.argwhere(mu_array < pm) #变异
        if len(mu_location):
            for location in mu_location:
                mutation = random.choice(predictedlist[location[0]])
                while mutation in mu_child[location[0]] or mutation in child[location[0]]:  # and letter < 1000:#防止卡死
                        mutation = random.choice(predictedlist[location[0]])
                child[location[0]][location[1]] = mutation
            child_individual = objectfun(child, wratmatrix,user_num,rem_num)
            offspring.append(child_individual)
        else:
            continue
    return  offspring