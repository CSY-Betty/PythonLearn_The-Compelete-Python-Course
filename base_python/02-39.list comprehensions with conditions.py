"""
list comprehensions with conditions
use to figure out some elements while we're putting them into a new list using list comprehensions
"""
ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)


friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

'''
compare friends and guests
they are in a mix of uppercase and lowercase

First approaches
turn all of these guests into lowercase
turn both of these into sets by actually passing them through the set function
then you could print the intersection of the two

but it's a bit more difficult to get these names out as capital C and capital R
because in the sets you've got them all as lowercase

'''

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))

'''
to compare friends and guests and get capital C and capital R
use a list comprehension where we create a present_friends list

'''

present_friends = [
    name.title() 
    for name in guests 
    if name.lower() in [f.lower() for f in friends]
]
print(present_friends)
