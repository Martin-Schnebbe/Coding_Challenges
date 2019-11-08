def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int("".join(filter(str.isdigit, x)))))

print(order("hell2o Thi1s"))

'''Approach

1. seperate words
2. search for the number in there
3. print them in order

idea: dictonary

'''