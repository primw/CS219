from random import choice

nouns = ["mum", "dad", "dog", "hairline"]
babyMode = ["kinda weird", "not cool", "failing the vibe check", "lame"]
blondeRoast = ["obtuse", "janky", "stupid", "whack"]
chicken = ["big chungus", "an airhead", "small brain", "big idiot"]
x = True


while x:
    print("How hard do you want to be insulted?\n\t[1] - Baby Mode\n\t[2]- Starbucks Blonde Roast\n\t[3] - Rotisserie Chicken")
    userChoice = input() 

    if userChoice == "1":
        print("Your " + choice(nouns) + " is " + choice(babyMode))
    elif userChoice == "2":
        print("Your " + choice(nouns) + " is " + choice(blondeRoast))
    elif userChoice == "3":
        print("Your " + choice(nouns) + " is " + choice(chicken))

    print("Go again? (y/n)")
    option = input()
    if option == 'y':
        x = True
    else:
        x = False

    print("\n\n\n\n\n\n\n\n")
