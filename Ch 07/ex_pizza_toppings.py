prompt = ("\nPlease enter the piiza toppings you want:")
prompt += ("\n(Enter 'quit' after you have added your toppings. ")

still_adding = True

while still_adding:
    topping = input(prompt)

    if topping == "quit":
        still_adding = False
    else:
        print("Adding " + topping + " to your pizza!")
