def make_car(manufacturer_name, model_name, **car_info):
    """
    Build a car using the information we know about the car.
    """
    car = {}
    car["manufacturer"] = manufacturer_name.title()
    car["model"] = model_name.title()
    for key, value in car_info.items():
        car[key] = value
    return car

outback = make_car("subaru", "outback", color="blue", tow_package=True)
print(outback)

accord = make_car("honda", "accord", year=1991, color="white",
                  headlights="popup")
print(accord)
