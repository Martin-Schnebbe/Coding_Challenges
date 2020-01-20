#My_solution
'''
def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        refurn ('')
    countList = []
    for category in listOfCat:
        sumCat = sum([int(i.split()[1]) for i in listOfArt if i[0] == category])
        cat = category
        countList.append(f"({cat} : {sumCat})")
    res = ' - '.join(countList)
    return res
'''
#Kata Solution
# #Combining counter with format and using generator expression

from collections import Counter

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)

listBooks = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
listCategories = ["A", "B"]

print(stock_list(listBooks, listCategories))

#, "(A : 200) - (B : 1140)")
# zählen alle mit a