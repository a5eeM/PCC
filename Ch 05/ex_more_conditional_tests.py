# test for equality and inequality with strings
my_car = "ford"
print(my_car != "ford")
print(my_car == "ford")

print("\nUsing lower()")
my_friends_car = "Ford"
print(my_car == my_friends_car)
print(my_car == my_friends_car.lower())

print("\nNumerical equalities/inequalities")
my_age = 29
print("My age > 30")
print(my_age > 30)
print("My age >= 30")
print(my_age >= 30)
print("My age < 30")
print(my_age < 30)
print("My age <= 30")
print(my_age <= 30)

# using and / or
print("My age > 30 and my age > 25")
print(my_age > 30 and my_age > 25 )
print("My age > 30 or my age > 25")
print(my_age > 30 or my_age > 25 )

# item in a list
print("\nItem in a list")
cars = ["bmw", "audi", "toyota", "bugati"]
print("Bugati in the list ?")
print("Bugati" in cars)

# item not in list
print("\nItems not in list")
cars = ["bmw", "audi", "toyota", "bugati"]
print("Tesla in the list?")
print("Tesla" in cars)
print("Tesla not in list?")
print("Tesla" not in cars)