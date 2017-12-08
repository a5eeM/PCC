# Importing class OrderedDict from module collections

from collections import OrderedDict

glossary = OrderedDict()


glossary["object"] = "Instance of a class."
glossary["string"] = "Any finite sequence of characters."
glossary["comment"] = "A note in a program that the language compiler/interpreter ignores."
glossary["list"] = "A collection of items in a particular order."
glossary["dictionary"] = "A collection of key-value pairs."

for word, meaning in glossary.items():
    print("\n" + word + ":" + "\n\t" + meaning)

glossary["key"] = "The firs item in a key-value pair in a dictionary."
glossary["value"] = "An item associated with a key in a dictionary."
glossary["conditional test"] = "A comparison between two values."
glossary["float"] = "A numerical value with a decimal component."
glossary["boolean expression"] = "An expression that evaluates to True or False."

for word, meaning in glossary.items():
    print("\n" + word + ":" + "\n\t" + meaning)

print(glossary)
