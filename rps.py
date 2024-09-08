import random 

class RockPaperScissors:
    def __init__(self):
        pass
    
    def play_game():
        print("\nWelcome to Rock, Paper, Scissors!")
        rpc = ["rock", "paper", "scissors"]

        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        computer_choice = random.choice(rpc)

        if user_choice not in rpc:
            print("Invalid Input: " + user_choice)
            RockPaperScissors.play_game()  # Restart the game if input is invalid
            return         

        print("User chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
            return

        if (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
            print("User wins!")

        else:
            print("Computer wins!")
    
    def play_again():
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            RockPaperScissors.play_game()
        else:
            print("Thanks for playing!")
            return
    
RockPaperScissors.play_game()
RockPaperScissors.play_again()