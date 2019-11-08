#My version1
def toJadenCase(quote):
    res = ' '.join([i.capitalize() for i in quote.split(" ")])

    return res

#My version2
def toJadenCase3(quote):
    res = quote.split(" ").title()

    return res

quote = "How can mirrors be real if our eyes aren't real"

print(toJadenCase(quote))