# Does not work.

def oneAway(a, b):
    change_counter = 0

    # a is always the shorter word
    if len(b) < len(a):
        temp = a
        a = b
        b = temp

    pointer_a = 0
    pointer_b = 0
    
    while pointer_a < len(a)-1 and pointer_b < len(b)-1:
        if a[pointer_a] != b[pointer_b]:
            if change_counter >= 1:
                return False
            change_counter += 1
            
            if len(a) != len(b):
                pointer_a += 1

        pointer_a += 1
        pointer_b += 1

    return change_counter <= 1
    

print(oneAway("pale", "palses"))