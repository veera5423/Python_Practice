#Problem 7: Remove Repeated Consecutive Values
values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
res=[]
for val in values:
    if val not in res:
        res.append(val)

print("Result:", res)