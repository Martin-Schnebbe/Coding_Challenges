def solution(string, ending):
    return string[len(string)-len(ending):] == ending

print(solution('abcde', 'cde'))
print(solution('abcde', 'abc'))