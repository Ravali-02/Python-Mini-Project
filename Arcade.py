import sys

from rps8 import rps
from guessnum_game import guessnum_game


def Play_Game(name="Ravali"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}m Welcome Back to Arcade Menu...")

        playerchoice = input(
            f"\nPlease Choose a Game which you want to Play out of Both:\n1: Rock Paper Scissors\n 2: Arcade\n\nor Press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name} Please enter 1, 2, or 3. otherwise it won't work")
            return Play_Game(name)

        welcome_back = True

        if playerchoice == "1":
            rps8 = rps()
            rps8()
        elif playerchoice == "2":
            guessnum_game = guessnum_game(name)
            guessnum_game()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")


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

    print(f"\n{args.name}, Welcome to the Arcade! 😎")
    Play_Game(args.name)
