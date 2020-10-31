
# The arguments corresponding to boolean true 
# are printed else all are skipped.

from itertools import compress

selectors = [1,0,0,1,1]
def compress1(string1):
    for i in compress(string1 , selectors):
        print(i)

compress1("Hello")