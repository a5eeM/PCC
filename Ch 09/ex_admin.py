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

class Admin(User):
    """
    Represent aspects of a User, specific to an Admin.
    """

    def __init__(self, first, last, username, age, location, email, privileges):
        """
        Initilize attributes, both parent and child class.
        """
        super().__init__(first, last, username, age, location, email)
        # child attributes
        self.privileges = privileges
    
    def show_privileges(self):
        """
        Print a statement showing the privileges of an admin.
        """
        full_name = self.first_name + " " + self.last_name
        print(full_name.title() + "'s privileges as an Admin are:")
        for privilege in self.privileges:
            print(" -" + privilege)

andrew = Admin("andrew", "jackson", "dungeon_freak", 35, "paris",
               "dungeon_freak@hotmail.com",
               ["can add post", "can delete post", "can ban user"])
andrew.show_privileges()
