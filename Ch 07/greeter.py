# input

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# if the prompt is very long / more than one lin
print("\n")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name ? "

name = input(prompt)
print("\nHello, " + name + "!")

# # numerical input - the wrong way
# age = input("How old are you? ")
# print(age) # string
# print(age >= 18) # error

# numerical input - the right way
age = input("How old are you ? ")
age = int(age)
print(age >= 18)

age = int(input("How old are you ? "))
print(age >= 18)

