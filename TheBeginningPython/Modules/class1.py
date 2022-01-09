def makepizza(size, *toppings):
    """Creates and outputs the size and toppings of the pizza"""
    print(f"The pizza size is {size} and the toppings are: ")
    for top in toppings:
        print(f"\n {top}")