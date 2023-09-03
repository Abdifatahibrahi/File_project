my_file = open('file1.txt', 'r')
file_content = my_file.read()

my_file.close()
print(file_content)

username = input("Enter your name: ")

file_writing = open('file1.txt', 'w')
file_writing.write(username)
file_writing.close()

