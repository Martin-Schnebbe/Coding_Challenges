def getCount(inputStr):
    return sum(1 for i in inputStr if i in'aeiou')


print(getCount("abracadabra"))