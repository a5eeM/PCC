cities = {
    "santorini": {
        "country": "greece",
        "population": 15550,
        "fact": "There is so little rain on the island of Santorini, that" +
                " wine is more plentiful than water."
        },
    "bora bora": {
        "country": "france",
        "population": 8800,
        "fact": "There are hundreds of underwater species around Bora Bora."
        },
    "new york": {
        "country": "united states of america",
        "population": 8538000,
        "fact": "New York sets train tracks on fire to keep them free of ice" +
                " in the winter."
        }
    }

for city, city_info in cities.items():
    print("\n" + city.title() + ":")
    print(" - Located in: " + city_info["country"].title())
    print(" - Population: " + str(city_info["population"]))
    print(" - Random Fact about " + city.title() + ": " + city_info["fact"])

