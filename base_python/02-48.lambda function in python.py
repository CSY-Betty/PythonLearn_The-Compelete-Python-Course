'''
lambda function
used to get inputs, do a small amount of processing,
and return outputs.
'''

def divide(x, y):
    return x / y


divide = lambda x, y: x / y #identical to the line 7 and 8

print(divide(5, 2))

print((lambda x, y: x / y )(15, 3))

'''
example
'''

def average(sequence):
    return sum(sequence) / len(sequence)

average = lambda sequence: sum(sequence) / len(sequence)#equal to line 21,22

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 8, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},    
]

for student in students:
    print(average(student["grades"]))