# Importing single classe from a module

from electric_car_instance_attributes import ElecricCar

my_tesla = ElecricCar("tesla", "model s", 2016)

print(my_tesla.get_desciptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
