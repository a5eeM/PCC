# checking whether a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

print(user in banned_users)
print(user not in banned_users)