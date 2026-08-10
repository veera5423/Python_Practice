num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

print("Enter the operation to be performed(+,-,/-%)")
op=input() 
if op=="+":
    print(f"Addition of {num1} and {num2} ={num1+num2}")
elif op=="-":
    print(f"Subbractionof {num1} and {num2} = {num1-num2}")
elif op=="*":
    print(f"Multiplication of {num1} and {num2} = {num1*num2}")
elif op=="/":
    if num2>0:
        print(f"Division of {num1} and {num2} = {num1/num2}")
    else:
        print("Division by zero is not possible")
elif op=="%":
    if num2>0:
        print(f"Modulo of {num1} and {num2} = {num1%num2}")
    else:
        print("Modulo by zero is not possible")
else:
    print("Invalid operator")
