"""""
age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming:{can_learn_programming}")
"""""
"""""
age = int(input("Enter your age: "))
usually_working = age >= 18 or age <= 65
20
print(f"At {age}, you are usually working: {usually_working}")
"""""
""""
and_gives you the first value if it is False, otherwise it gives you the second value.
or_gives you the first value if it is True, otherwise it gives you the second value.
"""""

x = 0 and 35
print(x)

y = 35 and 2

print(y)

name = ""
surname = "Smith"

greeting = name or f"Mr.{surname}"

print(greeting)