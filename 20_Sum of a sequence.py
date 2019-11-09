def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number,end_number+1,step)])

print(sequence_sum(2, 6, 2))
print(sequence_sum(1, 5, 1))
print(sequence_sum(1, 5, 3))
print(sequence_sum(0, 15, 3))
print(sequence_sum(16, 15, 3))