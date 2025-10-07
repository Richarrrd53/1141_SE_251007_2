num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=input("Enter choice (+,-,*,/)")



def add(i, j):
    return i + j

def subtract(i, j):
    return i - j

def miltiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Invalid value" 
    else:
        return a / b

if choice=='+':
    print(f"Result:{add(num1,num2)}")
elif choice=='-':
    print(f"Rrsult:{subtract(num1,num2)}")
elif choice=='*':
    print(f"Result:{miltiply(num1,num2)}")
elif choice=='/':
    print(f"Result:{divide(num1,num2)}")
else:
    print("Invalid input")