from functools import reduce

lst = [47, 11, 42, 13] 

max_find2 = lambda a,b: a if(a > b) else b

type (max_find2)

print(reduce(max_find2, lst))