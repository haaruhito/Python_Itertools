
# selectively prints the values mentioned 
# in its iterable container passed as an 
# argument.
# Syntax given below
# islice(iterable, start, stop, step)

from itertools import islice


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
a = islice(li, 1, 9, 2)

print(list(a))

    
