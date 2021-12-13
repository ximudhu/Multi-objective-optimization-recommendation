from math import *
from itertools import islice
import pickle
import os
import csv
import numpy as np
import random as rd

class Kmeans:
    #初始化
    def __init__(self,filepath,n_clusters,user_num,item_num):
        self.filepath = filepath  #导入文件路径
        self.n_clusters = n_clusters  #聚类中心的数目
        self.user_num = user_num      #用户数目
        self.item_num = item_num    # 商品数目
        self.ratingset = self.loadData()  #获取评分矩阵
        self.cluscenter = self.initcenter()  #初始化聚类中心
        self.clus_user,self.clus_rating = self.kmeans()

    #获取评分矩阵
    def loadData(self):
        ratingset = np.zeros((self.user_num,self.item_num))
        #f = csv.reader(open(self.filepath,'r'))
        f = open(self.filepath,'r')
        for eachline in f.readlines():
            curline = eachline.strip().split("\t")  #将每一行分隔分割为几部分
            ratingset[int(curline[0]) - 1][int(curline[1]) - 1] = int(curline[2])
        #for eachline in islice(f,1,None):
            #ratingset[int(eachline[0]) - 1][int(eachline[1]) - 1] = float(eachline[2])
        return ratingset

    #初始化聚类中心，选取评分数量最多的k个user作为初始聚类中心
    def initcenter(self):
        cluscenter = {}  #存放初始聚类中心
        #usercount = {}
        center = rd.sample(range(self.user_num),self.n_clusters)
        #for i in range(self.user_num):
            #usercount[i] = len(nonzero(self.ratingset[i,:])[0])  #计算非零个数
        #usercount = sorted(usercount.items(),key = lambda x:x[1],reverse = True)  #按键的值进行排序,返回一个列表
        for user in center:
            cluscenter[user] = self.ratingset[user,:]
        #for user in usercount[:self.n_clusters]:
            #cluscenter[user[0]] = self.ratingset[user[0], :]
        return cluscenter

    #计算余弦相似度
    def similarity(self,user_id,center_id):
        molecuter = 0.0  #分母
        denominater1 = 0.0
        denominater2 = 0.0
        for i in range(self.item_num):
            molecuter += self.ratingset[user_id][i]*self.cluscenter[center_id][i]
            if self.ratingset[user_id][i]:
                denominater1 += self.ratingset[user_id][i] ** 2
            if self.cluscenter[center_id][i]:
                denominater2 += self.cluscenter[center_id][i] ** 2
        return molecuter/(sqrt(denominater1)*sqrt(denominater2))

    #k-means聚类函数
    def kmeans(self):
        flag = True   #聚类中心改变标志，若为True，继续迭代
        while flag:
            clus_user = {}  # 簇类集，存放每类的用户id
            clus_rating = {}  # 簇类集，存放每类的打分
            for user_id in range(self.user_num):
                maxcosline = -inf
                cluster_id = -1
                #clusteru = {}  # 存放每个用户的评价情况
                for center_id in self.cluscenter.keys():
                    cosline = self.similarity(user_id,center_id)
                    if cosline > maxcosline:  #选择余弦值最大，即相似度最大的分到一类中
                        maxcosline = cosline
                        cluster_id = center_id
                clus_user.setdefault(cluster_id,[]).append(user_id)   #存放每类中的用户
                clus_rating.setdefault(cluster_id,[]).append(self.ratingset[user_id,:])  #存放每类中的评分矩阵
            #更新簇类中心
            new_cluscenter = {}  # 存放更新的聚类中心
            for cluster_id in clus_rating.keys():
                for i in range(self.item_num):
                    #print(sum(np.mat(clus_rating[cluster_id]).T[i]))
                    new_cluscenter.setdefault(cluster_id,[]).append(sum(np.array(clus_rating[cluster_id]).T[i])/np.size(np.array(clus_rating[cluster_id]).T[i]))
                #new_cluscenter[cluster_id] = np.array(new_cluscenter[cluster_id])
            for newclus_id in new_cluscenter.keys():
                if (self.cluscenter[newclus_id]-new_cluscenter[newclus_id]).all(): #若都不为零，则更新
                    self.cluscenter = new_cluscenter
                    flag = True
                    break
                else:
                    flag = False
        return clus_user,clus_rating

    #保存结果
    def save(self):
        if os.path.exists('file\\Ratingset.dat'):
            os.remove('file\\Ratingset.dat')
        pickle.dump(self.ratingset,open('file\\Ratingset.dat','wb'))

        i=1
        for k in self.clus_rating.keys():
            string = 'movielens'+ str(i+4)
            if os.path.exists('file\\'+string +'.dat'):
                os.remove('file\\'+string +'.dat')
            pickle.dump(self.clus_rating[k],open('file\\'+string +'.dat','wb'))
            i+=1
        return 1

if __name__ == '__main__':
            k_means = Kmeans('file\\u.data',n_clusters = 4,user_num = 943,item_num = 1682)
            print(k_means.ratingset)
            k_means.save()
            print("分类情况为：")
            for key in k_means.clus_user.keys():
                print(len(k_means.clus_user[key]))
            print ('cluster over!')





















