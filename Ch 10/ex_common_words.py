def common_words(filename, word):
    """
    Reads the file and determines how many times
    the word 'word' appears in each file.
    """

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry " + filename + " doesn't exist!"
        print(msg)
    else:
        number = contents.lower().count(word)
        print(filename + " consists of " + str(number) + " " + word + "'s.")

files = ["alice.txt", "raffles.txt", "patsy.txt"]
for file in files:
    common_words(file, "the")
