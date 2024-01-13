import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):  # to correct the intend click Tab in

        ROCK = 1
        PAPER = 2
        SCISSORS = 3

        # print(RPS(2))
        # print(RPS.ROCK)
        # print(RPS['ROCK'])
        # print(RPS.ROCK.value)
        # sys.exit()

    playerchoice = input(
        "\nEnter... \n1 For Rock, \n2 For Paper, or \n3 For Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)
    print("\nYou chose" + str(RPS(player)).replace('RPS.', ' ').
          title() + ".")
    print("\nPython chose" + str(RPS(computer)
                                 ).replace('RPS.', ' ').title() + ".\n")

    if player == 1 and computer == 3:

        print("🎉You Win!")
    elif player == 2 and computer == 1:
        print("🎉You Win!")
    elif player == 3 and computer == 2:
        print("🎉You Win!")
    elif player == computer:
        print("😕Tie Game!")
    else:
        print("🐍Python Wins!")

    print("\nPlay Again?")

    while True:
        playagain = input("\ny for Yes or\nQ to Quit!\n\n ")
        if playagain.lower() not in ["y", "Q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print('🎉\nCelebrate💖')
        print("Thank you for playing ravs game!\n")
        sys.exit("Bye! 🤞")


play_rps()
