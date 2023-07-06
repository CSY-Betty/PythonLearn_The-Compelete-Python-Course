'''
functions
start with the def keyword and after put a space
the next thing is the function name
afterwards, put a pair of brackets
inside the brackets, we can put some stuff...learn in a future video
after the brackets, the usual colon

variable created inside a function die when they reach the end of the function
variable in function only used within tje function itself
'''

from unicodedata import name


def greet():
    name = input("Enter your name: ")
    print(f"Hello,{name}!")

greet()

print(name)#this will be error