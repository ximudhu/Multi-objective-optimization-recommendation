from crowding_distance_assignment import *
import numpy as np
def elitism(combine_population,Front,object_num,population_size):
    new_population = []
    current_index = 0
    i = 0
    while len(new_population) + len(Front[i]) <= population_size:
        temp_list = crowding_distance_assignment(combine_population[current_index:current_index + len(Front[i])],object_num)  # 对种群进行拥挤度计算
        new_population.extend(temp_list)
        current_index += len(Front[i])
        i = i+1
    if population_size != len(new_population):
        remaining = population_size - len(new_population)
        temp_list = crowding_distance_assignment(combine_population[current_index:current_index + len(Front[i])],object_num)  # 对种群进行拥挤度计算
        remaining_list = sorted(temp_list,key=lambda x: x[object_num + 2], reverse=True)
        new_population.extend(remaining_list[:remaining])
    return new_population  # np.array(remaining_list)[:remaining,:object_num+2].tolist()
    # temp_list = crowding_distance_assignment(combine_population[current_index:current_index+length],object_num)# 对种群进行拥挤度计算








