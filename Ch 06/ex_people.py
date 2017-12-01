andrew = {
    "first_name": "andrew",
    "last_name": "johnson",
    "age": 43,
    "city": "kansas"
    }

john = {
    "first_name": "john",
    "last_name": "hardy",
    "age": 32,
    "city": "palo alto"
    }

carolina = {
    "first_name": "carolina",
    "last_name": "hopper",
    "age": 27,
    "city": "new york"
    }

people = [andrew, john, carolina]

for user in people:
    first_name = user["first_name"]
    last_name = user["last_name"]
    full_name = first_name + " " + last_name
    print("\n" + full_name.title() + ":")
    print("\tAge: " + str(user["age"]))
    print("\tLocation: " + user["city"].title())

