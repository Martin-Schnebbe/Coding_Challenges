def bouncingBall(h, bounce, window):

    count = 1
    
    while h*bounce > window:
        h = h*bounce
        count+=2

    # your code
    return count

print(bouncingBall(3, 0.66, 1.5))
print(bouncingBall(30, 0.66, 1.5))
