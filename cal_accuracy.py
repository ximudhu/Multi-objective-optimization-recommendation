from numpy import *
def cal_accuracy(population,proberating,object_num):
    #计算精确度
    accuracy = []
    individual = [indiv[0] for indiv in  population if indiv[object_num+1] == 1]
    [user_num, rem_length] = shape(individual[0])
    for single in individual:
        hit_num = 0
        for i in range(user_num):
            for j in range(rem_length):
                if proberating[i][int(single[i][j])] :
                    hit_num += 1
        mean_accuracy = round(hit_num/(rem_length * user_num),6)
        accuracy.append(mean_accuracy)
    return accuracy