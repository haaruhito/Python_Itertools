# This iterator splits the container into 
# a number of iterators mentioned in the 
# argument.
# Syntax: tee(iterator, count)

from itertools import tee
dic1 = {1: "a", 2: "b", 3: "c"}

for i in tee(dic1, 4):
    print(list(i))