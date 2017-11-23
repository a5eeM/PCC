motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# modifying a list
motorcycles[0] = "ducati"
print(motorcycles)

# appending to a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

# append makes it easy to build dynamic lists
motorcycles = []  # empty list
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

print(motorcycles)

# inserting elements to a list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# removing items from a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# removing item using pop
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# how pop can be useful
motorcycles = ["honda", "yamaha", "suzuki"]

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# popping items from any position in a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

first_owned = motorcycles.pop(0)
print(motorcycles)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# removing items by value using remove()

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati") # removing by value
print(motorcycles)

# using remove to use a value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"

motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")