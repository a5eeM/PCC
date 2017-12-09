filename = "guest.txt"

# Python will creathe the file if it does not exist

name = input("What is your name ? ")

if name:
    with open(filename, "w") as f:
        f.write(name)
else:
    print("You have not entered any name!")
