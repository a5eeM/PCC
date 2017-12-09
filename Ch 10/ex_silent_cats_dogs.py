def file_reader(filename):
    """
    Read the file and print it's content
    """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry " + filename + " doesn't exist or is missing!"
        # print(msg)

        # failing silently
        pass
    else:
        print(contents)

files = ["cats.txt", "dogs.txt"]
for file in files:
    file_reader(file)