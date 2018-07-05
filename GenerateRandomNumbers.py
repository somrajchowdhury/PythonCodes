'''
This code will print 10 random numbers between 1 and 50.
'''

import random


for i in range(10):
    r = random.randint(1, 50)   #(start_range, end_range)
    print(r)
