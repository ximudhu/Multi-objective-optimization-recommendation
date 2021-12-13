import matplotlib.pyplot as plt
#from scipy.interpolate import spline
from scipy.interpolate import make_interp_spline
import numpy as np
def Plot(temp_prc,temp_acc,object_num,Wtemp_prc,Wtemp_acc,label):#

    population_size = len(temp_acc)
    other_temp_prc = temp_prc.copy()
    other_temp_prc[:, 0] = temp_acc
    dominating = set ()
    for i in range (population_size):
        for j in range (population_size):
            less, more, equal = 0, 0, 0
            for k in range (object_num):
                if other_temp_prc[i][k] > other_temp_prc[j][k]:  # f(a) >= f(b),则a支配b
                    more += 1
                elif other_temp_prc[i][k] == other_temp_prc[j][k]:
                    equal += 1
                else:
                    less += 1
            if less == 0 and equal != object_num:  # j支配i，相应的np+1
                dominating.add (j)
            elif more == 0 and equal != object_num:  # i支配j,将q加入到Sp中
                dominating.add (i)
    dominating_accuracy = [other_temp_prc[i][0] for i in dominating]
    dominating_coverage = [other_temp_prc[i][1] for i in dominating]
    no_dominating_accuracy = [other_temp_prc[i][0] for i in range (population_size) if i not in dominating]
    no_dominating_coverage = [other_temp_prc[i][1] for i in range (population_size) if i not in dominating]
    plt.scatter (no_dominating_accuracy, no_dominating_coverage, c='b', marker='.')
    plt.scatter (dominating_accuracy, dominating_coverage, c='y', marker='<')

    other_Wtemp_prc = Wtemp_prc.copy()
    other_Wtemp_prc[:, 0] = Wtemp_acc
    Wdominating = set ()
    for i in range (population_size):
        for j in range (population_size):
            less, more, equal = 0, 0, 0
            for k in range (object_num):
                if other_Wtemp_prc[i][k] > other_Wtemp_prc[j][k]:  # f(a) >= f(b),则a支配b
                    more += 1
                elif other_Wtemp_prc[i][k] == other_Wtemp_prc[j][k]:
                    equal += 1
                else:
                    less += 1
            if less == 0 and equal != object_num:  # j支配i，相应的np+1
                Wdominating.add (j)
            elif more == 0 and equal != object_num:  # i支配j,将q加入到Sp中
                Wdominating.add (i)
    Wdominating_accuracy = [other_Wtemp_prc[i][0] for i in Wdominating]
    Wdominating_coverage = [other_Wtemp_prc[i][1] for i in Wdominating]
    Wno_dominating_accuracy = [other_Wtemp_prc[i][0] for i in range (population_size) if i not in Wdominating]
    Wno_dominating_coverage = [other_Wtemp_prc[i][1] for i in range (population_size) if i not in Wdominating]
    plt.scatter (Wno_dominating_accuracy, Wno_dominating_coverage, c='r', marker='.')
    plt.scatter (Wdominating_accuracy, Wdominating_coverage, c='g', marker='<')


    plt.legend (label, loc='lower left')
    plt.xlabel ("Accuracy")
    plt.ylabel ("Coverage")
    plt.show ()
    #plt.scatter (temp_prc[:,0] , temp_prc[:,1], c='r', marker='.')
    #plt.xlabel ("Predicted Rating")
    #plt.ylabel ("Coverage")
    #plt.subplot(133)
    #mean_hv,stdeviation = [],[]
    #for i in range(count):
        #mean_hv.append(np.mean(sum_hv[:,i]))
        #stdeviation.append(np.std(sum_hv[:,i]))
    #plt.xticks(range(0,3001,500))
    #plt.errorbar(range(0,3001,100), mean_hv, yerr=stdeviation, fmt='-o', ecolor='gray', color='black', elinewidth=1, capsize=2)
    #plt.xlabel("Generation")
    #plt.ylabel("Hypervolume")




