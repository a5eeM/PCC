# Importing OrderedDict from module collections

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = ["python", "rust"]
favorite_languages["sarah"] = ["c"]
favorite_languages["john"] = ["c++"]
favorite_languages["edward"] = ["ruby", "java"]
favorite_languages["phil"] = ["javascript", "python"]

for name, langage_list in favorite_languages.items():
    if len(langage_list) == 1:
        print(name.title() + "'s favorite language is:")
        for language in langage_list:
            print(" - " + language.title())
    else:
        print(name.title() + "'s favorite languages are:")
        for language in langage_list:
            print(" - " + language.title())
