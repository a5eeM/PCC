# rivers

rivers = {
    "nile": "egypt",
    "ganges": "india",
    "fraser": "canada",
    "thames": "england",
    "mississippi": "united states"
    }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + "\n")

print("Following rivers are in the Dictionary:")
for river in rivers.keys():
    print("- " + river.title())

print("\n")

print("Following countries are in this Dictionary:")
for country in rivers.values():
    print("- " + country.title())

