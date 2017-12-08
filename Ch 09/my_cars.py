# Importing multiple classes, electric_car_instance_attributes ideally should be just car
# For my own reasons it is not.

from electric_car_instance_attributes import Car, ElecricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_desciptive_name())

my_tesla = Car("tesla", "model s", 2016)
print(my_tesla.get_desciptive_name())
