friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D.C.'
    },
    {
        'name': 'Anna',
        'location': 'San Francisco'
    },
    {
        'name': 'Charlie',
        'location': 'San Francisco'
    },
    {
        'name': 'Jose',
        'location': 'San Francisco'
    }
]

your_location = input('Where are you right now? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print('You are not alone!')


if all(friends_nearby):  # True if there's at least one; or False if empty
    print('You are not alone!')

"""
false
* 0, 0.0
* None
* [], (), {}
* False
"""