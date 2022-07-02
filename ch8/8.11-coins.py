def coins(amount):
    if amount < 0:
        return 0
    
    if amount == 0:
        return 1
    
    return coins(amount - 0.25) + coins(amount - 0.10) + coins(amount - 0.05) + coins(amount - 0.01)

print(coins(0.5))