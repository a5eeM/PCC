favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
    }

print("Sarah's favorite language is " +
      favorite_languages["sarah"].title() +
      ".")
# for name, language in favorite_languages.items()
for key, value in favorite_languages.items():
    print("\nName: " + key)
    print("Favorite Language: " + value)
    print(key.title() + "'s favorite language is " + value.title() + ".")

# if we only are interested in keys
print("\n")
for name in favorite_languages.keys():
    print(name.title())

# looping through keys is the default behavious when looping through a dictionary
print("\n")
for name in favorite_languages:
    print(name.title())

# accessing the value of the key without using for key, value in..
print("\n")

friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ". I see your favorite language is " +
              favorite_languages[name].title() + "!")

# to find if a particular person took the poll of favorite languages

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")

if "erin" not in favorite_languages:
    print("Erin, please take our poll!")