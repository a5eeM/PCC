# using list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)


# more advanced but to print the squares
print("\n")
squares = [print(value**2) for value in range(1, 11)]
