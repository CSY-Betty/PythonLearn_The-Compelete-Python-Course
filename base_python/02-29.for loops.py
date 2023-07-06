"""
for  ... in ...:
    repeat something a defined number of times
    in other language is more like a foreach loop
    When you want to repeat something a certain number of timesand you know how many that is,
    or when you want to use each of the values of an iterable,such as a list, tuple, or set, or dictionary,
    and you want to do something once for each of the values.
"""
students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
    ]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} got a grade of {grade}.")

for a in range(3):
    print(a)
