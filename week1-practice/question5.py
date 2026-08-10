'''
Problem 5: Bus Seat Availability Manager

Start with:

seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
'''
print("------ seats availability ------")
seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
for i in range(len(seats)):
    print(f"Seat {i+1}: {seats[i]}")

user_input=int(input("Enter the seat number you want to book (1-8): "))
if user_input<1 and user_input>8:
    print("Invalid seat number. Please enter a number between 1 and 8.")

if seats[user_input-1]=="Available":
    seats[user_input-1]="Booked"
    print(f"Seat {user_input}has been successfully booked.")
else:
    print(F"Seat is already booked ")
