import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.score = {"player": 0, "computer": 0}
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def get_player_choice(self):
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        while choice not in self.choices:
            choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
        return choice

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            return "player"
        else:
            return "computer"
    
    def update_score(self, winner):
        if winner == "player":
            self.score["player"] += 1
        elif winner == "computer":
            self.score["computer"] += 1

    def play_round(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}.")

        winner = self.determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        else:
            print(f"{winner.capitalize()} wins this round!")
        
        self.update_score(winner)

    def play_game(self):
        rounds = int(input("How many rounds would you like to play? "))
        for _ in range(rounds):
            self.play_round()
            print(f"\nScore: Player {self.score['player']} - Computer {self.score['computer']}\n")
        
        if self.score['player'] > self.score['computer']:
            print("You win the game!")
        elif self.score['player'] < self.score['computer']:
            print("Computer wins the game!")
        else:
            print("The game is a tie!")

game = RockPaperScissors()
game.play_game()
