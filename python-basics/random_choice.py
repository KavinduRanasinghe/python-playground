import random

file_name = input('Enter the file name : ')

file = open(file_name)

file_content = file.readline()

file_content_list = file_content.split('\n')
file.close()

print(random.choice(file_content_list))
