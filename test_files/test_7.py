import random
score, dice, user, bol, num_players, total_score = 0, "", "", False, 0, 0


def main_loop():
    global score, dice, bol, total_score
    dice = random.choice([1, 2, 3, 4, 5, 6])
    score += dice
    total_score += score
    if total_score >= 50:
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
    global score, bol, num_players, total_score
    if num_players <= 4:
        for i in range(num_players):
            print("\n\n______ Player", i + 1, "______")
            score = 0
            validation()
            main_loop()
            if bol:
                print("\nYou win!", "\nScore:", score)
                break
    else:
        print("Maximum possible players is 4!")


def turns():
    global bol, num_players, total_score
    n = 1
    num_players = int(input("\nEnter number of players:"))
    while True:
        print("\n\nTurn", n)
        player()
        n += 1
        if bol:
            print("\nYou win!", "\nScore:", score)
            break


turns()
