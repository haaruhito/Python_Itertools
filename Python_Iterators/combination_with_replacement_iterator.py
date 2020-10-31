

#Syntax: combination_with_replacement(iterable, r)
# 'r' is necessary here.

from itertools import combinations_with_replacement

list1 = [1,2,3]

a = combinations_with_replacement(list1, 2)
print(list(a))

