marks =int(input())

if 90<=marks<=100:
    print("A")  
elif 80<=marks<90:
    print("B")
elif 70<=marks<80:
    print("C")
elif 50<=marks<70:
    print("D")
elif 35<=marks<50:
    print("E")
elif 0<=marks<35:
    print("F")
else:
    print("Invalid marks")

