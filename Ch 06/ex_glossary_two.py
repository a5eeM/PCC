glossary = {
    "object": "In the class-based object-oriented programming paradigm, 'object' " +
              "refers to a particular instance of a class where the object can " +
              "a combination of variables, functions, and data structures.",
    "string": "Any finite sequence of charactes.",
    "comment": "A note in a program that the language compiler/interpreter ignores.",
    "list": "A collection of items in a particular order",
    "dictionary": "A collection of key-value pairs."
    }

for word, meaning in glossary.items():
    print("\n" + word + ":" + "\n\t" + meaning)

glossary["key"] = "The first item in a key-value pair in a dictionary."
glossary["value"] = "An item associated with a key in a dictionary."
glossary["conditional test"] = "A comparison between two values."
glossary["float"] = "A numerical value with a decimal component."
glossary["boolean expression"] = "An expression that evaluates to True or False."

for word, meaning in glossary.items():
    print("\n" + word + ":" + "\n\t" + meaning)

print(glossary)
