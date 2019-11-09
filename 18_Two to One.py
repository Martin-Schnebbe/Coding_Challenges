
# my version1
def longest1(s1, s2):
    res_s1 = ''.join(sorted(set(i for i in s1)))
    res_s2 = ''.join(sorted(set(i for i in s2)))
    return res_s1,res_s2

#my version2
def longest2(s1, s2):
    return (''.join(sorted(set(i for i in s1))) if  len(''.join(sorted(set(i for i in s1)))) >= len(''.join(sorted(set(i for i in s2))))  else ''.join(sorted(set(i for i in s2)))   )

#my version3 - error! task : combined set
def longest3(s1, s2):
    res_s1 = ''.join(sorted(set(i for i in s1)))
    res_s2 = ''.join(sorted(set(i for i in s2)))
    return set(res_s1 + res_s2)

#my version4
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))


print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
print(longest("inmanylanguages", "theresapairoffunctions"))