import random
score, dice, user, bol = 0, "", "", False
total1 = 0
total2 = 0
total3 = 0
total4 = 0


def player():
    global score, bol, dice, user
    num_players = int(input("\nEnter number of players:"))
    if num_players <= 4:
        for i in range(num_players):
            print("\n\n______ Player", i + 1, "______")
            score = 0

            dice = random.choice([1, 2, 3, 4, 5, 6])
            score += dice

            if score >= 100:
                bol = True
                break

            if dice == 1:
                score = 0
                print("\nYou lose!\nResult:", dice, "\nscore:", score)
                break
            else:
                print("Result:", dice, "\nScore: ", score)

            if bol:
                print("\nYou win!", "\nScore:", score)
                break
    else:
        print("Maximum possible players is 4!")


player()
