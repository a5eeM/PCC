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

restaurant = Restaurant("Hot n Spicy", "Indian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()