
# This iterator takes two arguments, iterable target 
# and the function which would be followed at each 
# iteration of value in target. If no function is 
# passed, addition takes place by default. If the
#  input iterable is empty, the output iterable
#  will also be empty.

# Syntax: accumulate(iter, function)
from itertools import accumulate
import operator

def accumulate1(list1):
    for i in accumulate(list1, operator.add):
        print(i)


accumulate1([1,2,3,4])