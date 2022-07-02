def tripleStep(steps):
    # This is an invalid way to reach to steps amount
    if steps < 0:
        return 0
    
    # This is a valid form to reach steps amount. Therefore we'll add 1 way to step up these stairs. 
    if steps == 0:
        return 1
    
    return tripleStep(steps-1) + tripleStep(steps-2) + tripleStep(steps-3)
    
print(tripleStep(5))