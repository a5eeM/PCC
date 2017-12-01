pets = []

pet = {
    "kind": "dog",
    "owner": "Supriya"
    }
pets.append(pet)

pet = {
    "kind": "dog",
    "owner": "Megha"
    }
pets.append(pet)

pet = {
    "kind": "dog",
    "owner": "Nivedita"
    }
pets.append(pet)

for pet in pets:
    kind = pet["kind"]
    owner = pet["owner"]
    print(owner.title() + " has a pet who is a " +kind.title())
