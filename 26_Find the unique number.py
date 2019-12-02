def find_uniq(arr):
    return list(set(arr))[0] if arr.count(list(set(arr))[0])==1 else list(set(arr))[1]




print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print(find_uniq([ 3, 10, 3, 3, 3 ]))