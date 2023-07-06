friends = ["Rolf", "ruth", "charlie", "Jen"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends,time_since_seen))

print(long_timers)

long_timers = list(zip(friends,time_since_seen))

print(long_timers)

'''
can have more lists combines
if the list was longer than others, zip will just ignore any elements that don't match the other lists
'''
long_timers = list(zip(friends,time_since_seen), [1, 2, 3, 4, 5])