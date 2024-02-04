import random

choices = ["Rock", "Paper", "Scissors"]

def rockPaperScissors():
    playersChoice = str(input("Enter Either Rock, Paper, Scissors: ").capitalize())
    while playersChoice not in choices:
        playersChoice = str(input("Enter Either Rock, Paper, Scissors: ").capitalize())
    computersChoice = choices[random.randrange(0,3)]

    if (playersChoice == "Rock" and computersChoice == "Paper"):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Computer Won")
    elif (playersChoice == "Paper" and computersChoice == "Scissors"):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Computer Won")
    elif (playersChoice == "Scissors" and computersChoice == "Rock"):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Computer Won")
    elif (playersChoice == "Rock" and computersChoice == "Scissors"):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Player Won")
    elif (playersChoice == "Paper" and computersChoice == "Rock"):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Player Won")
    elif (playersChoice == "Scissors" and computersChoice == "Paper"):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Player Won")
    elif (playersChoice == computersChoice):
        print("Computers Choice ({}) vs Players Choice ({})".format(computersChoice, playersChoice))
        print("Tie")

while True:
    rockPaperScissors()
    continueChoice = input("Do you wish to continue [y/n]: ").casefold()
    if continueChoice == "n":
        break
