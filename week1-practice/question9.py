#Problem 9: Message Slicing Tool
'''First 5 Characters
Last 5 Characters
Characters from Index 2 to 7
Every Second Character
Message in Reverse
Message Without First and Last Character    '''

st=input("Enter a String:")

print("First 5 Characters:",st[:5])
print("Last 5 Characters:",st[-5:])
print("Characters from Index 2 to 7:",st[2:8])
print("Every Second Character:",st[::2])
print("Message in Reverse:",st[::-1])
print("Message Without First and Last Character:",st[1:-1])