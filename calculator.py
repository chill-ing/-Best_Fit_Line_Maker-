def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def calculator():
    x = int(input("Enter first value for calculation: "))
    y = int(input("Enter second value for calculation: "))
    operation = str(input("Enter operation to conduct [addition\subtraction\multiplication\division]: "))
    if (operation == "addition"):
        print(addition(x,y))
    elif (operation == "subtraction"):
        print(subtraction(x,y))
    elif (operation == "multiplication"):
        print(multiplication(x,y))
    elif (operation == "division"):
        print(division(x,y))
    else:
        print("There's only 4 methods to perform [addition/subtraction/multiplication/division]")

if __name__ == "__main__":
    calculator()
    
"05/02/24"