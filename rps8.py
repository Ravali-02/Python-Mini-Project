import sys
import random
from enum import Enum


def rps(name="Ravali"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
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
            f"{name} \nPlease Enter... \n1 For Rock, \n2 For Paper, or \n3 For Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name} Please enter 1, 2, or 3. otherwise it won't work")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)
        print(f"\nYou chose {str(RPS(player)).replace('RPS.', ' ').title()}.")
        print(
            f"\nPython chose {str(RPS(computer)).replace('RPS.', ' ').title()}.\n")

        def decisionW(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉{name} You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉{name} You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{name} You Win!"
            elif player == computer:
                return "😕Tie Game!"
            else:
                python_wins += 1
                return f"{name} 🐍Python Wins!\nSorry, {name}...😉"

        winner = decisionW(player, computer)
        print(winner)

        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"\n{name} Wins: {player_wins}")
        print(f"\nPython Wins: {python_wins}")

        print(f"\nPlay Again, {name}?")

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
            sys.exit(f"Bye {name}!🤞")
    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    rock_paper_scissiors = rps()
    rock_paper_scissiors()
