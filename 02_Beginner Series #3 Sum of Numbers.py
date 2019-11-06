
#Version 1
'''
def get_sum(a,b):
    if a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a

    return sum(range(smaller,bigger+1))
'''

#Version 2
def get_sum(a,b):
    return sum(range( min(a,b), max(a,b)+1))

print (get_sum(1,5))