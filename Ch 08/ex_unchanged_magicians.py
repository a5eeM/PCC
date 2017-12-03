def show_magicians(names):
    """Displays name of the magicians"""
    for name in names:
        print(name)

# def make_great(names):
#     """
#     Modifies the list of magicians by adding 'the Great'
#     to each magician's name
#     """
#     for val in range(len(names)):
#         names[val] = names[val] + " the Great"

def make_great(names):
    """
    Modifies the list of magicians by adding 'the great'
    to each magician's name
    """

    great_magicians = []

    while names:
        name = names.pop()
        great_magician_name = name + " the Great"
        great_magicians.append(great_magician_name)
    for great_magician_name in great_magicians:
        names.append(great_magician_name)
    new_names = names
    return new_names


magician_names = ["Magician Philip", "Harry Houdini", "David Blaine"]
show_magicians(magician_names)

new_magician_names = make_great(magician_names[:])
print("\nGreat magicians:")
show_magicians(new_magician_names)
print("\nOriginal magicians")
show_magicians(magician_names)