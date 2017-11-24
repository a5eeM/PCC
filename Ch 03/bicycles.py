bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# accesing through index
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])

# using String methods
print(bicycles[0].title())

# using individual values from the list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)