# ROCK-PAPER-SCISSORS GAME

import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

def decide_winner(user, comp):
    if user == comp:
        return "tie"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "user"
    else:
        return "computer"

while True:
    print("\n==== ROCK PAPER SCISSORS ====")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid input. Try again.")
        continue

    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")

    winner = decide_winner(user_choice, comp_choice)
    if winner == "tie":
        print("🤝 It's a tie!")
    elif winner == "user":
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1

    print(f"🏆 Score: You = {user_score} | Computer = {computer_score}")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! 👋")
        break