import random
score, dice, user, bol = 0, "", "", False


def main_loop():
    global score, dice, bol
    dice = random.choice([1, 2, 3, 4, 5, 6])
    score += dice
    if score >= 100:
        bol = True


def validation():
    global score, dice, user
    while True:
        user = input("\nEnter 'R' to roll dice or 'H' to hold :-")
        if user == "h" or user == "H":
            print("You chose to hold.", "\nScore: ", score)
            break
        elif user == "r" or user == "R":
            main_loop()
            if bol:
                break
            if dice == 1:
                score = 0
                print("\nYou lose!\nResult:", dice, "\nscore:", score)
                break
            else:
                print("Result:", dice, "\nScore: ", score)


def player():
    global score, bol
    num_players = int(input("\nEnter number of players:"))
    if num_players <= 4:
        for i in range(num_players):
            print("\n\n______ Player", i + 1, "______")
            score = 0
            validation()

            if bol:
                print("\nYou win!", "\nScore:", score)
                break
    else:
        print("Maximum possible players is 4!")


player()
