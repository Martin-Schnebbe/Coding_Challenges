def xo(s):
    xcount, ocount = 0,0
    for i in s:
        if i == 'x':
            xcount+=1
        elif i == 'o':
            ocount+=1
    if xcount != ocount:
        return False
    return True


print(xo('xo0'))

'''
Test.expect(xo('xo'), 'True expected')
Test.expect(xo('xo0'), 'True expected')
Test.expect(not xo('xxxoo'), 'False expected')
'''