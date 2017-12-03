# providing a defaut alue for parameter

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")

describe_pet("willie")
describe_pet("timmy", "cat")
describe_pet(animal_type="rat", pet_name="scabbers")
