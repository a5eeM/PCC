language_list = ["hindi", "punjabi", "french", "german"]

# using title() and accesing a list value by index
print(language_list[1].title())

print(language_list[-len(language_list)].title())

# using append() to add something to the list at the end
language_list.append("kannada")
print("\n")
print(language_list)

# using insert() to add something to the list anywhere
language_list.insert(2, "swiss")
print("\n")
print(language_list)

# using del to remove itme from a list
del language_list[2]
print("\n")
print(language_list)

# using pop() to remove an item from the end of the list and storing it in a variable
tough_language = language_list.pop()
print("\n")
print(language_list)
print(tough_language)

# using pop() to remove any item from a list using index
tough_language = language_list.pop(1)
print("\n")
print(language_list)
print(tough_language)

# using remove() to remove an item by value

language_list.remove("french")
print(language_list)

language_list.insert(2, "french")
very_difficult = "french"
language_list.remove(very_difficult)
print(language_list)
print("\n" + very_difficult.title() + " is very difficult to learn.")

language_list.insert(2, "french")
language_list.insert(1, "punjabi")
print(language_list)

# sorting a list permanently
language_list_perm_sort = ["swiss", "hindi", "punjabi"]
print("\n")
print(language_list_perm_sort)
language_list_perm_sort.sort()
print("\n after sort method:")
print(language_list_perm_sort)

# sorting a list reverse alphabateically
print("\nreverse sort")
language_list_perm_sort.sort(reverse=True)
print(language_list_perm_sort)

# sorting a list temporarily
print("\n")
print("before:")
print(language_list)
print("\nsort")
print(sorted(language_list))
print("\nafter")
print(language_list)

# sorting a list reverse alphabetically temporarily
print("\n")
print("before:")
print(language_list)
print("\nsort")
print(sorted(language_list, reverse=True))
print("\nafter")
print(language_list)

# reversing a list permanently
print("\n")
print(language_list_perm_sort)
language_list_perm_sort.reverse()
print("\nafter reversing")
print(language_list_perm_sort)

# getting the original after reversing permanently
print("\n")
print(language_list_perm_sort)
language_list_perm_sort.reverse()
print("\nafter reversing, getting the original")
print(language_list_perm_sort)

# finding the length of a list
language_list_length =len(language_list)
print("The length is: " + str(language_list_length) + ".")
language_list.append("dutch")
print("\nThe new length is: " + str(len(language_list)) + ".")