from math import *
import numpy as np
from itertools import product
#ProbS算法
def Probs(trainrating):
    [user_num,item_num] = trainrating.shape
    user_degree = {}.fromkeys([i for i in range(user_num)],0) #用户的度
    item_degree = {}.fromkeys([i for i in range(item_num)],0) #商品的度
    #计算user的度
    for k in user_degree.keys():
        user_degree[k] = len(np.nonzero(trainrating[k,:])[0])
    #计算item的度
    for k in item_degree.keys():
        item_degree[k] = len(np.nonzero(trainrating.T[k,:])[0])
    print('a')
    #第一步利用概率传播机制计算资源矩阵
    weight = np.zeros((item_num,item_num))
    for i,j in product(range(item_num),range(item_num)):
        w_sum = sum([trainrating[k][i] * trainrating[k][j] / user_degree[k] for k in range(user_num) if trainrating[k][i] and trainrating[k][j] and user_degree[k]])
        if item_degree[j]:
            weight[i][j] = round(w_sum/item_degree[j],6)
    print('b')
    #对weight数组中的nan元素进行处理
    #nan_location = isnan(weight)
    #weight[nan_location] = 0
    #第二步利用权重矩阵和训练数据集对每个用户对每一个item评分
    ratmatrix = np.array(np.mat(trainrating) * np.mat(weight).T)
    print('c')
    #np.savetxt ("file\\1.txt", ratmatrix)
    return ratmatrix

















