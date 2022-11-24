from functools import reduce

lst = [47, 11, 42, 13]

reduce(lambda x,y: x+y, lst)

print(reduce(lambda x,y: x+y, lst))

