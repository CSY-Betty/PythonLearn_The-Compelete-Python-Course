friends_ages ={"Rolf": 25, "Anne": 37, "Charlie": 31,"Bob": 22}

for name in friends_ages:
    print(name)

for age in friends_ages.values():
    print(age)

for name, age in friends_ages.items():
    print(f"{name} is {age} years old.")