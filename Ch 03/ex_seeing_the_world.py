location_list = ["santorini", "bora bora", "amsterdam", "norway", "iceland"]

# print in original order
print(location_list)

# print in alphabetical order without changing the order fo the original
print("\nsorted alphabetical without changing the order of original list")
print(sorted(location_list))

# print orginal
print("\n")
print(location_list)

# print in reverse alphabetical order without changing the original order
print("\nsorted reverse alphabetical order without changing the order of original list")
print(sorted(location_list, reverse=True))

# use reverse - will change order
print("\nreverse order")
location_list.reverse()
print(location_list)

# use reverse again - will change the order back to original
print("\nreverse again- change the order to original")
location_list.reverse()
print(location_list)

# use sort - will change the order
print("\nsort alphabetically changing the original order of the list")
location_list.sort()
print(location_list)

# use sort to reverse alphabetical order
print("\nsort reverse alphabetically changing the original order of the list")
location_list.sort(reverse=True)
print(location_list)