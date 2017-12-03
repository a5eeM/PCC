# passing arguments
# position arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type.title() + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")
# order matters
describe_pet("harry", "hamster")

# keyword arguments
describe_pet(animal_type="dog", pet_name="Spark")
describe_pet(pet_name="Hazel", animal_type="dog")
