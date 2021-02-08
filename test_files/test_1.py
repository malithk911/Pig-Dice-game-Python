import random
score, user, dice = 0, "", ""


def main_loop():
    global score, user, dice

    dice = random.choice([1, 2, 3, 4, 5, 6])
    score += dice


def validation():
    global score, user, dice

    while True:
        user = input("\nEnter 'R' to roll dice or 'H' to hold :-")

        if user == "h" or user == "H":
            print("Hold!")
            print("Score: ", score)
            break

        elif user == "r" or user == "R":
            main_loop()
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
    num_players = int(input("Enter number of players:"))
    for i in range(num_players):
        validation()
        main_loop()


player()



