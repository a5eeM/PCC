# Importing classes from linked modules

from car_attribute import Car
from electric_car_two import ElecricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElecricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())
