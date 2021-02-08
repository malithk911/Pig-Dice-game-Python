import random
score, dice, user, bol, num_players = 0, "", "", False, 0
scores = [0, 0, 0, 0]


def main_loop():
    global score, dice, bol, scores
    dice = random.choice([1, 2, 3, 4, 5, 6])
    score += dice
    if score >= 100:
        bol = True


def validation():
    global score, dice, user, scores
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
    global score, bol, num_players, scores
    if num_players <= 4:
        for i in range(num_players):
            print("\n\n______ Player", i + 1, "______")
            score = scores[i]
            validation()
            main_loop()
            scores[i] += score
            print("total", scores[i])
            if bol:
                print("\nYou win!", "\nScore:", score)
                break
    else:
        print("Maximum possible players is 4!")


def turns():
    global bol, num_players
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
