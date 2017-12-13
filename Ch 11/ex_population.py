def city_country(city, country, population=0):
    """
    Store a city and a country it is in.
    """
    if population:
        return city.title() + ", " + country.title() + " - population " + str(population)
    else:
        return city.title() + ", " + country.title()
