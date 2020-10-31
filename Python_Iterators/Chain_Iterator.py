
#It is a function that takes a series of iterables and 
# returns one iterable
# It takes two or more arguments. 

from itertools import chain

def chain1(list1, list2):
    result = list(chain(list1, list2))
    print(result)

chain1([1,2,3], [4,5,6])
