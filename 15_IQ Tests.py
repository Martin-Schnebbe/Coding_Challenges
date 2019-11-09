#my verion1
def iq_test1(numbers):
    res = [i for i in numbers.split(' ') if int(i) %2  == 0]
    if res.len() > 1:
        return
    return res

#my version2
def iq_test2(numbers):
    res = {int(i):lambda i:'even' if int(i) % 2 == 0 else 'odd' for i in numbers.split(' ')}
    return res

#my verion3
def iq_test3(numbers):
    res = {int(i):int(i)%2 for i in numbers.split(' ')}

#my verion4
def iq_test4(numbers):
    res = [i for i in numbers.split(' ') if int(i) %2  == 0]
    if len(res) == 1:
        return res[0]
    else:
        return [i for i in numbers.split(' ') if i not in res]

#my version5
def iq_test5(numbers):
    res1 = [int(i) for i in numbers.split(' ')]
    res2 = [int(i) for i in numbers.split(' ') if int(i) %2  == 0]
    res3 = [i for i in res1 if i not in res2]
    return res1,res2,res3

#kata version
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

print(iq_test("2 4 7 8 10"))