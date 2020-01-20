# My approach
def two_sum(numbers, target):
    # start coding!
    for i in range(0,len(numbers)):
        for y in range(i+1,len(numbers)):
            print(i,y)
            if numbers[i]+numbers[y]==target:
                return(i,y)

def two_sum1(nums,t):
    for i,x in enumerate(nums):
        for n,y in enumerate(nums):
            if x!=y and x+y==t:
                return:(i,n)



print(two_sum([1,2,3], 4))
#two_sum([1234,5678,9012], 14690)), [1,2])
#two_sum([2,2,3], 4)), [0,1])