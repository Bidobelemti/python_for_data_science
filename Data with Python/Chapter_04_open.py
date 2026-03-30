# 4. Working with Data in Python
# 4.1 Reading and Writing Files
# Reading a file
# we use the open() function to read a file
file = open('Data with Python\\data\\example.txt', 'r')  # 'r' stands for read mode
content = file.read()  # read the entire content of the file
print(content)  # print the content of the file
file.close()  # close the file after reading
# if we want to read the file line by line, we can use a loop
with open('Data with Python\\data\\example.txt', 'r') as file:  # using 'with' ensures the file is closed after we're done
    for line in file:
        print(line.strip())  # strip() removes any leading/trailing whitespace
# this will print each line of the file without extra blank lines in between
# Writing to a file
# we can use the open() function with 'w' mode to write to a file
with open('Data with Python\\data\\output.txt', 'w') as file:  # 'w' stands for write mode if the file doesn't exist, it will be created; if it does exist, it will be overwritten
    file.write('Hello, this is a new file.\n')  # write a line to the file
    file.write('This file was created using Python.\n')  # write another line to the file

# if we want to append to an existing file instead of overwriting it, we can use 'a' mode
with open('Data with Python\\data\\output.txt', 'a') as file:  # 'a' stands for append mode
    file.write('This line will be added to the existing content.\n')  # append a line to the file

# Also, we can write multiple lines at once using writelines() method
lines = ['First line.\n', 'Second line.\n', 'Third line.\n']
with open('Data with Python\\data\\output.txt', 'a') as file:
    file.writelines(lines)  # write multiple lines to the file at once

# we can copy the content of one file to another using read and write
with open('Data with Python\\data\\example.txt', 'r') as source_file:  # open the source file in read mode
    content = source_file.read()  # read the content of the source file
    with open('Data with Python\\data\\copy.txt', 'a') as dest_file:  # open the destination file in append mode
        dest_file.write(content)  # write the content to the destination file
