requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print("Adding " +requested_topping + ".")

print("\nFinished making your pizza!")

# what if pizzeria runs out of green peppers, using if in list
print("\nOut of green peppers")
requested_topping = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# checking the list is not empty
print("\nCheking list is not empty")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ",")
    
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

