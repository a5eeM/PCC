prompt = ("\nHow old are you ?")
prompt += ("\nEnter 'quit' after you are finished ")

user_entering = True

while user_entering:
    age = input(prompt)

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        print("\tTicket is free.")
    elif age < 13:
        print("\tTicker is $10.")
    else:
        print("\tTicket is $15")
