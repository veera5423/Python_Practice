'''
Problem 2: Movie Ticket Booking Summary

Take the following details from the user:

Customer name
Age
Number of tickets

Ticket price rules:

Age below 12      → ₹120 per ticket
Age 12 to 59      → ₹200 per ticket
Age 60 or above   → ₹150 per ticket
If the customer buys 5 or more tickets, provide a 10% discount on the total amount.

Display:

Customer Name
Ticket Price
Number of Tickets
Total Before Discount
Discount
Final Amount
'''

name=input("Enter Customer Name: ")
age=int(input("Enter Age: "))
no_tickets=int(input("Enter Number of Tickets: "))

price_per_ticket=0
if age<12:
    price_per_ticket=120
elif age<60:
    price_per_ticket=200
else:
    price_per_ticket=150

total=price_per_ticket*no_tickets
discount=0
if no_tickets>=5:
    discount=total*0.1

final_amount=total-discount
print("Customer Name:",name)
print("Ticket Price: ₹",price_per_ticket)
print("Number of Tickets:",no_tickets)
print("Total Before Discount: ₹",total)
print("Discount: ₹",discount)
print("Final Amount: ₹",final_amount)