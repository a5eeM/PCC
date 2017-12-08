# Admin module for ex 9-12
"""
A set of classes to represent admin and admin privileges.
"""
from ex_user_module_mm import User

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