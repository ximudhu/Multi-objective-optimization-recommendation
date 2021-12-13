from itertools import product
from numba import jit
#@jit
def objectfun(individual,ratmatrix,user_num,rem_num):
    #ratmatrix:评分矩阵
    coverlist = set()
    #[user_num,rem_num] = np.shape(individual) #individual是数组
    item_num = ratmatrix.shape[1]
    sum_rating = 0.0
    for i in range(user_num):
        for j in range(rem_num):
            item = int(individual[i][j])
            sum_rating += ratmatrix[i][item]
            coverlist.add(item)# 计算不同类型的物品数量
    predicted_rating = round(sum_rating / (user_num * rem_num), 6)
    coverage = round(len(coverlist) / item_num,6)
    temp = [individual,predicted_rating,coverage]
    return temp