def addition(first, second):
    """
    Addition of two numbers.
    """
    try:
        first = int(first)
        second = int(second)
    except ValueError:
        print("Sorry, both inputs should be numbers.")
    else:
        print("Result: " + str(first + second))

first_num = input("Enter first number: ")
second_num = input("Enter second number: ")
addition(first_num, second_num)
