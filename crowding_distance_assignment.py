import numpy as np
def crowding_distance_assignment(population,object_num):#某一前沿面的非支配排序
    for individual in population:
        individual.append(0)  #初始化每个个体拥挤距离为0
    size = len(population)
    location = object_num + 2  # 拥挤距离存放的位置
    temp_population = population
    for k in range(object_num):
        temp_population = sorted(temp_population,key = lambda x:x[k+1])  #按照目标函数大小排序
        fmin = temp_population[0][k+1]   #目标函数最小值
        fmax = temp_population[size-1][k+1]  #目标函数最大值
        temp_population[0][location] = np.inf #排序后第一个个体和最后一个个体的拥挤距离设为无穷大
        temp_population[size-1][location] = np.inf
        for n in range(1,size-1):
            if fmax - fmin == 0:
                temp_population[n][location] = np.inf
            else:
                temp_population[n][location] = temp_population[n][location] + \
                                                           round((temp_population[n+1][k+1] - temp_population[n-1][k+1])/(fmax - fmin),6)
     #返回包含等级和距离的矩阵，并按照等级进行了排序
    return temp_population