guest_list = ["issac newton", "albert einstein", "nikola tesla"]

# inviting newton
message = "Dear " + guest_list[0].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting einstein
message = "Dear " + guest_list[1].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting tesla
message = "Dear " + guest_list[2].title() + ", you are invited for Dinner tomorrow ar 8pm"
print(message)

# tesla can't make it
print(guest_list[2].title() + " won't be able to make it tomorrow.")

# modify the guest_list
guest_list[2] = "elon musk"

# sending invites again
# inviting newton
message = "Dear " + guest_list[0].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting einstein
message = "Dear " + guest_list[1].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting musk
message = "Dear " + guest_list[2].title() + ", you are invited for Dinner tomorrow ar 8pm"
print(message)

# more space for guests
print("Found a bigger table, so inviting new guests!!")

guest_list.insert(0, "alan turing")
guest_list.insert(2, "sergey brin")
guest_list.append("larry page")

# new invites
# inviting turing
message = "Dear " + guest_list[0].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting newton
message = "Dear " + guest_list[1].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting brin
message = "Dear " + guest_list[2].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting einstein
message = "Dear " + guest_list[3].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# inviting musk
message = "Dear " + guest_list[4].title() + ", you are invited for Dinner tomorrow ar 8pm"
print(message)

# inviting page
message = "Dear " + guest_list[5].title() + ", you are invited for Dinner tomorrow at 8pm"
print(message)

# JUST" FOUND OUT - table won't be coming in time, have to pop
print("Due to table not arriving on time, only two people can be invited to the Dinner tomorrow")

# sorry for page
popped_guest = guest_list.pop()
message = "I am deeply sorry " + popped_guest + ", I can not invite you for tomorrow's Dinner"
print(message)

# sorry for musk
popped_guest = guest_list.pop()
message = "I am deeply sorry " + popped_guest + ", I can not invite you for tomorrow's Dinner"
print(message)

# sorry for einstein
popped_guest = guest_list.pop()
message = "I am deeply sorry " + popped_guest + ", I can not invite you for tomorrow's Dinner"
print(message)

# sorry for brin
popped_guest = guest_list.pop()
message = "I am deeply sorry " + popped_guest + ", I can not invite you for tomorrow's Dinner"
print(message)

# invite still holds for the first two guests
# inviting turing
message = "Dear " + guest_list[0].title() + ", you are still invited for Dinner tomorrow at 8pm"
print(message)

# inviting newton
message = "Dear " + guest_list[1].title() + ", you are still invited for Dinner tomorrow at 8pm"
print(message)

# after dinner
del guest_list[1]
del guest_list[0]
print(guest_list)
