num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=input("Enter choice (+,-,*,/)")

def subtract(i, j):
    return i - j

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