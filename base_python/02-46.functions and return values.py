cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Copper", "mileage": 31000, "fuel_consumed": 235},
]

#leave two lines between each functions definition
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles.")
    return None#no value,all functions in Python return the value, none by default可寫可不寫，預設是none，若想比較詳細，可寫


for car in cars:
    print_car_info(car)


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    return f"{name} does {mpg} miles."


for car in cars:
    print(print_car_info(car))


''' 
functions can return multiple times
'''

def divide(x, y):
    if y == 0:
        return "You tried to divide zero!"
    else:
        return x / y

print(divide(10, 2))

