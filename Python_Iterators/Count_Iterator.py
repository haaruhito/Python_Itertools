

#count(start,[step])

from itertools import count

def count1(num):
    for num in count(start=5, step=2):
        if num > 20:
            break
        print(num)
    
count1(10)
