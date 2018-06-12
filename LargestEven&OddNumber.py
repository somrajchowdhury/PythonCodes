n=int(input("Enter the number of elements to be in the list: "))     #Enter the size of List

b=[]    #Create an Empty List

for i in range(1,n+1):
    a=int(input('Element '+str(i)+' : '))       #Input the elements
    b.append(a)                                 #Using append(), adds the entered element to the end of the List
print()                                         #Add new line
print('List b: ' + str(b))
print()                                         #Add new line

c=[]        #Create an empty list to Store even numbers in list b
d=[]        #Create an empty list to Store odd numbers in list b

for i in b:             #looping elements in the list b
    if(i%2==0):         #if number divisible by 2, it is even
        c.append(i)     #Store the even number in list c using append()
    else:               #if not even, it is an odd number
        d.append(i)     #Store the odd number in list d using append()
print('Even Number List c: ' + str(c))
print('Odd Number List d: ' + str(d))
print()                 #Add new line

c.sort()        #Sort the even number list in increasing order using sort()
d.sort()        #Sort the odd number list in increasing order using sort()

print('Sorted list c: ' + str(c))
print('Sorted list d: ' + str(d))
print()     #Add new line

count1=0
count2=0

for k in c:             #loops through every element in list c
    count1=count1+1     #count1 saves the size i.e. the number of elements in the list c
for j in d:             #loops through every element in list d
    count2=count2+1     #count2 saves the size i.e. the number of elements in the list d

print('Largest even number:',c[count1-1])       # 'count1-1' is the index position that points to the
                                                # last element in the sorted list which is the largest even
print('Largest odd number',d[count2-1])         # number in list c and largest odd number in  list d

'''
------OUTPUT------

Enter the number of elements to be in the list: 8
Element 1 : 9
Element 2 : 2
Element 3 : 5
Element 4 : 3
Element 5 : 8
Element 6 : 1
Element 7 : 4
Element 8 : 7

List b: [9, 2, 5, 3, 8, 1, 4, 7]

Even Number List c: [2, 8, 4]
Odd Number List d: [9, 5, 3, 1, 7]

Sorted list c: [2, 4, 8]
Sorted list d: [1, 3, 5, 7, 9]

Largest even number: 8
Largest odd number 9

------------------
'''
