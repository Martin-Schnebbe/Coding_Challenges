#my version1
def high_and_low1(numbers):
    liste_nb = [int(i) for i in numbers.split(' ')] 
    return (max(liste_nb),min(liste_nb))

#my version2
def high_and_low2(numbers):
    liste_nb = [int(i) for i in numbers.split(' ')] 
    return str(max(liste_nb)) + ' ' + str(min(liste_nb))

#my version3 - Python3
def high_and_low(numbers):
    liste_nb = [int(i) for i in numbers.split(' ')] 
    return f'{max(liste_nb)} {str(min(liste_nb))}'

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
