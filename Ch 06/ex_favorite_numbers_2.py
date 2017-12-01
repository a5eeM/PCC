favorite_numbers = {
    "edward": [13, 12, 6],
    "eric": [7, 6, 4],
    "carolina": [3],
    "andrew": [9, 2, 1],
    "tom": [3, 14, 99]
    }

for name, number_list in favorite_numbers.items():
    if len(number_list) == 1:
        print("\n" + name.title() + "'s favorite number is:")
        for number in number_list:
            print("\t" + str(number))
    else:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in number_list:
            print("\t" + str(number))

