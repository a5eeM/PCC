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
        magician_names.append(great_magician_name)


magician_names = ["Magician Philip", "Harry Houdini", "David Blaine"]
make_great(magician_names)
show_magicians(magician_names)