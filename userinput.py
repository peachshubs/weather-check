import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1 
    PAPER = 2
    SCISSOR = 3

# Displaying enum values
print(RPS(2))  # PAPER
print(RPS.ROCK)  # RPS.ROCK
print(RPS['ROCK'])  # RPS.ROCK
print(RPS.ROCK.value)  # 1

# Game starts
player_choice = input("Enter \n1 for Rock \n2 for Paper \n3 for Scissors\n")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

computer = random.randint(1, 3)

# Display choices
print(f"\nYou chose {RPS(player).name}.")
print(f"Python chose {RPS(computer).name}.\n")

# Determine winner
if (player == 1 and computer == 3) or \
   (player == 2 and computer == 1) or \
   (player == 3 and computer == 2):
    print("You win!✨")
elif player == computer:
    print("Tie game!😊")
else:
    print("Python wins!🎉")
