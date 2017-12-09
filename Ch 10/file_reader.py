with open("text_files/pi_digits.txt") as file_object:
    contents = file_object.read()
    # use rstrip if you see an empty new line
    # print(contents)
    print(contents.rstrip())

file_path = "/Users/billo/Development/Python/PCC/Ch 10/text_files/pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# reading line by line
file_path = "/Users/billo/Development/Python/PCC/Ch 10/text_files/pi_digits.txt"
with open(file_path) as file_object:
    # read line by line
    for line in file_object:
        print(line.rstrip())

# file name as variable
filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
