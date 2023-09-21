# A simple "Rock, Paper, Scissors!" game, written in Python
import random

def playRockPaperScissors():
    print("\n\nWelcome to Rock, Paper, Scissors!\n")
    print("Enter your choice below.\n")

    possibleSelections = ["Rock", "Paper", "Scissors"]
    possibleSelectionsString = ', '.join(possibleSelections)

    playerSelection = input()
    while playerSelection not in possibleSelections:
        print("\nThe selection you made was not recognized.\n")
        print("\nThe options are " + possibleSelectionsString + ".\n")
        print("\nPlease try again.\n")
        playerSelection = input()

    computerSelection = possibleSelections[random.randint(0, 2)]
    
    determineWinner(playerSelection, computerSelection)

def determineWinner(playerSelection, computerSelection):
    draw = False
    computerWon = False
    playerWon = False
    if playerSelection.lower() == "rock":
        if computerSelection.lower() == "rock":
            draw = True
        if computerSelection.lower() == "paper":
            computerWon = True
        if computerSelection.lower() == "scissors":
            playerWon = True
    if playerSelection.lower() == "paper":
        if computerSelection.lower() == "rock":
            playerWon = True
        if computerSelection.lower() == "paper":
            draw = True
        if computerSelection.lower() == "scissors":
            computerWon = True
    if playerSelection.lower() == "scissors":
        if computerSelection.lower() == "rock":
            computerWon = True
        if computerSelection.lower() == "paper":
            playerWon = True
        if computerSelection.lower() == "scissors":
            draw = True
    
    print("\nYou chose " + playerSelection + ".\n")
    print("The computer chose " + computerSelection + ".\n")
    if playerWon:
        print("You win!")
    elif draw:
        print("It was a draw!")
    elif computerWon:
        print("The computer wins!")
    else:
        print("This should not be printed.")
    print("\n")

def main():
    playRockPaperScissors()

if __name__ == "__main__":
    main()