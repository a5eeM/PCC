def make_sandwich(*items):
    """
    Make a sandwich with the list of items
    """
    print("\nMaking your sandwich with the following items:")
    for item in items:
        print("- " + item)
    
make_sandwich("cheese", "cucumber", "tomatoes")
make_sandwich("chicken", "cheese")
make_sandwich("cheddar cheese", "peanut butter", "strawberry jam")
