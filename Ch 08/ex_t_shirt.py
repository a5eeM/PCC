def make_tshirt(size, message):
    """Describe the size and message of a t shirt"""
    print("\nThe size of the t-shirt to be made is " + str(size) + ".")
    print("The t-shirt will say '" + message + "'." )

make_tshirt(40, "Just Do It")
make_tshirt("large", "life runs on code")
# keyword arguments
make_tshirt(message="Eat, Sleep, Code, Repeat", size="medium")
