filename = "learning_python.txt"

# reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# looping over the file object and then printing
print("\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# storing lines as list and then printing
print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
