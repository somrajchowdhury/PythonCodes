''' Creating an Empty List '''

L1 = []
L2 = list()

print(L1)       #Prints the empty list.
print(L2)       #Prints the empty list.
print()

''' List can hold elements of any data type '''

L3 = [1, 2.3, 'Three']
print(L3)
print()

''' In-Built List Methods '''
print('List in built methods \n')

''' NOTE: After every operation on list1, the list is updated in some way.
          The updated list is taken for the next operation.'''

list1 = [3,4,2,6,1,5]
print('list1 = ' + str(list1))
print()     #Adds an empty line that prints nothing

''' append() : Used to add a new element at the end of a list. '''

list1.append(7)
print('List after element 7 is appended')
print(list1)
print()

''' extend() : Takes a list as an argument and all
               the elements in this list are added
               at the end of invoking list. '''

list1.extend([8,9])
print('List after the extend() method')
print(list1)
print()

''' sort() : Used to sort the contents of the list.
             By default, the function will sort the
             items in ascending order.  '''

list1.sort()
print('List sorted in ascending order')
print(list1)
print()

''' To sort a list in descending order, we use the following argument '''

list1.sort(reverse=True)
print('List sorted in descending order')
print(list1)
print()

''' reverse() : Reverses the elements {in the recently sorted (updated)} list. '''

list1.reverse()
print('List after reverse() method')
print(list1)
print()

''' insert() : Used to insert a value before a specified index of the list.
               The index of elements in a list starts from 0. '''

list1.insert(9,'TEN')
print('List after inserting the string \'TEN\' at index 9')
print(list1)
print()

''' index() : Used to get the index position of a particular value in the list. '''

e = list1.index(4)
print('The index() method')
print('Element 4 is at index ' + str(e))
print()

''' count() : Used to count number of occurrences of a particular value
              within list. '''

c = list1.count(9)
print('The count() method')
print('Number of times the element 9 occurs in ths list : ' + str(c))
print()

''' pop() : Deletes the last element in the list, by default. '''

p = list1.pop()
print('List after the pop() method')
print(list1)
print('The popped element is : ' + str(p))
print()

''' When an element at a particular index position has to be deleted, then we
    can give that element's index as argument to pop() function.  '''

u = list1.pop(8)
print('List after the element at index 8 is deleted')
print(list1)
print('The popped element is : ' + str(u))
print()

''' remove() : When we don’t know the index, but know the value to be removed,
               then this function can be used.

               This function will remove only the first occurrence of the
               specified value, but not all occurrences.

               If element 2 occurs 3 times in a list then the first occurence of
               element 2 in the list is removed not all the occuerences.'''

print('List after the element 7 is removed')
list1.remove(7)
print(list1)
print()

''' max(list_name) : Returns maximum element in the list. '''

me = max(list1)
print('Maximum element in the list is : ' + str(me))
print()

''' min(list_name) : Returns minimum element in the list. '''

ve = min(list1)
print('Minimum element in the list is : ' + str(ve))
print()

''' sum(list_name) : Returns sum of the elements in the list. '''

sm = sum(list1)
print('Sum of the elements in the list is : ' + str(sm))
print()

''' len(list_name) : Returns the number of elements in the list '''

le = len(list1)
print('Length of the list is : ' + str(le))
print()

''' clear() : This method removes all the elements in the list and makes the list empty.'''

print('List after clear() method')
list1.clear()
print(list1)
print()

'''
------------------------OUTPUT------------------------

[]
[]

[1, 2.3, 'Three']

List in built methods 

list1 = [3, 4, 2, 6, 1, 5]

List after element 7 is appended
[3, 4, 2, 6, 1, 5, 7]

List after the extend() method
[3, 4, 2, 6, 1, 5, 7, 8, 9]

List sorted in ascending order
[1, 2, 3, 4, 5, 6, 7, 8, 9]

List sorted in descending order
[9, 8, 7, 6, 5, 4, 3, 2, 1]

List after reverse() method
[1, 2, 3, 4, 5, 6, 7, 8, 9]

List after inserting the string 'TEN' at index 9
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'TEN']

The index() method
Element 4 is at index 3

The count() method
Number of times the element 9 occurs in ths list : 1

List after the pop() method
[1, 2, 3, 4, 5, 6, 7, 8, 9]
The popped element is : TEN

List after the element at index 8 is deleted
[1, 2, 3, 4, 5, 6, 7, 8]
The popped element is : 9

List after the element 7 is removed
[1, 2, 3, 4, 5, 6, 8]

Maximum element in the list is : 8

Minimum element in the list is : 1

Sum of the elements in the list is : 29

Length of the list is : 7

List after clear() method
[]

------------------------------------------------------
'''
