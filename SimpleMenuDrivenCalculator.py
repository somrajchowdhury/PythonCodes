add=sub=mul=div=0
while True:
    print()
    print('''       MENU   ''')
    print("-----------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    print("-----------------\n")
    print("Enter your choice:")
    ch = input("Choice: "+" ")
    if ch=='5':
        break
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    if ch=='1':
        add = x+y
        print("Sum : " + str(add))
    elif ch=='2':
        sub = x-y
        print("Difference : " + str(sub))
    elif ch=='3':
        mul = x*y
        print("Product : " + str(mul))
    elif ch=='4':
        if y==0:
            print("Math ErrOR!")
        else:
            div = x/y
            print("Result : " + str(div))
            
'''
This program does't quit until you give Choice: 5 which means 'Quit' in the menu.

------OUTPUT------

MENU   
-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
-----------------

Enter your choice:
Choice:  1
Enter first number: 1
Enter second number: 2
Sum : 3

       MENU   
-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
-----------------

Enter your choice:
Choice:  2
Enter first number: 3
Enter second number: 4
Difference : -1

       MENU   
-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
-----------------

Enter your choice:
Choice:  3
Enter first number: 5
Enter second number: 6
Product : 30

       MENU   
-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
-----------------

Enter your choice:
Choice:  4
Enter first number: 1
Enter second number: 0
Math ErrOR!

       MENU   
-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
-----------------

Enter your choice:
Choice:  4
Enter first number: 4
Enter second number: 2
Result : 2.0

       MENU   
-----------------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Quit
-----------------

Enter your choice:
Choice:  5

------------------
'''
