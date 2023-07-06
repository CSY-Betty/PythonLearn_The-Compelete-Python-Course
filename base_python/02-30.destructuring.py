'''
Destructuring
(also called unpacking) is where we take a collection, like a list or a tuple, and 
we break it up into individual values. This is quite useful, as it enables us to do things 
like destructuring assignments, where we assign values to several variables at once from a 
single collection.
'''


#currencies = 0.8, 1.2
#usd, eur = currencies

friends =[("Rolf", 25), ("Anne", 37), ("Charlie", 31),("Bob", 22)]

#for friend in friends:
#    name, age = friend 
#    print(f"{name} is {age} years old.")


#using destructuring
for name, age in friends:
    print(name, age)
    print(f"{name} is {age} years old.")
