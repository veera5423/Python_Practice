#Problem 8: Employee Record Analyzer
employee = ("Arjun", "Developer", 45000, 3)
name,desg,sal,exp=employee
print(f"Employee Name: {name}")
print(f"Designation: {desg}")
print(f"Salary: ₹{sal}")
print(f"Experience: {exp}")
print(f"Monthly Salary: ₹{sal}")
print(f"Annual Salary: ₹{sal*12}")
if exp>5:
    bonus=sal*0.15
elif exp>2:
    bonus=sal*0.10
else:
    bonus=sal*0.05
print(f"Bonus: ₹{bonus}")
print(f"Total Compensation: ₹{sal+bonus}")