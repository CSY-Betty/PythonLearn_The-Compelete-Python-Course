friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "charlie", "michael"]

friends_lower = set([n.lower()for n in friends])
guests_lower = set([n.lower() for n in guests])

print(friends_lower.intersection(guests_lower))

'''
Using set comprehensions
put a single value into the set comprehension
'''
friends_lower = {n.lower()for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}

print(present_friends)

'''
create a dictionary about how long ago since you last saw friends
'''
friends = ["Rolf", "ruth", "charlie", "Jen"]
time_since_seen = [3, 7, 15, 11]

'''
dictionary comprehension
put the key,colon,the value into the dictionary comprehension

'''
long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)