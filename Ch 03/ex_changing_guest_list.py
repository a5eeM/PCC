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