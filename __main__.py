from NSGA2 import *
from WNSGA2 import *
from WProbS import *
from WNSGA2_ProbS import *
from WNSGA2_init import *
from WNSGA2_cross import *

if __name__ == '__main__':
    start = time.time ()

    run_count = 1  #跑的次数记录
    population_size = 100  #种群大小
    object_num = 2
    rem_length = 10  #推荐列表长度
    gmax = 3000  #迭代次数 运行到3000代为止
    pm = 1 / rem_length  #变异概率
    pc = 0.8  #交叉概率
    filepath = 'D:\\E11514024_江婉榕_毕业设计\\E11514024_江婉榕_毕业设计成果\\file\\movielens1.dat'
    trainrating, wtrainrating, proberating, temp_predictedlist,predictedlist = loadData (filepath)  # 读入文件，加载数据
    print (1)
    ratmatrix = Probs (trainrating)  # probs算法，得到评分矩阵
    print (2)


    sum_result, Wsum_result, sum_result_probs, sum_result_init, sum_result_cross = [], [], [], [], []
    sum_accuacy, Wsum_accuacy, sum_accuacy_probs, sum_accuacy_init, sum_accuacy_cross = [], [], [], [], []
    sum_hv, Wsum_hv, sum_hv_probs, sum_hv_init, sum_hv_cross = [], [], [], [], []
    max_hv, Wmax_hv, max_hv_probs, max_hv_init, max_hv_cross = [], [], [], [], []

    for k in range (run_count):
        hv, result, accuacy, gen = NSGA2 (ratmatrix,temp_predictedlist,proberating,object_num,population_size,rem_length,gmax,pc,pm)
        sum_result.append (result)
        sum_accuacy.append (accuacy)
        sum_hv.append (hv)
        max_hv.append (hv[len (hv) - 1])
    max_index = max_hv.index (max (max_hv))
    hv = sum_hv[max_index]
    temp_prc = sum_result[max_index]  # 数组
    temp_acc = sum_accuacy[max_index]  # 列表

    wratmatrix = WProbs (trainrating)
    for k in range (run_count):
        Whv, Wresult, Waccuacy, Wgen, initpopulation,population1 = WNSGA2(predictedlist,wtrainrating,ratmatrix, wratmatrix, proberating, object_num,population_size, rem_length,gmax, pc, pm)
        Wsum_result.append (Wresult)
        Wsum_accuacy.append (Waccuacy)
        Wsum_hv.append (Whv)
        Wmax_hv.append (Whv[len (Whv) - 1])
    Wmax_index = Wmax_hv.index (max (Wmax_hv))
    Whv = Wsum_hv[Wmax_index]
    Wtemp_prc = Wsum_result[Wmax_index]  # 数组
    Wtemp_acc = Wsum_accuacy[Wmax_index]  # 列表

    plt.scatter (Wtemp_prc[:, 0], Wtemp_prc[:, 1], c='r', marker='.')
    plt.scatter (temp_prc[:, 0], temp_prc[:, 1], c='b', marker='.')
    plt.legend (['MOEA-WProbS', 'MOEA-ProbS'], loc='upper right')
    plt.xlabel ("Predicted Rating")
    plt.ylabel ("Coverage")
    plt.show ()

    plt.figure (figsize=(9, 4))
    plt.subplot (121)
    plt.plot (range (100, gmax + 1, 100), hv, 'g.-')
    plt.title ('MOEA-ProbS')
    # generation = [50 * (k + 1) for k in range (gen // 50)]
    # generation.append (gen)
    # plt.legend (['MOEA-WProbS', 'MOEA-ProbS'], loc='lower right')
    # plt.yticks(np.arange(floor(hv[0]),ceil(Whv[len(Whv) - 1]),0.1))
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")
    plt.subplot (122)
    plt.plot (range (100, gmax + 1, 100), Whv, 'r.-')
    plt.title ('MOEA-WProbS')
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")
    plt.show ()

    #plt.plot (range (100, gmax + 1, 100), hv, 'g.-')
    #plt.plot (range (100, gmax + 1, 100), Whv, 'r.-')
    #plt.yticks(np.arange(hv[0],Whv[len(Whv)-1],0.008))
    #plt.legend (['MOEA-WProbS', 'MOEA-ProbS'], loc='center right')
    #plt.xlabel ("Generation")
    #plt.ylabel ("Hypervolume")
    #plt.show()

    Plot (temp_prc, temp_acc, object_num, Wtemp_prc, Wtemp_acc, ["MOEA-Probs_Non_Dominated", "MOEA-Probs_Dominated","MOEA-WProbs_Non_Dominated", "MOEA-WProbs_Dominated"])

    #Plot (temp_prc, temp_acc, object_num, Wtemp_prc, Wtemp_acc, ['MOEA-ProbS', 'MOEA-WProbS'])

    for k in range (run_count):
        hv_probs, result_probs, accuacy_probs, gen_probs = WNSGA2_ProbS(predictedlist, trainrating, ratmatrix,proberating, object_num, population_size,rem_length,gmax, pc, pm,population1)
        sum_result_probs.append (result_probs)
        sum_accuacy_probs.append (accuacy_probs)
        sum_hv_probs.append (hv_probs)
        max_hv_probs.append (hv_probs[len (hv_probs) - 1])
    max_index_probs = max_hv_probs.index (max (max_hv_probs))
    hv_probs = sum_hv_probs[max_index_probs]
    temp_prc_probs = sum_result_probs[max_index_probs]  # 数组
    temp_acc_probs = sum_accuacy_probs[max_index_probs]  # 列表

    plt.scatter (Wtemp_prc[:, 0], Wtemp_prc[:, 1], c='r', marker='.')
    plt.scatter (temp_prc_probs[:, 0], temp_prc_probs[:, 1], c='b', marker='.')
    plt.legend (['MOEA-WProbS', 'MOEA-WProbS(-WProbS)'], loc='upper right')
    plt.xlabel ("Predicted Rating")
    plt.ylabel ("Coverage")
    plt.show ()

    # generation = [5 * (k + 1) for k in range (Wgen // 50)]
    # generation.append (Wgen)
    plt.figure (figsize=(9, 4))
    plt.subplot (121)
    plt.plot (range(100,gmax+1,100), hv_probs, 'g.-')
    plt.title ('MOEA-WProbS(-WProbS)')
    # generation = [50 * (k + 1) for k in range (gen // 50)]
    # generation.append (gen)
    # plt.legend (['MOEA-WProbS', 'MOEA-ProbS'], loc='lower right')
    # plt.yticks(np.arange(floor(hv[0]),ceil(Whv[len(Whv) - 1]),0.1))
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")
    plt.subplot (122)
    plt.plot (range(100,gmax+1,100), Whv, 'r.-')
    plt.title ('MOEA-WProbS')
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")
    plt.show ()

    Plot(temp_prc_probs, temp_acc_probs, object_num, Wtemp_prc, Wtemp_acc,["MOEA-WProbs(-WProbS)_Non_Dominated", "MOEA-WProbs(-WProbS)_Dominated", "MOEA-WProbs_Non_Dominated", "MOEA-WProbs_Dominated"])

    for k in range (run_count):
        hv_init, result_init, accuacy_init, gen_init = WNSGA2_init(predictedlist, trainrating, wratmatrix, proberating,object_num, population_size, rem_length, gmax,pc, pm)
        sum_result_init.append (result_init)
        sum_accuacy_init.append (accuacy_init)
        sum_hv_init.append (hv_init)
        max_hv_init.append (hv_init[len (hv_init) - 1])
    max_index_init = max_hv_init.index (max (max_hv_init))
    hv_init = sum_hv_init[max_index_init]
    temp_prc_init = sum_result_init[max_index_init]  # 数组
    temp_acc_init = sum_accuacy_init[max_index_init]  # 列表

    plt.scatter (Wtemp_prc[:, 0], Wtemp_prc[:, 1], c='r', marker='.')
    plt.scatter (temp_prc_init[:, 0], temp_prc_init[:, 1], c='b', marker='.')
    plt.legend (['MOEA-WProbS', 'MOEA-WProbS(-init)'], loc='upper right')
    plt.xlabel ("Predicted Rating")
    plt.ylabel ("Coverage")
    plt.show ()


    # generation = [5 * (k + 1) for k in range (Wgen // 50)]
    # generation.append (Wgen)
    plt.figure (figsize=(9, 4))
    plt.subplot (121)
    plt.plot (range(100,gmax+1,100), hv_init, 'g.-')
    plt.title ('MOEA-WProbS(-init)')
    # generation = [50 * (k + 1) for k in range (gen // 50)]
    # generation.append (gen)
    # plt.legend (['MOEA-WProbS', 'MOEA-ProbS'], loc='lower right')
    # plt.yticks(np.arange(floor(hv[0]),ceil(Whv[len(Whv) - 1]),0.1))
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")

    plt.subplot (122)
    plt.plot (range(100,gmax+1,100), Whv, 'r.-')
    plt.title ('MOEA-WProbS')
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")

    plt.show ()

    Plot (temp_prc_init, temp_acc_init, object_num, Wtemp_prc, Wtemp_acc, ["MOEA-WProbs(-init)_Non_Dominated", "MOEA-WProbs(-init)_Dominated", "MOEA-WProbs_Non_Dominated", "MOEA-WProbs_Dominated"])

    for k in range (run_count):
        hv_cross, result_cross, accuacy_cross, gen_cross = WNSGA2_cross (predictedlist, trainrating, wratmatrix,proberating, object_num, population_size,rem_length,gmax, pc, pm, initpopulation)
        sum_result_cross.append (result_cross)
        sum_accuacy_cross.append (accuacy_cross)
        sum_hv_cross.append (hv_cross)
        max_hv_cross.append (hv_cross[len (hv_cross) - 1])
    max_index_cross = max_hv_cross.index (max (max_hv_cross))
    hv_cross = sum_hv_cross[max_index_cross]
    temp_prc_cross = sum_result_cross[max_index_cross]  # 数组
    temp_acc_cross = sum_accuacy_cross[max_index_cross]  # 列表

    plt.scatter (Wtemp_prc[:, 0], Wtemp_prc[:, 1], c='r', marker='.')
    plt.scatter (temp_prc_cross[:, 0], temp_prc_cross[:, 1], c='b', marker='.')
    plt.legend (['MOEA-WProbS', 'MOEA-WProbS(-cross)'], loc='upper right')
    plt.xlabel ("Predicted Rating")
    plt.ylabel ("Coverage")
    plt.show ()


    # generation = [5 * (k + 1) for k in range (Wgen // 50)]
    # generation.append (Wgen)
    plt.figure (figsize=(9, 4))
    plt.subplot (121)
    plt.plot (range(100,gmax+1,100), hv_cross, 'g.-')
    plt.title ('MOEA-WProbS(-cross)')
    # generation = [50 * (k + 1) for k in range (gen // 50)]
    # generation.append (gen)
    # plt.legend (['MOEA-WProbS', 'MOEA-ProbS'], loc='lower right')
    # plt.yticks(np.arange(floor(hv[0]),ceil(Whv[len(Whv) - 1]),0.1))
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")

    plt.subplot (122)
    plt.plot (range(100,gmax+1,100), Whv, 'r.-')
    plt.title ('MOEA-WProbS')
    plt.xlabel ("Generation")
    plt.ylabel ("Hypervolume")

    plt.show ()

    Plot (temp_prc_cross, temp_acc_cross, object_num, Wtemp_prc, Wtemp_acc, ["MOEA-WProbs(-cross)_Non_Dominated", "MOEA-WProbs(-cross)_Dominated", "MOEA-WProbs_Non_Dominated", "MOEA-WProbs_Dominated"])

    end = time.time ()
    print (end - start)