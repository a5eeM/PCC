current_users = ["Eric", "carolina", "steve", "andrew", "tom"]
new_users = ["john", "eric", "Andrew", "gabriel", "tony", "ToM"]
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user + " is already taken, please enter a new user name")
    else:
        print(new_user + " is available")
