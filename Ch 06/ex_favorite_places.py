favorite_places = {
    "supriya": ["santorini", "zurich", "barcelona"],
    "aseem": ["bora bora", "barcelona", "interlakken"],
    "john": ["new york", "tokyo", "shanghai"]
    }

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
    print("\n")
