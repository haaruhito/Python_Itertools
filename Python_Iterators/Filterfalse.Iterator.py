
# Make an iterator that filters elements from 
# iterable returning only those for which 
# the predicate is False.
#filterfalse(fun, iter)

from itertools import filterfalse  
    
def filteringfalse(y): 
    return (y > 5) 
        
li = [2, 4, 5, 7, 8, 10, 20]   
    
 
print(list(filterfalse(filteringfalse, li)))
