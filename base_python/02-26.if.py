'''
if x == y:
    print....
else:
    print....

if x = y:
    print....
elif y=z:
    print....
else:
    print....

indentation => the four spaces in front of a line that denote that this is inside a block
'''

friend = "Rolf"
user_name = input("Enter tour name: ")

if user_name == friend:
    print("Hello, fried")
else:
    print("Hello, stranger")

friends = ["Rolf", "Bob", "Anne"]
family = ["Jane", "Charlie"]

user_name = input("Enter tour name: ")
"""
user_name is a string
friends is a list
diferent type cannot use ==
instead use in
"""
if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")