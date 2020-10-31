# Make an iterator that returns elements 
# from the iterable as long as the predicate 
# is true
# Syntax: takewhile(predicate, iterable)

from itertools import takewhile

def greator(n):
    return n > 10

list1 = [11,12,44,7,22,56,8]

list2 = list(takewhile(greator, list1))
print(list2)

