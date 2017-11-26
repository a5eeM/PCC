buffet_menu = ("bread", "rice", "curd", "paneer pasanda", "butter chicken")

print("Restaraunt menu is:")
for food in buffet_menu:
    print(food)

# changing a tuple's value to generate error
# buffet_menu[1] = "steamed rice"

# modifyiing a tuple
buffet_menu = ["naan", "steamed rice", "curd", "paneer pasanda", "butter chicken"]
print("\nNew Restaraunt menu is:")
for food in buffet_menu:
    print(food)
