from itertools import chain, combinations

def powerSet(iterable):
    return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable)+1)) 

print(list(powerSet([1, 2, 3, 4, 5])))