def sum_pairs(ls, target):
    sums = []
    for i in range(0,len(ls)):
        for j in range(1, len(ls)):
            if(i<j):
                if(ls[i]+ ls[j] == target):
                    sums.append([ls[i], ls[j]])

    if(len(sums) == 0):
        return("unable to find pairs")
    else:
        return sums