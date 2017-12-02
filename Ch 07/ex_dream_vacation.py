responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name ? ")
    response = input("\nIf you could visit one place in the world, " +
                     "where would you go ? ")
    
    responses[name] = response

    repeat = input("\nWould you like to let any other person respond ? (yes/no) ")

    if repeat == "no":
        polling_active = False


print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would love to go to " + response.title())
