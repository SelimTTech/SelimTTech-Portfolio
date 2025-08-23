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
pr = input("please enter a process: (+,-,x,/)")
if pr == "+":
    print("result: "+ str(a + b))
elif pr == "-":
    print("result: "+ str(a - b))
elif pr == "x":
    print("result: "+ str(a * b))
elif pr == "/":
    print("result: "+ str(a / b))
else:
    print("please enter a valid input")

input("press enter to exit...")
