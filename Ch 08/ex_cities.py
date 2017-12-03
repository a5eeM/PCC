def descibe_city(city, country="Spain"):
    """Describe a city and the country in which it it"""
    print("\n" + city.title() + " is in  " + country.title() + ".")

descibe_city("barcelona")
descibe_city("seville")
descibe_city(city="New Delhi", country="India")
descibe_city("Reykjavik", "Iceland")
