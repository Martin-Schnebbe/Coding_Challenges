def is_isogram1(string):
    temp1 = string.lower()
    for i in temp1:
        if temp1.count(i) >=2:
            return False
    return True
#Kata verion
def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))


'''    temp2 = ''.join([i for i in temp1 if (not i.isdigit()) and (string.findall('i')<=1]))
    return temp2'''

print(is_isogram("Dermatoglyphics"))
print(is_isogram("isIsogram"))
print(is_isogram("mo0se"))
print(is_isogram("mose"))
