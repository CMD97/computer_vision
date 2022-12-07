import random


options = ['Rock', 'Paper', 'Scissors']

def get_user_choice():
    while True:
        user_choice = input(f'Choose either {options[0]}, {options[1]} or {options[2]}: ').title()
        if user_choice != 'Rock' and user_choice != 'Paper' and user_choice != 'Scissors':
            print(f'{user_choice} is not a valid option. Please make sure to type {options[0]}, {options[1]} or {options[2]}.')
        else:
            print('\n')
            print(f'You chose: {user_choice}')
            return user_choice
            
def get_computer_choice():
    computer_choice = random.choice(options)
    return computer_choice

def get_winner():
    computers_choice = get_computer_choice()
    users_choice = get_user_choice()
    print('Computer chose:', computers_choice)
    if users_choice == computers_choice:
        print('You both chose the same, choose again!')
        get_winner()
    elif users_choice == 'Rock' and computers_choice == 'Scissors' or users_choice == 'Scissors' and computers_choice == 'Paper' or users_choice == 'Paper' and computers_choice == 'Rock':
        print(f'{users_choice} beats {computers_choice}, you win!')
    else:
        print(f'{users_choice} gets beat by {computers_choice}, you lose!')

get_winner()