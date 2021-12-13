from math import *
from numpy import *
import pickle
import random
import numpy as np
from itertools import product
#读入数据

def loadData(filepath):
    cluster = pickle.load(open(filepath,"rb"))
    cluster  = np.array(cluster)
    wcluster = cluster.copy()
    [user_num,item_num] = shape(cluster)
    print(user_num,item_num)
    cluslist = []  #存放评分为1的项
    #预处理数据，若评分大于等于3，则为1，否则为0
    for user_id in range(user_num):
        for item_id in range(item_num):
            if cluster[user_id][item_id] >= 3:
                cluslist.append([user_id,item_id,cluster[user_id][item_id]]) #把评分>=3的项存入cluslist
                cluster[user_id][item_id] = 1
            else:
                cluster[user_id][item_id] = 0
    #划分数据集为训练集和测试集
    trainrating = np.zeros((user_num,item_num))
    #temp_trainratig = trainrating.copy()
    trainingset = random.sample(cluslist,round(len(cluslist)*0.8)) #随机选取80%的数据作为训练集，其余作为测试集
    #!!!!!!!!!!!!!
    for item in trainingset:
        trainrating[item[0]][item[1]] = 1     #训练集评分矩阵
        #temp_trainratig[item[0]][item[1]] = item[2]
    proberating  = cluster - trainrating #测试集评分矩阵
    location = np.where(proberating > 0)
    wcluster[location] = 0
    wtrainrating = wcluster
    temp_predictedlist = [np.where(trainrating[i] == 0)[0].tolist() for i in range(user_num)]
    predictedlist = [np.where(wtrainrating[i] == 0)[0].tolist() for i in range(user_num)]
    return trainrating,wtrainrating,proberating,temp_predictedlist,predictedlist