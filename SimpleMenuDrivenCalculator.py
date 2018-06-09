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
