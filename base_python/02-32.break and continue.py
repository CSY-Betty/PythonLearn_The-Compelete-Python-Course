"""
break is useful for when you want to terminate a loop completely.

stop the loop when "faulty" happens.

"""

cars = ["ok", "ok", "ok", "faulty","ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")

"""
skip the faulty one and continue the loop.

"""

cars = ["ok", "ok", "ok", "faulty","ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")