#Gets chained inputs from a single iterable 
# argument that is evaluated lazily
# it takes one argument unlike chain. 

from itertools import chain

def chain1(string):
    result = list(chain.from_iterable(string))
    print(result)

chain1(["Hello", "World"])