filename = "guestbook.txt"

quit = False

while not quit:
    name = input("What is your name? ")
    if name == "quit":
        break
    else:
        print("Hey " + name + ", welcome to my guestbook." +
              "Enter 'quit' to Quit.")
        with open(filename, "a") as f:
            f.write(name + " visited your guestbook.\n")

