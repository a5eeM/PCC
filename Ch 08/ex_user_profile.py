def build_profile(first, last, **user_info):
    """
    Build a user profile with the information we know about a user.
    """
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("john", "edwards", location="new york city",
                             age=29, gender="male", nationality="British")

print(user_profile)
