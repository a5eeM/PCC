usernames = ["eric", "admin", "andrew", "carolina", "steve"]

for username in usernames:
    if username == "admin":
        print("Hello " + username + ", would you like to see a status report ?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again.")
