# pizzas = ["farmhouse", "mexican green wave", "double cheese margherita"]
# for pizza in pizzas:
#     print(pizza)

# modifying
pizzas = ["farmhouse", "mexican green wave", "double cheese margherita"]
friend_pizzas = pizzas[:]
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza")

print("\nI really love pizza!!")

# add a new pizza to original
pizzas.append("Peppy Paneer")

# add a different to firend's list
friend_pizzas.append("5 pepper")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzs are:")
for pizza in friend_pizzas:
    print(pizza)
