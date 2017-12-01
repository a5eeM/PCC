# sorting the dictionary 
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# looping through the values
print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# no repeats - use set
print("\n")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
