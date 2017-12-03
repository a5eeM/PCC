def make_tshirt(message="I love Python", size="large"):
    """Describe the size and message of a t shirt"""
    print("\nThe size of the t-shirt to be made is " + str(size) + ".")
    print("The t-shirt will say '" + message + "'.")

make_tshirt()
make_tshirt(size="medium")
make_tshirt(message="life runs on code", size="small")

