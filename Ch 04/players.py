# slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# another slice
print(players[1:4])

# another one, if first index is omitted, python assumes it has to start from 0
print(players[:4])

# another one, if second index is omitted, python prints till and inclusing the last item
print(players[2:])

# using negative index 
print(players[-3:])
print(players[-len(players):])

# looping through a subset

print("\n")
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
