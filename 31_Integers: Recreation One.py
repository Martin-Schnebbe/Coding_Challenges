def list_squared(m, n):
    result = []
    for i in range(m,n+1):
        for y in range(1,i):
            if (i/y)%0:
                result.append(y)
    print(result)


list_squared(1,5)


#list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
#list_squared(42, 250), [[42, 2500], [246, 84100]])
#list_squared(250, 500), [[287, 84100]])
