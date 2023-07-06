'''
The FizzBuzz challenge

In this exercise, print out 100 numbers, from 1 to 100 (both inclusive). 

But: 
Instead of printing multiples of 3, print "Fizz" 
Instead of printing multiples of 5, print "Buzz" 
Instead of printing multiples of both 3 and 5, print "FizzBuzz". 

That means your program will print a combination of numbers, Fizz , Buzz , and FizzBuzz .
'''

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)