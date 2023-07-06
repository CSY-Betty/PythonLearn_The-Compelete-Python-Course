#while

user_input = input("Do you wish to run the program?(yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program?(yes/no): ")

print("We stopped running.")


'''
Exercise
A menu is something that repeats over and over again until the user types something that 
makes the program terminate.
In our menu, the user will be able to choose from two options: 
  If they type p , we will print "Hello" 
  If they type q , we will terminate the program 

How will we go about it? 
First, we'll ask the user for what they want to do first. 
  Do they want to print (p ), or do they want to exit without printing (q )? 
Then we'll have a while  loop that will repeat until the user types q . 
Inside the while loop, we'll have an if  statement that checks whether the user typed p . 
If they did, we'll print "Hello" .

'''

user_input = input("Enter q or p")

while user_input != 'q':
    if user_input == 'p':
        print("Hello")
    user_input = input("Enter q or p")

