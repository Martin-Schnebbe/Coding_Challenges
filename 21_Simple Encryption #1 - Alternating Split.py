#my version1
'''def encrypt(text, n):
    return ''.join([x for i,x in enumerate(text) if i%2 ==n] + [x for i,x in enumerate(text) if i%2 ==0])

def decrypt(text, n):
    pass'''

#my version2
def encrypt2(text, n):
    liste = []
    for x in range(n,-1,-1):
        for i in text[::x]:
            print(i)
    return liste


#my version3
def encrypt3(text, n):
    liste = []
    for x in range(n,-1,-1):
        print(x)
    return liste

#my version4
def encrypt4(text, n):
    liste = []
    for x in range(n+1,0,-1):
        for i in text[x-1::n]:
            liste.append(i)
    return liste

def encrypt(text, n):
    liste =[]
    for x in range(2,0,-1):
        for i in text[x-1::]:
            liste.append(i)
    return liste

#print(encrypt("This is a test!", 0))
#"This is a test!")
print(encrypt("This is a test!", 1))
#"hsi  etTi sats!")
#print(encrypt("This is a test!", 2))
#"s eT ashi tist!")
'''
decrypt("This is a test!", 0)
#"This is a test!")
decrypt("hsi  etTi sats!", 1)
#"This is a test!")
decrypt("s eT ashi tist!", 2)
#"This is a test!")'''