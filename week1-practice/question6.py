#Problem 6: Expense Tracker

expenses = [250, 1200, 450, 800, 150, 2000, 350]

total=sum(expenses)
average=total/len(expenses)
max_expense=max(expenses)
min_expense=min(expenses)
above_500=0
below_or_equal_500=0
for ex in expenses:
    if ex>500:
        above_500+=1
    else:
        below_or_equal_500+=1

print("Total Expenses:", total)
print("Average Expense:", average )
print("Highest Expense:", max_expense)
print("Lowest Expense:", min_expense)
print("Number of Expenses above ₹500:", above_500)
print("Number of Expenses below or equal to ₹500:", below_or_equal_500)
print("Expenses Above Average:")
for ex in expenses:
    if ex>average:
        print(ex)
    