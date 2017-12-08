# Importing a module into a module
"""
A set of classes that can be used to represent electric cars.
"""

from car_attribute import Car

class Battery():
    """
    A simple attempt to model a bettery for an electrice car.
    """

    def __init__(self, battery_size=70):
        """
        Initializ the battery's attributes.
        """
        self.battery_size = battery_size

    def describe_battery(self):
        """
        Print a statement describing the battery size.
        """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """
        Print a statement about the range this battery provides.
        """
        if self.battery_size == 70:
            range_of_car = 240
        elif self.battery_size == 85:
            range_of_car = 270
        
        message = "This car can go approximately " + str(range_of_car)
        message += " miles on a full charge."
        print(message)

class ElecricCar(Car):
    """
    Represents aspects of a car, specific to electic vehicles.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        """
        super().__init__(make, model, year)
        # using the instance instead of mucking up this class
        self.battery = Battery()

