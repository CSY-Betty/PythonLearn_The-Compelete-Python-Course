
numbers = [0, 1, 2, 3, 4]

#without using comprehensions
doubled_numbers = []

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)

#using comprehensions
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

doubled_numbers = [number * 2 for number in range(5)]
print(doubled_numbers)

doubled_numbers = [5 for number in range(5)]
print(doubled_numbers)

doubled_numbers = [5 for _ in range(5)]
print(doubled_numbers)

friends_ages = [22, 31, 35, 37]
age_stings = [f"My friend is {age} years old." for age in friends_ages]

print(age_stings)

names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)


friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend_titlecased} is one of your friends.")

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")




friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "charlie", "michael"]

friends_lower = ([f.lower() for f in friends])

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]

print(present_friends)