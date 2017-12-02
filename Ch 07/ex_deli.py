sandwich_orders = ["bacon", "bagel toast", "baked bean", "bologna", 
                   "british rail", "pastrami"]

finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print("I made your " + sandwich_order.title() + " sandwich.")

    finished_sandwiches.append(sandwich_order)

print("\nSandwiches made today:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title() + " sandwich")
