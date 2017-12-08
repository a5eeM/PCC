# Importing an entire module
# Ideally I do not have to use 'as', but because we don't have a car module to work with.

import electric_car_instance_attributes as car

my_beetle = car.Car("volkswagen", "beetle", 2016)
print(my_beetle.get_desciptive_name())

my_tesla = car.ElecricCar("tesla", "roadster", 2016)
print(my_tesla.get_desciptive_name())
