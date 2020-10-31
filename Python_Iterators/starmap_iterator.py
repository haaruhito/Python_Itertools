# This iterator takes a function and 
# tuple list as argument and returns the 
# value according to the function from each 
# tuple of list.
# Syntax: starmap(func., tuple list)

from itertools import starmap
import operator

a = [(5,5), (3,4), (10,10)]

b = (starmap(operator.add, a))
print(list(b))