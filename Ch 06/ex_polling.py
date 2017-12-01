favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title())

people_list = ["tom", "jen", "josh", "andrew", "sarah", "carolina", "matt"]

print("\n")
for people in people_list:
    if people in favorite_languages.keys():
        print("Thank you, " + people.title() + " for taking the poll.")
    else:
        print(people.title() + ", you are invited to take the poll!")
