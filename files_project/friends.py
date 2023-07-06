# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to `nearby_friends.txt`

friends = input('Enter three friend name, separated by commas (no spaces, please): ').split(',')
#['Rolf', 'Jose', 'Charlie']

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()] # [line1, line2, line3, line4]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n') # save them to the file

nearby_friends_file.close()