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

# Big O == O(n) because hashmap only has to loop through the list once.
def hashmap_sum_pairs(ls, target):
    hashmap = {}
    sums = []

    # hash logic
    for i, n in enumerate(ls):
        diff = (target - n)
        if diff in hashmap:
            sums.append([diff, n])
            hashmap[n] = i
        else:
            hashmap[n] = i
            
    if len(sums) != 0:
        return sorted(sums)
    else:
        return("unable to find pairs")