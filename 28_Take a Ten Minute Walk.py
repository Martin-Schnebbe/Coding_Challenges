def isValidWalk(walk):
    if walk.count('n') == walk.count('s') and walk.count('n') == walk.count('s') and len(walk) == 10:
        return True
    return False


print(isValidWalk(['n','n','w','w','e','e','s','s','s','n']))