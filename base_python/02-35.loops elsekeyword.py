"""
else in for loop
the else is in the same line as the for loop.
And what this means in Python,
is that if the loop completely ran through all of the elements,
without encountering a break,
or an error, then we run this code here.

"""

"""
cars = ["ok", "ok", "ok", "faulty","ok", "ok"]
all_successful = True

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        all_successful = False
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")

if all_successful:
    print("All cars built successfully. No faulty cars!")
"""

cars = ["ok", "ok", "ok", "faulty","ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")