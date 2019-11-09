#my version1
def get_middle1(s):
    if len(s)%2 ==0:
        res = s[int(len(s)/2)-1:int((len(s)/2)+1)]
    else: 
        res = s[int((len(s)/2))]
    return res

#my version2
def get_middle2(s):
    mid = int(len(s)/2)
    return s[mid-1:mid+1]

#my version3
def get_middle3(s):
    return s[int(len(s)/2)-1:int((len(s)/2)+1)] if len(s)%2 ==0 else s[int((len(s)/2))]

#kata version
def get_middle(s):
   return s[int((len(s)-1)/2):int(len(s)/2+1)]

print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
