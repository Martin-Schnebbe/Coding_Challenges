def friend(x):
     return [i+'!' for i in x if len(i) == 4]

#return ((lambda i: print('hallo') if len(i)==4) for i in x)

print(friend(["Ryan", "Kieran", "Mark",]))