# User module for ex 9-12
"""
A class used to represent users.
"""

class User():
    """Model a user"""

    def __init__(self, first, last, username, age, location, email):
        """Initialize attributes"""
        self.first_name = first.title()
        self.last_name = last.title()
        self.username = username
        self.age = age
        self.location = location.title()
        self.email = email
    
    def describe_user(self):
        """Describes a user"""
        full_name = self.first_name + " " + self.last_name
        print(full_name + "'s profile information:")
        print("\tUsername: " + self.username)
        print("\tAge: " + str(self.age))
        print("\tLocation: " + self.location)
        print("\tEmail: " + self.email)
    
    def greet_user(self):
        """Greet a user"""
        print("Hey, " + self.first_name + "!")