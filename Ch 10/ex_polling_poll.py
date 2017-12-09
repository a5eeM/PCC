filename = "polling.txt"

print("\nEnter 'quit' to Quit")

while True:
    answer = input("Why do you like programming? ")
    if answer == "quit":
        break
    else:
        with open(filename, "a") as f:
            f.write(answer + "\n")
