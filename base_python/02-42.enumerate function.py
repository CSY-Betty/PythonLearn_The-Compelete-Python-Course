friends = ["Rolf", "ruth", "charlie", "Jen"]

#using index or counter to give each friends numbers
index = 0

for friend in friends:
    print(index)
    print(friend)
    index = index + 1


counter = 0

for friend in friends:
    print(counter)
    print(friend)
    counter = counter + 1

'''
enumerate
give a number for each element in list
join them together so that we can then access them like that in the for loop
'''

#enumerate function default starts at 0 but can tell it to start at 1
for counter, friend in enumerate(friends, start = 1):
    print(counter)
    print(friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))
print(list(zip([0, 1, 2, 3],friends)))