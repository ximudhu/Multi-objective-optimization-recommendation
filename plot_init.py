import matplotlib.pyplot as plt
from scipy.interpolate import spline
import numpy as np
def Plot_init(temp_prc,temp_acc,pre_temp_prc,pre_temp_acc,object_num,Wtemp_prc,Wtemp_acc,titl):

    plt.figure(figsize=(14,4))
    plt.subplot(131)
    population_size = len (temp_acc)
    temp_prc[:, 0] = temp_acc
    dominating = set ()
    for i in range (population_size):
        for j in range (population_size):
            less, more, equal = 0, 0, 0
            for k in range (object_num):
                if temp_prc[i][k] > temp_prc[j][k]:  # f(a) >= f(b),则a支配b
                    more += 1
                elif temp_prc[i][k] == temp_prc[j][k]:
                    equal += 1
                else:
                    less += 1
            if less == 0 and equal != object_num:  # j支配i，相应的np+1
                dominating.add (j)
            elif more == 0 and equal != object_num:  # i支配j,将q加入到Sp中
                dominating.add (i)
    dominating_accuracy = [temp_prc[i][0] for i in dominating]
    dominating_coverage = [temp_prc[i][1] for i in dominating]
    no_dominating_accuracy = [temp_prc[i][0] for i in range (population_size) if i not in dominating]
    no_dominating_coverage = [temp_prc[i][1] for i in range (population_size) if i not in dominating]
    plt.scatter (no_dominating_accuracy, no_dominating_coverage, c='b', marker='.')
    plt.scatter (dominating_accuracy, dominating_coverage, c='g', marker='<')
    label = ["Non_Dominated", "Dominated"]
    plt.legend (label, loc='upper right')
    plt.xlabel("Accuracy")
    plt.ylabel ("Coverage")
    plt.title (titl[0])
    #plt.scatter (temp_prc[:,0] , temp_prc[:,1], c='r', marker='.')
    #plt.xlabel ("Predicted Rating")
    #plt.ylabel ("Coverage")

    plt.subplot (132)
    population_size = len (pre_temp_acc)
    pre_temp_prc[:, 0] = pre_temp_acc
    dominating = set ()
    for i in range (population_size):
        for j in range (population_size):
            less, more, equal = 0, 0, 0
            for k in range (object_num):
                if pre_temp_prc[i][k] > pre_temp_prc[j][k]:  # f(a) >= f(b),则a支配b
                    more += 1
                elif pre_temp_prc[i][k] == pre_temp_prc[j][k]:
                    equal += 1
                else:
                    less += 1
            if less == 0 and equal != object_num:  # j支配i，相应的np+1
                dominating.add (j)
            elif more == 0 and equal != object_num:  # i支配j,将q加入到Sp中
                dominating.add (i)
    dominating_accuracy = [pre_temp_prc[i][0] for i in dominating]
    dominating_coverage = [pre_temp_prc[i][1] for i in dominating]
    no_dominating_accuracy = [pre_temp_prc[i][0] for i in range (population_size) if i not in dominating]
    no_dominating_coverage = [pre_temp_prc[i][1] for i in range (population_size) if i not in dominating]
    plt.scatter (no_dominating_accuracy, no_dominating_coverage, c='r', marker='.')
    plt.scatter (dominating_accuracy, dominating_coverage, c='g', marker='<')
    label = ["Non_Dominated", "Dominated"]
    plt.legend (label, loc='upper right')
    plt.xlabel ("Accuracy")
    plt.ylabel ("Coverage")
    plt.title (titl[1])

    plt.subplot (133)
    population_size = len (Wtemp_acc)
    Wtemp_prc[:, 0] = Wtemp_acc
    Wdominating = set ()
    for i in range (population_size):
        for j in range (population_size):
            less, more, equal = 0, 0, 0
            for k in range (object_num):
                if Wtemp_prc[i][k] > Wtemp_prc[j][k]:  # f(a) >= f(b),则a支配b
                    more += 1
                elif Wtemp_prc[i][k] == Wtemp_prc[j][k]:
                    equal += 1
                else:
                    less += 1
            if less == 0 and equal != object_num:  # j支配i，相应的np+1
                Wdominating.add (j)
            elif more == 0 and equal != object_num:  # i支配j,将q加入到Sp中
                Wdominating.add (i)
    Wdominating_accuracy = [Wtemp_prc[i][0] for i in Wdominating]
    Wdominating_coverage = [Wtemp_prc[i][1] for i in Wdominating]
    Wno_dominating_accuracy = [Wtemp_prc[i][0] for i in range (population_size) if i not in Wdominating]
    Wno_dominating_coverage = [Wtemp_prc[i][1] for i in range (population_size) if i not in Wdominating]
    plt.scatter (Wno_dominating_accuracy, Wno_dominating_coverage, c='r', marker='.')
    plt.scatter (Wdominating_accuracy, Wdominating_coverage, c='b', marker='<')
    label = ["Non_Dominated", "Dominated"]
    plt.legend (label, loc='upper right')

    plt.xlabel ("Accuracy")
    plt.ylabel ("Coverage")
    plt.title (titl[2])

    plt.show()
    #plt.subplot(133)
    #mean_hv,stdeviation = [],[]
    #for i in range(count):
        #mean_hv.append(np.mean(sum_hv[:,i]))
        #stdeviation.append(np.std(sum_hv[:,i]))
    #plt.xticks(range(0,3001,500))
    #plt.errorbar(range(0,3001,100), mean_hv, yerr=stdeviation, fmt='-o', ecolor='gray', color='black', elinewidth=1, capsize=2)
    #plt.xlabel("Generation")
    #plt.ylabel("Hypervolume")




