'''
any function is just a value
it happens that if you put a better brackets after its name it's going to run
and it's going to execute the code inside it
but you can still refer to them by name and use them as values
'''

def greet():
    print("Hello")


hello = greet

hello()


avg = lambda seq: sum(seq) / len(seq)
total = lambda seq :sum(seq)
top = lambda seq: max(seq)


#using dictionaries instead of an if statement
operations = {
    "average": avg,#lambda seq: sum(seq) / len(seq)
    "total": total,#sum
    "top": top#max
}


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 8, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},    
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))