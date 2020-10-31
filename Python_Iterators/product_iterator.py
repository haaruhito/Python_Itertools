# Roughly equivalent to nested for-loops in a 
# generator expression. For example, product(A, B) 
# returns the same as ((x,y) for x in A for y in B).

# Syntax: 

from itertools import product

list1 = [1,2,3,4]
list2 = [3,4,5,6]

new_list = list(product(list1, list2))
print(new_list)


