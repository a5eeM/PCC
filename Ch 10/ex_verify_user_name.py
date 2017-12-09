import json

def get_stored_username():
    """
    Get stored username if available.
    """
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """
    Prompt for a new username.
    """
    filename = "username.json"
    username = input("What is your name ? ")
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username

def check_user_name():
    """
    Check the user name.
    """
    username = get_stored_username()
    is_username = input("Is " + username + " your username ? (yes/no) ")
    if is_username == "yes":
        return True

def greet_user():
    """
    Greet the user by name.
    """
    username = get_stored_username()
    if check_user_name():
        print("Welcome back, " + username + "!")
        return

    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")

greet_user()