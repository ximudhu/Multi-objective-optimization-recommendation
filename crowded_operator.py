def crowded_operator(individual1,individual2,object_num):
    if individual1[object_num + 1] < individual2[object_num + 1] or \
        individual1[object_num + 1] == individual2[object_num + 1] and individual1[object_num + 2] > individual2[object_num + 2]:
        return 1
    else:
        return 0