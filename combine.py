list1 = [11,22,33]
list2 = [1,2,3]
def combine(list1, list2):
    
    lst = []
    len1 = len(list1)
    len2 = len(list2)

    for index in range( max(len1, len2) ):
        if index+1 <= len1:
            lst += [list1[index]]

        if index+1 <= len2:
            lst += [list2[index]]

    return lst
    
print(combine(list1, list2))
