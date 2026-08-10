'''Problem 3: Multiplication Pattern Analyzer

Take a number n from the user.

Print its multiplication table from 1 to 10.

For every result, also display whether the result is even or odd.'''

n=int(input("Enter a number: "))
e_count=0
o_count=0
for i in range(1, 11):
    res=n*i
    print(F"{n} x {i} = {res}")
    if res%2==0:
        e_count+=1
    else:
        o_count+=1
print("Even Results:",e_count)
print("Odd Results:",o_count)
