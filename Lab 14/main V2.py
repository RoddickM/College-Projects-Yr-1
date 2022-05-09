class CupcakeStore:
    chocolate = 24
    lemon = 15
    strawberry = 22
    vanilla = 44


def buy_cupcake():
    print("\nHow many do you want to buy?\n")


texts = "Choose a flavour between:"
texts += "\nChocolate"
texts += "\nLemon"
texts += "\nStrawberry"
texts += "\nVanilla"
texts += "\nInput: "

while True:
    flavour = hasattr(CupcakeStore, input(texts).lower())

    if flavour == True:
        print("\nHow many do you want to buy?\n")
        break
    else:
        print("\nFlavour Unavailable/Wrong Input/There is a typo\n")
