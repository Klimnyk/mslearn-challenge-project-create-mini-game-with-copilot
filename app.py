import random
import sys

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock (r), paper(p), scissors(s)): ")
        choice = choice.lower()

        if choice in ["rock", "paper", "scissors", "r","p","s"]:
            if choice == "r" or choice == "rock":
                choice = "rock"
                
            elif choice == "p" or choice == "paper":
                choice = "paper"
                
            elif choice == "s" or choice == "scissors":
                choice = "scissors"
                
            return choice
        else:
            print("Invalid choice. Please enter either rock (r), paper(p), scissors(s).")
        


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    player_score = 0  # Initialize player score
    player_wins = 0  # Initialize player wins
    player_losses = 0  # Initialize player losses
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            player_score += 1  # Increment player score if they win
            player_wins += 1  # Increment player wins
        elif result == "Computer wins!":
            player_score -= 1   # Decrement player score if they lose
            player_losses += 1  # Increment player losses
        
        play_again = input("Do you want to play again? yes(y) /no(n): ")
        if play_again.lower() not in ["yes", "y"]:
            break
    
    print(f"Your final score is: {player_score}")  # Display player score at the end of the game
    print(f"You won {player_wins} times and lost {player_losses} times.")  # Display player wins and losses

play_game()
