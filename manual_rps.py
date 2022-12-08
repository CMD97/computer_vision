import random


options = ['Rock', 'Paper', 'Scissors']
wins = 0
losses = 0
ties = 0
games_played = 0

def welcome():
    print('Welcome to best of 3, Rock, Paper, Scissors! \n')

def get_user_choice():
    while True:
        user_choice = input(f'Choose either {options[0]}, {options[1]} or {options[2]}: ').title()
        if user_choice != 'Rock' and user_choice != 'Paper' and user_choice != 'Scissors':
            print(f'{user_choice} is not a valid option. Please make sure to type {options[0]}, {options[1]} or {options[2]}.')
        else:
            print(f'You chose: {user_choice}')
            return user_choice
            
def get_computer_choice():
    computer_choice = random.choice(options)
    print(f'Computer chose:', computer_choice)
    return computer_choice

def get_winner():
    global wins, losses, ties, games_played
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    if user_choice == computer_choice:
        print('You both chose the same, it\'s a tie!')
        ties += 1
    elif user_choice == 'Rock' and computer_choice == 'Scissors' or user_choice == 'Scissors' and computer_choice == 'Paper' or user_choice == 'Paper' and computer_choice == 'Rock':
        print(f'{user_choice} beats {computer_choice}, you win!')
        wins += 1
        games_played += 1
    else:
        print(f'{user_choice} gets beat by {computer_choice}, you lose!')
        losses += 1
        games_played += 1
    print(f'''
wins:   {wins}
losses: {losses}
ties:   {ties}
''')

def play():
    welcome()
    while True:
        if games_played != 3 and wins != 2 and losses != 2:
            get_winner()
        elif wins == 2:
            print(f'You won! {wins} wins over the computers {losses} win. \n')
            play_again()
            break
        else:
            print(f'You lost! Only {wins} win over the computers {losses} wins.\n')
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
                play()
                break
            elif ask_user_to_play_again == 'N':
                print('\n')
                print('Thanks for playing.')
                print('\n')
                break
            else: 
                print('Invalid selection, please choose either Y or N')

play()