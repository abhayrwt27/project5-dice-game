import random

player_score = 0
computer_score = 0
history = []

print("Advanced Dice Game")

while True:

    press = input("\nPress Enter to roll the dice....")

    if press != "":
        print("Just press Enter")
        continue

    # Roll Dice
    player_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    print("You rolled:", player_roll)
    print("Computer rolled", computer_roll)

    history.append((player_roll, computer_roll))

    if(player_roll > computer_roll):
        print("You win this round.")
        player_score += 1

    elif(player_roll < computer_roll):
        print("Computer wins this round.")
        computer_score += 1

    else:
        print("It's a tie!")

    # Show scores
    print(f"\n Score")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")

    # Play again
    choice = input("\nPlay again? (yes/no): ").lower()

    if choice != "yes":
        break

#Final Result
print("\n Final result")

if player_score > computer_score:
    print("You won the game!")

elif player_score < computer_score:
    print("Computer won the game!")

else:
    print("Match Draw!")

# Roll History
print("\n Roll History")
for round_num, rolls in enumerate(history, start=1):
    print(f"Round {round_num}: You={rolls[0]}, Computer={rolls[1]}")

