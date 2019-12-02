def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1,key = len)) - len(min(a1,key = len)),
            len(max(a2,key = len)) - len(min(a1,key = len)))
    return -1



s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))