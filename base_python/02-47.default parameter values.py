import re


def add(x, y= 3):#y= 3 means a  default parameter
    total = x + y
    return total

print(add(5))#default y=3

print(add(5, 6))#changeed default value

print(add(x=3))#named argument

print(add(x=3, y=2))

print(add(4 ,y=2))

#print(add(x=5, 2))
#error,because the argument that doesn't have a name cannot be used after an argument that has a name.

#def add(x=5, y=)
# #error:default values must go at the end


print(1, 2, 3, 4, 5, sep=" - ")

default_y = 3

def add(x, y=default_y):
    total = x + y
    print(total)

add(2)

default_y = 4#won't change
add(2)

'''
when python defines the function, it also stores the default value at the time
even if you change the variable that is the default value,
it will not change when you use the functon,
it still keeps the value what was used when you defined the function initially.

mutability
'''
