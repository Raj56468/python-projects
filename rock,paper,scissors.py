import random 

def play_round(player_choice, computer_choice):
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('rock', 'paper'): 'lose',
        ('rock', 'rock'): 'draw',
        ('paper', 'rock'): 'win',
        ('paper', 'scissors'): 'lose',
        ('paper', 'paper'): 'draw',
        ('scissors', 'paper'): 'win',
        ('scissors', 'rock'): 'lose',
        ('scissors', 'scissors'): 'draw',
    }
    return outcomes[(player_choice, computer_choice)]

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
    else:
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = play_round(player_choice, computer_choice)
        if result == 'win':
            print("You win!")
        elif result == 'lose':
            print("You lose!")
        else:
            print("It's a draw!")

