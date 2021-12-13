import random
from crowded_operator import *
#选择适合繁殖的个体
def tournament_selection(population,object_num,tournament_size):#基于非支配排序和拥挤度
    best = None
    parent = random.sample(population,tournament_size) #随机选取竞赛选手
    for k in parent:
        if best == None or crowded_operator(k,best,object_num):
            best = k
    return best




