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

print(sum_pairs([1, 2, 3, 4, 5], 9))
print(sum_pairs([1,2,3,4,5], 7))
print(sum_pairs([3, 1, 5, 8, 2], 27))