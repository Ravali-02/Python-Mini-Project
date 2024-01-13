import sys
import random


def guessnum_game(name="Ravali"):
    game_count = 0
    player_wins = 0

    def play_guessnum():
        nonlocal name
        nonlocal player_wins
        nonlocal game_count

        playerchoice = input(
            f"{name}, Guess Which Number I'm Thingking rightnow like......1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name} Please enter 1, 2, or 3. otherwise it won't work")
            return play_guessnum()

        computerchoice = random.choice("123")

        print(f"\n{name}, You Chose {playerchoice}.")
        print(
            f"\nI was Thinking about the number {computerchoice}.\n"

        )
        player = int(playerchoice)
        computer = int(computerchoice)

        def decisionW(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉{name} You Win!"
            else:
                return f"Sorry, {name}. Better Luck next time.😢"

        winner = decisionW(player, computer)

        print(winner)
        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}")
        print(f"\n{name} Wins: {player_wins}")
        print(f"\nYour winning Percentage: {player_wins/game_count:.2%}")

        print(f"\nPlay Again, {name}?")

        while True:
            playagain = input("\ny for Yes or\nQ to Quit!\n\n ")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guessnum()
        else:
            print('🎉\nCelebrate💖')
            print("Thank you for playing ravs game!\n")
        if __name__ == "__main__":
            sys.exit(f"Bye {name}!🤞")
        else:
            return

    return play_guessnum()


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
    guessnum_game = guessnum_game(args.name)
    guessnum_game()
