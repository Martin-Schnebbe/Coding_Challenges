#My version
def array_diff2(a, b):

    match_res = [i for i in a if i in b]

    indices = [i for i,x in enumerate(a) if x in match_res]

    res = [x for i,x in enumerate(a) if i not in indices]

    return res

#Kata version
def array_diff(a, b):
    return [x for x in a if x not in b]


print(array_diff([1,2,1,3,4], [1,3]))

'''Approach 1
1. list all matching in a list
2. get indices which should be deleted
3. substract that list
'''