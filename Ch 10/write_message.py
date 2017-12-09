filename = "programming.txt"

with open(filename, "w") as file_object:
    # writing single line without '\n'
    file_object.write("I love programming.")
    # writing multiple lines without '\n
    file_object.write("I love creating games.")

# 'w' mode erases the file before returning the file object
with open(filename, "w") as file_object:
    # writing single line with '\n'
    file_object.write("I love programming.\n")
    # writing multiple lines
    file_object.write("I love creating new games.\n")


# 'a' mode appends to the file instead of erasing
with open(filename, "a") as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in the browser.\n")
