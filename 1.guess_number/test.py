import random


turnsToPlay = 5
randomNumber = random.randrange(1, 101)


def chooseRandomNumber():
    print(
        "Welcome to the game. You have "
        + str(turnsToPlay)
        + " turns guess the Number.Start!!"
    )


def isUserGuessValid(user_guess: str) -> bool:
    valid_User_Guess: int
    try:
        valid_User_Guess = int(user_guess)
    except:
        print("Input is not valid\n Input Should Be A Number")
        return False

    if valid_User_Guess > 0 and valid_User_Guess < 101:
        return True
    else:
        print("Input is not valid\n Input Should be between the range of 1 to 100")
        return False


chooseRandomNumber()
while turnsToPlay > 0:
    user_guess: str = input("Your Guess: ")
    if isUserGuessValid(user_guess):
        valid_User_Guess = int(user_guess)
        if valid_User_Guess == randomNumber:
            print("Correct!! --- you WIINNNN!! --- :)")
            break
        else:
            turnsToPlay = turnsToPlay - 1
            advice: str = "The Random Number is Greater than you guess :|"

            if valid_User_Guess > randomNumber:
                advice = "The Random Number is Less than you guess :|"

            print(
                "Wrong... --- You have "
                + str(turnsToPlay)
                + " turn to guess --- "
                + advice
            )
else:
    print("you lost --- ran out of turns --- :(")

print("The Random Number Was: " + str(randomNumber))
