'''
Argument 引數: value you pass in to the function

Parameter 參數: variable that accepts a value inside the function.

'''


def calculate_mpg():
    car = {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460
    }

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles.")

calculate_mpg()

'''
to make upper more better to that it can use any arbitrary piece of data
'''

def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles.")

calculate_mpg({
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
})

'''
If we have a list of cars

'''
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Copper", "mileage": 31000, "fuel_consumed": 235},
]

def calculate_mpg(car_to_calculate):#car_to_calculate: a parameters
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles.")

for car_to_calculate in cars:
    calculate_mpg(car_to_calculate)#car_to_calculate: a arguments

'''
multiple parameters
two parameters needs two arguments
'''

def calculate_mpg(car, intro):#car, intro: two parameters
    print(intro)
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles.")

for car in cars:
    calculate_mpg(car, "New car")#car, "New car": two arguments