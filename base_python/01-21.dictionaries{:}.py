'''
:
dictionary - allow to store keys and values
useful for when you know the key and tou wanna get the value back.

'''

friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friends_ages["Rolf"])


friends_ages["Bob"] = 20  #accessing a key of the dictionary
friends_ages["Rolf"] = 25 #change a key of the dictionary

print(friends_ages)
'''
a list or a tuple of dictionaries
multiple keys and wanna store multiple pieces of information about them
'''
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
)

print(friends[0]["name"])

'''
dict - used to turn data into a dictionary
'''
friends =[("Rolf", 24), ("Bob", 30), ("Anne", 27)]
friends_ages = dict(friends)

print(friends_ages)