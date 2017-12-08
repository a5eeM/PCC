class Restaurant():
    """
    A class for a restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
    
    def describe_restaurant(self):
        """describe the restaurant"""
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")
    
    def open_restaurant(self):
        """Indicates the restaurant is open"""
        print(self.restaurant_name + " is now open.")

class IceCreamStand(Restaurant):
    """
    Represents aspects of a restaurant, specific to ice cream stands.
    """

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Initilize attributes, both parent and child class.
        """
        super().__init__(restaurant_name, cuisine_type)
        # child class attributes
        self.flavors = flavors
    
    def get_flavors(self):
        """
        Print a statement about the flavors the ice cream stand provides.
        """
        print(self.restaurant_name + " has:")
        for flavor in self.flavors:
            print(" -" + flavor.title())

baskin_robins = IceCreamStand("baskin robins", "ice cream",
                              ["chocolate", "vanilla", "strawberry", "belgian dark chocolate"])
baskin_robins.get_flavors()
