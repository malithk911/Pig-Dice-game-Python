import random
print("\n\n━━━━━━━━━━━━━━━━━━━━━━━━━ PIG DICE ━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
score, dice, user, bol, total_score, num_players = 0, "", "", False, [0, 0, 0, 0], 0


def player():
    global score, bol, total_score, num_players
    if num_players <= 4:
        for i in range(num_players):
            print("\n\n______ PLAYER", i + 1, "______")
            score = 0
            validation()
            total_score[i] += score
            if total_score[i] >= 100:
                bol = True
                print("\nPlayer", i + 1, "wins!\n", "\nTOTAL SCORES :-", total_score)
                break
            print("\nTOTAL SCORES :-", total_score)


def main_loop():
    global score, dice, bol, total_score
    dice = random.choice([1, 2, 3, 4, 5, 6])
    score += dice


def validation():
    global score, dice, user
    while True:
        user = input("\nEnter 'R' to roll dice or 'H' to hold :-")
        if user == "h" or user == "H":
            print("You chose to hold.", "\nScore: ", score)
            break
        elif user == "r" or user == "R":
            main_loop()
            if dice == 1:
                score = 0
                print("\nYou lose!\nResult:", dice, "\nscore:", score)
                break
            else:
                print("Result:", dice, "\nScore: ", score)


def turns():
    try:
        global num_players, score
        n = 1
        num_players = int(input("\n♦ Enter number of players:"))
        while True:
            print("\n\n━━━━━━━━━")
            print(" Turn", n)
            print("━━━━━━━━━")
            player()
            if num_players > 4:
                print("Maximum possible players is 4!")
                break
            else:
                n += 1
                if bol:
                    break
    except ValueError or TypeError:
        print("Error")


turns()
