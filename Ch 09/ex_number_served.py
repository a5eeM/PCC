class Restaurant():
    """
    A class for a restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0
    
    def describe_restaurant(self):
        """describe the restaurant"""
        print(self.restaurant_name + " is a " + self.cuisine_type + " restaurant.")
  
    def open_restaurant(self):
        """Indicates the restaurant is open"""
        print(self.restaurant_name + " is now open.")
    
    # print number_served
    def read_number_served(self):
        """
        Print a statement showing the number of customers served.
        """
        print(self.restaurant_name + " has served " + str(self.number_served) +
              " customers.")

    # change attribute number_served using a method
    def set_number_served(self, number):
        """
        Update number_served by the restaurant
        """
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can not add negative numbers")
    
    # incrementing number_served attribute
    def increment_number_served(self, number):
        """
        Add given number to number_served reading
        """
        if number >= 0:
            self.number_served += number
        else:
            print("You can not add negative numbers.")

restaurant = Restaurant("hot n spicy", "indian")
restaurant.read_number_served()
restaurant.number_served = 4
restaurant.read_number_served()
restaurant.set_number_served(40)
restaurant.read_number_served()
restaurant.increment_number_served(6)
restaurant.read_number_served()
