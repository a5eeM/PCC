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

hot_n_spicy = Restaurant("hot n spicy", "north indian")
eye_of_the_tiger = Restaurant("eye of the tiger", "continental")
sagar_ratna = Restaurant("sagar ratna", "south indian")

hot_n_spicy.describe_restaurant()
eye_of_the_tiger.describe_restaurant()
sagar_ratna.describe_restaurant()