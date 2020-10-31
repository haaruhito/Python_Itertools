# The Function takes only one argument as 
# input it can be like list, String, tuple, etc
# It iterates through each element and repeates 
# the cycle. 
# Syntax: cycle(iterables)

from itertools import cycle

def cycle1(string):
    count = 0
    for i in cycle([string]):    
        if count == 7:
            break
        count += 1
        print(i)   
cycle1("ABCD")
    
    
