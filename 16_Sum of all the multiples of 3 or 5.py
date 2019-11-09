#my version1
def find1(n):
    res3 = [i*3 for i in range(n) if 3*i<=n]
    res5 = [i*5 for i in range(n) if 5*i<=n]
    return sum(set(res3+res5))

#my version2 incl. kata (no use of set() -> incl. if statement at second list)
def find2(n):
    res3 = [i*3 for i in range(n) if 3*i<=n]
    res5 = [i*5 for i in range(n) if 5*i<=n if (i*5) % 3 !=0]
    return sum(res3+res5)

#kata version
def find(n):
    return sum(e for e in range(1, n+1) if e % 3 == 0 or e % 5 == 0)


print(find(15))