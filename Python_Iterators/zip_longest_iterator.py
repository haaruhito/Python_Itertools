# It prints the values of iterables alternatively
#  in sequence. If one of the iterables is printed 
# fully, the remaining values are filled by the 
# values assigned to fillvalue parameter.

#Syntax : zip_longest( iterable1, iterable2, fillval)
# default fillval is "Null"
from itertools import zip_longest

list1 = [1,2,3]
list2 = [3,4,5,6,7]

new_list = list(zip_longest(list1, list2))
print(new_list)