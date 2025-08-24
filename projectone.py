while True:
    try:
        a=int(input("Enter a number: "))
        break
    except ValueError:
        print("please enter a number like 1, 2, 3, 4")
while True:
    try:
        b=int(input("Enter an another number: "))
        break
    except ValueError:
        print("please enter a number like 1, 2, 3, 4")
while True:
    try:
        pr = input("please enter a process: (+, -, x, /) ")
        if pr in ["+","-","x","/"]:
            if pr == "+":
                print("result: " + str(a + b))
            elif pr == "-":
                print("result: " + str(a - b))
            elif pr == "x":
                print("result: " + str(a * b))
            elif pr == "/":
                print("result: " + str(a / b))
            break
    except ValueError:
        print("please enter process from the box, (+, -, x, /)")
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        while True:
            try:
                b = int(input("please enter second number as non-zero: "))
                break
            except ValueError:
                print("please enter second number as non-zero and enter an integer")


input("press enter to exit...")
