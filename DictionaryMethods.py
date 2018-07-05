'''
A Dictionary is a Data Structure which consists of Key:Value pairs
'''

d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
print("d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}")
print()
'''
1. keys()

This function returns the keys in the dictionary.

'''
print('Operation: d.keys()\n')
print('Output:   ', d.keys())
print('\n-----\n')
'''
2. values()

This function returns the values in the dictionary.

'''
print('Operation: d.values()\n')
print('Output:   ', d.values())
print('\n-----\n')
'''
3. items()

This function returns the items i.e., the Key:Value pairs in the dictionary.

'''
print('Operation: d.items()\n')
print('Output:   ', d.items())
print('\n-----\n')
'''
4. get(Key)

This function returns the corresponding Value on inputting the Key.

'''
print('Operation: d.get(\'a\')')
print('Output:   ', d.get('a'))
print('\n-----\n')
'''
5. pop(Key)

This function removes the item corresponding to the input Key value.

'''
print('Operation: d.pop(\'e\')')
print('Output:   ', d.pop('e'))
print('Status:   ', d)
print('\n-----\n')
'''
6. popitem()

This function removes the last element from the dictionary.

'''
print('Operation: d.popitem()')
print('Output:   ', d.popitem())
print('Status:   ', d)
print('\n-----\n')
'''
'''
