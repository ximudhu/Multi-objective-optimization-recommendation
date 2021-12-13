import numpy as np

#ProbS算法
def WProbs(trainrating):
    [user_num,item_num] = trainrating.shape
    #第一步将电影的资源分配给用户
    temp_user = np.zeros((user_num,user_num))
    for i in range(user_num):#目标用户
        for j in range(item_num):
            if trainrating[i][j] > 0 :
                temp_weight = np.zeros((1,user_num))
                location = np.where(trainrating.T[j] > 0)
                non_index = location[0]
                #！！item_allocation = [5 - abs(trainrating[i][j] - trainrating[k][j]) for k in non_index]
                #！！weight_value = 1 / sum(item_allocation)
                #错误
                #item_allocation = [2 - abs(trainrating[i][j] - trainrating[k][j] for k in non_index)]  #形成【-2，-1， 0， 1， 2】
                #TypeError: bad operand type for abs(): 'generator'
                #正确的为：
                item_allocation = [2 - abs(trainrating[i][j] - trainrating[k][j]) for k in non_index]  # 形成【-2，-1， 0， 1， 2】
                weight_value = 1/sum(abs(i) for i in item_allocation)  #分母是绝对值之和
                temp_weight[0][location] = np.array(item_allocation) * weight_value
                temp_user[i] = temp_user[i] + temp_weight
        #print([max(temp_user[i]),min(temp_user[i])])
    print('a')
    #第二步将用户资源分配给项目
    temp_weight = np.zeros ((user_num, item_num))
    for i in range(user_num):
        location = np.where(trainrating[i] > 0)
        non_index = location[0]
        user_allocation = [trainrating[i][loc] for loc in non_index]#分配权重
        weight_value = 1 / sum(user_allocation)
        temp_weight[i][location] = np.array(user_allocation) * weight_value#得到的权重
    #得到评分矩阵
    ratmatrix = np.array(np.mat(temp_user) * np.mat(temp_weight))
    print('b')
    #对weight数组中的nan元素进行处理
    #nan_location = isnan(weight)
    #weight[nan_location] = 0
    #第二步利用权重矩阵和训练数据集对每个用户对每一个item评分
    #ratmatrix = np.array(np.mat(trainrating) * np.mat(weight).T)
    print('c')
    #np.savetxt ("file\\1.txt", ratmatrix)
    return ratmatrix

















