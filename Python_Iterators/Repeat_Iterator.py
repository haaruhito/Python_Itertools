# In repeat() we give the data and give the 
# number, how many times the data will be 
# repeated. If we will not specify the number,
#  it will repeat infinite times. In repeat(),
#  the memory space is not created for every 
# variable. Rather it creates only one variable
#  and repeats the same variable.

# Syntax: repeat(object, times)

from itertools import repeat

def repeat1(string):
    for i in repeat(string, 5):
        print(i)
repeat1("Hello")