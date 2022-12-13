import random

class RPS:
    def __init__(self, options, games_played=0, wins=0, losses=0, ties=0):

        self.computer_choice = random.choice(options)
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.games_played = games_played

        print('Welcome to Rock, Paper, Scissors! This game is a best of 5.\n')

    def get_user_choice(self):
        while True:
            user_choice = input(f'Choose either {options[0]}, {options[1]} or {options[2]}: ').title()
            if user_choice != 'Rock' and user_choice != 'Paper' and user_choice != 'Scissors':
                print(f'{user_choice} is not a valid option. Please make sure to type {options[0]}, {options[1]} or {options[2]}. \n')
            else:
                print(f'You chose: {user_choice}')
                return user_choice
                
    def get_computer_choice(computer_choice, options):
        computer_choice = random.choice(options)
        print(f'Computer chose:', computer_choice)
        return computer_choice

    def get_winner(self, user_choice, computer_choice):
        global wins, losses, ties, games_played
        if user_choice == computer_choice:
            print('You both chose the same, it\'s a tie!')
            self.ties += 1
        elif user_choice == 'Rock' and computer_choice == 'Scissors' or user_choice == 'Scissors' and computer_choice == 'Paper' or user_choice == 'Paper' and computer_choice == 'Rock':
            print(f'{user_choice} beats {computer_choice}, you win!')
            self.wins += 1
            self.games_played += 1
        else:
            print(f'{user_choice} gets beat by {computer_choice}, you lose!')
            self.losses += 1
            self.games_played += 1
        print(f'''
    wins:   {self.wins}
    losses: {self.losses}
    ties:   {self.ties}
    ''')

def play(options):
    game = RPS(options, games_played=0)
    while True:
        if game.games_played != 5 and game.wins != 3 and game.losses != 3:
            user_choice = game.get_user_choice()
            computer_choice = game.get_computer_choice(options)
            game.get_winner(user_choice, computer_choice)
        elif game.wins == 3 and game.losses == 1:
            print(f'You won! {game.wins} wins over the computers {game.losses} win. \n')
            break
        elif game.wins == 3 and (game.losses == 2 or game.losses == 0):
            print(f'You won! {game.wins} wins over the computers {game.losses} wins. \n')
            play_again()
            break
        elif (game.wins == 2 or game.wins == 0) and game.losses == 3:
            print(f'You lost! {game.wins} wins over the computers {game.losses} wins. \n')
            play_again()
            break
        else:
            print(f'You lost! Only {game.wins} win over the computers {game.losses} wins.\n')
            play_again()
            break

def play_again():
        while True:
            ask_user_to_play_again = input('Play again? Input Y or N: ').upper()
            if ask_user_to_play_again == 'Y':
                global wins, losses, ties, games_played
                losses = 0
                wins = 0
                ties = 0
                games_played = 0
                print('\n')
                print('Let\'s jump back in!')
                print('_______________________________________________________')
                print('\n')
                play(options)
                break
            elif ask_user_to_play_again == 'N':
                print('\n')
                print('Thanks for playing.')
                print('\n')
                break
            else: 
                print('Invalid selection, please choose either Y or N')

if __name__ == '__main__':
    options = ['Rock', 'Paper', 'Scissors']
    play(options)