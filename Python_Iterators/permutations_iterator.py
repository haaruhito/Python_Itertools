# The function itertool.permutations() takes an 
# iterator and ‘r’ (length of permutation needed) 
# as input and assumes ‘r’ as default length of 
# iterator if not mentioned and returns all 
# possible permutations of length ‘r’ each.

#Syntax: Permutations(iterator, r)

from itertools import permutations

list1 = [1,2,3]

#a = permutations(list1) #Here r takes default length
#print(list(a))

# or
a = permutations(list1, 2) #Here r=2
print(list(a))

#for j in list(a):
    #print(j)

