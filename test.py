def is_isogram(string):
    temp1 = set(string)
    return temp1

'''    temp2 = ''.join([i for i in temp1 if (not i.isdigit()) and (string.findall('i')<=1]))
    return temp2'''

print(is_isogram("aaaccceee"))
print(is_isogram("AaaBbbCcc"))
print(is_isogram("mo0se"))
print(is_isogram("mose"))