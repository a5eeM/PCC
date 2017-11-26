# declaring a tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# lets try to change dimensions
# dimensions[0] = 250

# for loop in a tuple
for dimension in dimensions:
    print(dimension)

# modifying a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
