print('Before Swapping')
n1 = eval(input('first number: '))      #Input first number
n2 = eval(input('second number: '))     #Input second number
print()
print('Swapping...')
n1,n2 = n2,n1           #Main Logic of Swapping - Simultaneous Assignment
print()
print('After Swapping')
print('first number: ',n1)
print('second number: ',n2)

'''
------OUTPUT------

Before Swapping
first number: 1
second number: 2

Swapping...

After Swapping
first number:  2
second number:  1

------------------
'''
