import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        def decisionW(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉You Win!"
            elif player == computer:
                return "😕Tie Game!"
            else:
                python_wins += 1
                return "🐍Python Wins!"

        winner = decisionW(player, computer)
        print(winner)

        nonlocal game_count
        game_count += 1
        print("\nGame count:" + str(game_count))
        print("\nPlayer Wins:" + str(player_wins))
        print("\nPython Wins:" + str(python_wins))

        print("\nPlay Again?")

        while True:
            playagain = input("\ny for Yes or\nQ to Quit!\n\n ")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print('🎉\nCelebrate💖')
            print("Thank you for playing ravs game!\n")
            sys.exit("Bye! 🤞")
    return play_rps

play = rps()
play()


