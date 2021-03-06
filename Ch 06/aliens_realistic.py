# # Nesting Realistic Example

# # Make an empty list for stroing aliens

# aliens = []

# # Make 30 green aliens
# for alien_number in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)

# # show first five aliens
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # show how many aliens have been created
# print("Total number of aliens: " +str(len(aliens)))

# Changing firs three aliens
# Make an empty list for stroing aliens

aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15


# show first five aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print("Total number of aliens: " +str(len(aliens)))