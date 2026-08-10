'''Problem 1: Parking Fee Calculator

Write a Python program that calculates the parking charge based on the number of hours a vehicle was parked.

Parking charges:

Up to 2 hours      → ₹30 per hour
3 to 5 hours       → ₹25 per hour
More than 5 hours  → ₹20 per hour
If the parking charge exceeds ₹150, add a service charge of ₹20.

Example:

Enter parking hours: 6

Parking Charge: ₹120
Service Charge: ₹0
Final Amount: ₹120'''

parking_hr=int(input("Enter Parking hours: "))

pc=0
sc=0
fa=0
if parking_hr<=2:
    pc=parking_hr*30
elif parking_hr<=5:
    pc=parking_hr*25
else:
    pc=parking_hr*20

if pc>150:
    sc=20
fa=pc+sc
print("Parking Charge: ₹",pc)
print("Service Charge: ₹",sc)
print("Final Amount: ₹",fa)
