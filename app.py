# write a minigame for rock paper scissors
# rules is Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# ask user to input their choice
# computer will randomly choose one
# compare the result and print out who wins
# ask user if they want to play again
# if yes, play again
# if no, exit the game
# if invalid input, ask user to input again
# use screen function to show result 
# use random function to generate computer's choice
# use a function to compare the result
# use a function to ask user to play again

import random
import time
import os
import sys

def screen():
    print("Rock Paper Scissors")
    print("Rules: Rock beats scissors. Scissors beat paper. Paper beats rock.")
    print("Please input your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

def compare(user, computer):
    if user == computer:
        print("Draw!")
    elif user == 1:
        if computer == 2:
            print("Computer wins!")
        else:
            print("You win!")
    elif user == 2:
        if computer == 3:
            print("Computer wins!")
        else:
            print("You win!")
    elif user == 3:
        if computer == 1:
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid input!")

def play_again():  
    while True:
        print("Do you want to play again? (y/n)")
        choice = input()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input!")

def main():
    while True:
        screen()
        user = int(input())
        if user == 4:
            sys.exit()
        elif user > 4 or user < 1:
            print("Invalid input!")
            continue
        computer = random.randint(1, 3)
        print("Computer is choosing...")
        time.sleep(1)
        print("Computer chooses: " + str(computer))
        compare(user, computer)
        if not play_again():
            break
        os.system("cls")

if __name__ == "__main__":
    main()

    