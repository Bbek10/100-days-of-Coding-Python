# file = open("my_file.txt")

# To read the file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#to write to the file with mode w a
with open("new_file.txt", mode="w") as file:
    file.write("I am Bibek")

