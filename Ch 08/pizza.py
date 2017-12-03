# passing arbitrary number of arguments

def make_pizza(*toppings):
    """
    Print the lisy of toppings that have been requested
    """
    print(toppings)

# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")

def make_pizza_two(*toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\nMaking a pizza with the follwing toppings:")
    for topping in toppings:
        print("- " + topping)

# make_pizza_two("pepperoni")
# make_pizza_two("mushrooms", "green peppers", "extra cheese")


def make_pizza_three(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\nMaking a " + str(size) + "-inch pizza" +
          " with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# make_pizza_three(16, "pepperoni")
# make_pizza_three(12, "mushrooms", "green peppers", "extra cheese")
