# Inheritance - child class with attributes

class Car():
    """
    A simple attempt to represent a car.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_desciptive_name(self):
        """
        Return a neatly formatted descriptive name.
        """
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        """
        Print a statement showing the car's mileage.
        """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        """
        if miles > 0:
            self.odometer_reading =+ miles
        else:
            print("You can't roll back an odometer!")
  
class ElecricCar(Car):
    """
    Represents aspects of a car, specific to electic vehicles.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(make, model, year)
        # child class attributes
        self.battery_size = 70

    # child class method
    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery. ")


my_tesla = ElecricCar("tesla", "model s", 2016)
print(my_tesla.get_desciptive_name())
my_tesla.describe_battery()
