def oddOrEven(arr):
    return 'odd' if sum(arr)%2 == 1 else 'even'

print(oddOrEven([0, 1, 2]))
print(oddOrEven([0, 1, 3]))
print(oddOrEven([1023, 1, 2]))