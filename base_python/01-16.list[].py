"""
[]
list
  An ordered, sequential data type.
"""
grades = [80, 75, 90, 100]
friends =[["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(len(grades))
print(friends[0][0])

friends.append(["Jen",25])
print(friends)

friends.remove(["Bob", 30])
print(friends)
"""
tuple
  immutable
  Defined by separating multiple values with commas.
  For better readability, it can be surrounded by parentheses (brackets).
  cannot add new grades
"""
grades = (80, 75, 90, 100)

"""
set 
  An unordered data type.
  Defined by using a pair of curly braces.
  cannot have duplicates,if want to compare
"""
grades = {80, 75, 90, 100}

"""
dic
  Defined with 3 key components: curly braces, keys, and values
  Keys must be strings or other hashable values
  Values associated to each key can be anything
  Dictionaries can be defined in one line or in multiple lines to aid readability
  Access values in a dictionary by using square brackets and the key
"""
grades = {"Bob": 80, "Ann": 75, "Jane": 90, "Rose": 100}
employees = {
    'ID': 16915,
    'name': 'James',
    'department': ['Sales','Accounting']
}