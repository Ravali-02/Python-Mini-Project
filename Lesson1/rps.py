import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()
Playerchoice = input(
    "Enter... \n1 For Rock, \n2 For Paper, or \n3 For Scissors\n\n")
player = int(Playerchoice)
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)
print("")
print("your choose" + str(RPS(player)).replace('RPS.', ' ') + ".")
print("Python choose" + str(RPS(computer)).replace('RPS.', ' ') + ".")
print("")
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
