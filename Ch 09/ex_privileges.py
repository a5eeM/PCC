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

class Privileges():
    """
    A simple class to hold an admin's privileges.
    """

    def __init__(self, privileges):
        """
        Initialize attribues.
        """
        self.privileges = privileges
    
    def show_privileges(self):
        """
        Print a statement showing the privileges of a user.
        """
        print("privileges are:")
        for privilege in self.privileges:
            print(" -" + privilege)

class Admin(User):
    """
    Represents aspect of a user, specific to an admin.
    """

    def __init__(self, first, last, username, age, location, email, privilege_list):
        """
        Initial attributes for both parent and child classes.
        """
        super().__init__(first, last, username, age, location, email)
        # child class attributes
        self.privilege_list = privilege_list
        self.privileges = Privileges(self.privilege_list)
       
andrew = Admin("andrew", "jackson", "dungeon_freak", 35, "paris",
               "dungeon_freak@hotmail.com",
               ["can ban user", "can add post", "can delete post"])

andrew.privileges.show_privileges()