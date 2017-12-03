def city_country(city, country):
    """Returns a city and the country it is in."""
    return city.title() + ", " + country.title()


city_info = city_country("santiago", "chile")
print(city_info)
city_info = city_country("new delhi", "india")
print(city_info)
city_info = city_country("barcelona", "spain")
print(city_info)
