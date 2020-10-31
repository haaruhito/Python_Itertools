
# Make an iterator that drops elements from 
# the iterable as long as the predicate is 
# true; afterwards, returns every element.
# That means, drops true elements and print false.
# dropwhile(fun, seq)


from itertools import dropwhile

from itertools import filterfalse  
    
def filteringtrue(y): 
    return (y < 5) 
        
li = [2, 4, 5, 7, 8, 10, 20]   
    
 
print(list(filterfalse(filteringtrue, li)))