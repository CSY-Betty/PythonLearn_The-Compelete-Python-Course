'''
slice(start, stop, step)

start (optional)- Starting index value where the slicing of the object starts. 
Default to 0 if not provided.

stop - Index value until which the slicing takes place.

step (optional) - Index value steps between each index for slicing. 
Defaults to 1 if not provided.

'''
'''
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

print(friends[2:4])
print(friends[1:])
print(friends[:4])
print(friends[:])
print(friends[-3:])
'''
 # x = [ -10, -9, -8, -7,   -6,   -5,  -4,   -3,   -2,  -1] 
 # x = [   0, 1,  2,   3,   4,    5,   6,    7,    8,   9]
x = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x[:-3])

#          0 -5     1 -4     2 -3    3 -2   4 -1
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[-3:4])