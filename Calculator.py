def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x+y

def divide(x, y):
    if y == 0:
        return "y cannot be equal to zero"
    return x/y

def calculator():
    print("Select the operator from the following: ")
    print("a. Add")
    print("b. Subtract")
    print("c. Multiply")
    print("d. Divide")

    Enter = input("Enter (a/b/c/d): ")

    N1 = float(input("Enter the first number: "))
    N2 = float(input("Enter the second number: "))

    if Enter == "a":
        print("The addition of the two numbers is: ", add(N1, N2))
    elif Enter == "b":
        print("The subtraction of the two numbers is: ", subtract(N1, N2))
    elif Enter == "c":
        print("The product of the two numbers is: ", multiply(N1, N2))
    elif Enter == "d":
        print("The division of the two numbers is: ", divide(N1, N2))
    else:
        print("Invalid input")

calculator()