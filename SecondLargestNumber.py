n = int(input('Enter size of the List: '))      #Enter List Size

list = []       #Create empty list

for i in range(1,n+1):  
    elem = int(input('Element '+str(i)+' : '))      #Enter the elements of list
    list.append(elem)       #Add these elements to the list using append()
    
print()     #Print nothing, return an empty line
print('List = ' + str(list) + '\n')     #Display the list elements

list.sort()     #Sort the list elements in increasing order using sort()
print('Sorted List = ' + str(list) + '\n')      #Display sorted list elements

count = 0

for j in list:
    count = count + 1       #'count' saves the count of elements in list

print('Second Largest Element = ', list[count-2])       #'count-2' is the index value for the second
                                                        # element from the end of the sorted list which
                                                        # is the Second Largest element in the List




