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
        self.login_attempts = 0
    
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
    
    def read_login_attempts(self):
        """
        Print login_attempta for a particular user.
        """
        print(self.first_name + " has made " + str(self.login_attempts) +
              " login attempts!")

    def increment_login_attempts(self):
        """
        Increment the logging attempts by 1.
        """
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """
        Reset login attempts to 0.
        """
        self.login_attempts = 0

rohit = User("rohit", "verma","dungeon_master", 29, "paris",
             "dungeon_master@hotmail.com")

andrew = User("andrew", "johnson", "dungeon_freak", 35, "new york city",
              "dungeon_freak@hotmail.com")
rohit.greet_user()
rohit.describe_user()
andrew.greet_user()
andrew.describe_user()
rohit.increment_login_attempts()
andrew.increment_login_attempts()
rohit.increment_login_attempts()
andrew.increment_login_attempts()
andrew.increment_login_attempts()
rohit.read_login_attempts()
andrew.read_login_attempts()
rohit.reset_login_attempts()
andrew.reset_login_attempts()
rohit.read_login_attempts()
andrew.read_login_attempts()
