import random
print("\n\n━━━━━━━━━━━━━━━━━━━━━━━━━ PIG DICE GAME ━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
score, dice, user, bol, total_score, num_players = 0, "", "", False, [0, 0, 0, 0], 0


def main_loop():
    try:
        global num_players, score, bol, user, dice
        n = 1  # n == number of turns
        num_players = int(input("\n♦ Enter number of players:"))
        while True:
            if num_players > 4:
                print("\nMaximum possible players is 4!")
                break
            elif num_players == 1:
                print("\nMinimum possible players is 2!")
                break
            else:
                print("\n\n━━━━━━━━━ \n Turn", n, "\n━━━━━━━━━")
                if num_players <= 4:
                    for i in range(num_players):
                        print("\n\n__________________________ PLAYER", i + 1, "_________________________")
                        score = 0  # score starts with 0 on every iteration of the for loop
                        while True:
                            user = input("\nEnter 'R' to roll dice or 'H' to hold :-")
                            if user == "h" or user == "H":
                                print("\nHOLDING......", "\nTurn Score:", score)
                                break
                            elif user == "r" or user == "R":
                                dice = random.choice([1, 2, 3, 4, 5, 6])
                                score += dice
                                if dice == 1:
                                    score = 0
                                    print("\nPLAYER", i + 1, "LOST THE TURN!\nResult:", dice, "\nscore:", score)
                                    break
                                else:
                                    print("Result:", dice, "\nTurn Score:", score)
                            else:
                                print("Error! Invalid input.")
                        total_score[i] += score  # Turn score will only be added to the total score when the user holds.
                        if total_score[i] >= 100:
                            bol = True
                            print("\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            print(" PLAYER", i + 1, "WINS!\n", "\n TOTAL SCORES :-", total_score)
                            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            break
                        print("\n\nTOTAL SCORES :-", total_score)
                n += 1  # iterate number of turns
                if bol:  # if score >= 100
                    break
    except ValueError or TypeError:
        print("Error! Invalid input.")


main_loop()
