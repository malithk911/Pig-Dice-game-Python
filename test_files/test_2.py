import random


def main_loop(score):

    dice = random.choice([1, 2, 3, 4, 5, 6])
    score += dice


def validation(score, dice):

    while True:
        user = input("\nEnter 'R' to roll dice or 'H' to hold :-")

        if user == "h" or user == "H":
            print("Hold!")
            print("Score: ", score)
            break

        elif user == "r" or user == "R":
            main_loop(score)
            if dice == 1:
                score = 0
                print("Result:", dice)
                print("You lose!")
                print("score:", score)
                break
            else:
                print("Result:", dice)
                print("Score: ", score)


def player():
    score_1, dice_1 = 0, 0
    score_2, dice_2 = 0, 0
    score_3, dice_3 = 0, 0
    score_4, dice_4 = 0, 0

    num_players = int(input("Enter number of players:"))
    if num_players <= 4:
        for i in range(num_players+1):
            if i == 1:
                print("\nplayer 1")
                validation(score_1, dice_1)
                main_loop(score_1)
            elif i == 2:
                print("\nplayer 2")
                validation(score_2, dice_2)
                main_loop(score_2)
            elif i == 3:
                print("\nplayer 3")
                validation(score_3, dice_3)
                main_loop(score_3)
            elif i == 4:
                print("\nplayer 4")
                validation(score_4, dice_4)
                main_loop(score_4)
    else:
        print("Maximum possible players is 4!")


player()



