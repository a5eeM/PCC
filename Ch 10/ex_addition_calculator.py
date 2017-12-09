def addition(first, second):
    """
    Adding two numbers.
    """
    try:
        result = int(first) + int(second)
    except ValueError:
        print("Sorry, both inputs should be numbers!!")
    else:
        print("Result: " + str(result))

while True:
    print("\nEnter 'q' to quit.")
    first = input("Enter first number: " )
    if first == "q":
        break
    second = input("Enter second number: ")
    addition(first, second)


