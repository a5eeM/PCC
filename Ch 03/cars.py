# using sort() method on a list, sort changes the order permanently
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.sort()
print(cars)

# sorting in reverse
print("\n")
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.sort(reverse=True)
print(cars)

# using sorted() function to sort temporarily
print("\n")
cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

# list in reverse order
print("\n")
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse()
print(cars)

# length of a list
print("\n")

cars = ["bmw", "audi", "toyota", "subaru"]
print("Length of the list is: "  + str(len(cars)))