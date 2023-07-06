my_file = open('data.txt', 'r') #r is the mode of reading.
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w') #w is the mode of writing. will erases the contents of the file and overwrite anything that's already there
my_file_writing.write(user_name)

my_file_writing.close()