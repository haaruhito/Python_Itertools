# Make an iterator that returns 
# consecutive keys and groups from 
# the iterable
#groupby(iterable, key)

from itertools import groupby

list1 = [("animals", "cat"), ("animals", "dog"), ("birds", "sparrow"), ("birds", "crow")] 
  

key_func = lambda x: x[0] 

  
for key, group in groupby(list1, key_func): 
    print(key + " :", list(group)) 