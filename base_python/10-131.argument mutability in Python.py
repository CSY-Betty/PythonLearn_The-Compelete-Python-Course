friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0


print(id(friends_last_seen))
print(id(friends_last_seen['Rolf']))

see_friend((friends_last_seen, 'Rolf'))
print(id(friends_last_seen['Rolf']))
print(id(see_friend))