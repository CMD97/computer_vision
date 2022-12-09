# Computer Vision

## Milestone 1
Milestone 1 had the task of creating a model on Teachable Machine to be able to recognise the difference between 4 classes: rock, paper, scissors & nothing.

Within the creation of this model, approximately 800 images was taken of my hand representing the 3 classes of rock, paper & scissors, with the last class consistenting of 800 images of 'nothing' present.
This will allow the model to correctly determine if the user of the program will be showing each of the four classes.

## Milestone 2 - Setting up the environment
The model needed to be under certain environment criteria to be ran, therefore a new environment needed to be created using conda called 'cvrps', within this pip was installed to allow several python packages, the packages included are: opencv-python, tensorflow& ipykernel.

## MIlestone 3 - Creating the manual Rock-Paper-Scissors game
To be able to put it altogether with the model, a manual version of rock paper scissors was created within VSCode. This manual version included 3 key functions with a final added to put it altogether under a 'play' function.
The first function created was 'get_user_choice', this has an input section for the user to choose rock paper and scissors, with validation of the users answer, e.g. if they typed something other than 'rock' 'paper' or 'scissors' it would ask them to choose again:

    if user_choice != 'Rock' and user_choice != 'Paper' and user_choice != 'Scissors':
            print(f'{user_choice} is not a valid option. Please make sure to type {options[0]}, {options[1]} or {options[2]}.')
        else:
            print(f'You chose: {user_choice}')
            return user_choice

The user's choice would then be returned into the get_winner function to be compared with the computers choice.

The second function created was 'get_computer_choice' for this choice the code `import random` was utilised as well as a list of each option `options = ['Rock', 'Paper', 'Scissors']`. The computers choice was chosen as followed:
     computer_choice = random.choice(options)
    print(f'Computer chose:', computer_choice)
    return computer_choice

As the user's choice was returned into the get_winner function, so was the computers allowing the comparison to begin.

The final key function is 'get_winner' this function consisted mainly of a if/elif/else statement:

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
    print(f''' wins:   {wins}   losses: {losses}    ties:   {ties}''')

If the user tied with the computer it would add +1 to the tie counter, and print out a statement regarding the tie. 
Under the `elif` statement, it shows which booleans are used to determine if the user beat the computer and add +1 to the wins, as well as adding +1 to games_played.
Finally the `else` statement used would catch any occurrences if the computer beat the user and add +1 to the losses, as well as adding +1 to the games_played.

To wrap the code together, the game was then played under the function 'play'. Allowing the entire code to run through in a while loop from there:

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

As stated above, the game was a best of 3, so the while statement will play through until 3 games are played which consistent of wins and losses, or 2 wins or 2 losses occur.

### Added extras
2 other functions were utilised to make the experience user friendly which are encapsulated within the `play()` function also. These are: 'welcome' and 'play_again'.
At the beginning of the game when launching from the command line, the program will print a line telling you what the game is:

    print('Welcome to Rock, Paper, Scissors! This game is a best of 3.\n')

At the end of the game, when the `play()` while loop is broken, the user will be asked to play again, under the function `play_again()`:

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

# Milestone 4
