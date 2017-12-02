prompt = ("\nHow old are you?")
prompt += ("\nEnter 'quit' after you are finished. ")

user_entering = True

while user_entering:
    age = input(prompt)

    if age == "quit":
        user_entering = False
    elif int(age) > 12:
        print("Ticket is $15" )
    elif int(age) >= 3 and int(age) <= 12:
        print("Ticker is $10.")
    else:
        print("Ticket is free.")
