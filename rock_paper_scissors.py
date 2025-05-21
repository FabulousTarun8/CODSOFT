import random

round = 1
player_score = 0
computer_score = 0

emojis = {
    "r": "🪨",
    "p": "📃",
    "s": "✂️"
}

def play():
    while True:
        choice = input("Rock, paper or scissors? (r/p/s): ").lower()
        if choice not in list(emojis.keys()):
            print("Invalid choice!")
            continue
        computer = random.choice(list(emojis.keys()))
        print(f"You chose {emojis[choice]}.")
        print(f"Computer chose {emojis[computer]}.")
        if ((choice == "r" and computer == "s") or
                (choice == "p" and computer == "s") or
                (choice == "s" and computer == "p")):
            print("You win.")
            return 1
        elif choice == computer:
            print("Tie.")
            return 0
        else:
            print("You lose.")
            return -1


while round != 4:
    print(f"ROUND {round}")
    result = play()
    if result == 1:
        player_score += 1
    elif result == -1:
        computer_score += 1
    round += 1
    print("Player score:", player_score)
    print("Computer score:", computer_score)
    print()

if computer_score > player_score:
    print("Computer won the match!")
elif player_score > computer_score:
    print("Player won the match!")
else:
    print("It was a tie!")

