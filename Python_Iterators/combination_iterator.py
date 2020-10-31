# The formula for combinations is nCr = n! / (r! * (n - r)!), 
# where n represents the number of items, and r 
# represents the number of items being chosen at 
# a time.

#Syntax: combinations(iterator, r)

from itertools import combinations

list1 = [1,2,3]

#a = combinations(list1) #Here r takes default length
#print(list(a))

# or
a = combinations(list1, 2) #Here r=2
print(list(a))

#for j in list(a):
    #print(j)
