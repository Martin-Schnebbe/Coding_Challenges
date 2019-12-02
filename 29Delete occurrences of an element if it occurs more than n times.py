#My version1
def delete_nth1(order,max_e):

    liste1 =[]

    for i in order:
        if liste1.count(i) < max_e:
            liste1.append(i)
        

    return liste1



print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))