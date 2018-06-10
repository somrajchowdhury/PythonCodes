class Stack:
    def __init__(self):
        self.items = []     #Start with an empty List.

    def isEmpty(self):
        return self.items == []     #Returns the same empty List.

    def push(self, item):
        self.items.append(item)     #Pushes the element input.
                                    #Append() means placing the element at the end of the list.
    def pop(self):
        return self.items.pop()     #pop() removes the last appended element.

    def peek(self):
        return self.items[len(self.items) - 1]      #Returns the element which is pushed last.

    def size(self):
        return len(self.items)                      #Length is number of elements in the List i.e size.

s=Stack()          #Object is Created here.

print(s.isEmpty()) #Stack is checked if it is Empty.
s.push(4)          #Integer value of 4 is pushed.
print(s.peek())    #Display this pushed element.
s.push('dog')      #String 'dog' is pushed.
print(s.peek())    #Display this pushed element.
s.push(8.4)        #Floating point number 8.4 is pushed.
print(s.peek())    #Display this pushed element.
print(s.size())    #Returns the number of elements the stack holds.
print(s.pop())     #Stack is LastInFirstOut, as 8.4 is inserted last, it's popped.
print(s.pop())     #'dog' element is popped.
print(s.size())    #Returns the number of elements the stack holds.

'''
------OUTPUT------
True
4
dog
8.4
3
8.4
dog
1
-------------------
'''

