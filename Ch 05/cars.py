cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# conditional tests
car = "bmw"
print(car == "bmw")

car = "audi"
print(car == "bmw")

# Ignoring case
car = "Audi"
print(car == "audi")
print(car.lower() == "audi")
print(car)
