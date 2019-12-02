def create_phone_number1(n):
    input_string = ''.join(str(n))
    return F"({input_string[:4]})"

def create_phone_number(n):
    input_string = ''.join(map(str,n))
    return "(s%) s% - s%" % (input_string[:4], input_string[4:7], input_string[7:])


print(type(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))