''' Version 1
def square_digits(num):
    return int(''.join(map(str,[(int((str(num)[i])))**2 for i in range(len(str(num))) ])))
'''
#Version 2
def square_digits(num):
    return ''.join(str(int(d)**2) for d in str(num)) 


res = square_digits(321)

print(type(res))
print(res)