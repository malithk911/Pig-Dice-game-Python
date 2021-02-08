import random
score, dice, user = 0, "", ""


def main_loop():
    global score, dice
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
                print("You lose!\nResult:", dice, "\nscore:", score)
                break
            else:
                print("Result:", dice, "\nScore: ", score)


def player():
    global score

    num_players = int(input("\nEnter number of players:"))

    if num_players <= 4:

        for i in range(num_players+1):
            if i == 1:
                print("\n\n______ Player", i, "______")
                score = 0
                validation()
                main_loop()
                if score >= 10:
                    print("You win!")
                    break
            elif i == 2:
                print("\n\n______ Player", i, "______")
                score = 0
                validation()
                main_loop()
                if score >= 10:
                    print("You win!")
                    break
            elif i == 3:
                print("\n\n______ Player", i, "______")
                score = 0
                validation()
                main_loop()
                if score >= 10:
                    print("You win!")
                    break
            elif i == 4:
                print("\n\n______ Player", i, "______")
                score = 0
                validation()
                main_loop()
                if score >= 10:
                    print("You win!")
                    break
    else:
        print("Maximum possible players is 4!")


player()



