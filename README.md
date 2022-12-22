# Computer Vision

## Milestone 1
Milestone 1 had the task of creating a model on Teachable Machine to be able to recognise the difference between 4 classes: rock, paper, scissors & nothing.

Within the creation of this model, approximately 800 images was taken of my hand representing the 3 classes of rock, paper & scissors, with the last class consistenting of 800 images of 'nothing' present.
This will allow the model to correctly determine if the user of the program will be showing each of the four classes.

## Milestone 2 - Setting up the environment
The model needed to be under certain environment criteria to be ran, therefore a new environment needed to be created using conda called 'cvrps', within this pip was installed to allow several python packages, the packages included are: opencv-python, tensorflow & ipykernel.

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

## Milestone 4 - Combining the manual version into the camera version
Once the manual version was complete, the function `get_user_choice` was replaced by the code from Teachable Machine that allowed it to run within opencv-python. The next part was ensuring that the probabilities of each class showed correctly within a numpy array; the highest probability needed to be chosen so that the user would have an output to the program and the user would have a choice of 'Rock', 'Paper', 'Scissors' or 'Nothing' which will compete with the computers choice from the manual version. 

To ensure the highest probability was selected from the list:

    user_index = np.argmax(prediction[0])
    user_choice = user_options[user_index]

This was then returned to the function of `get_winner()` to be compared with the computers choice.

After this, a countdown was required to make sure the code doesn't take each frame as a new rock, paper or scissors from the user. To make sure the user had full control over when they wanted to begin the next round in the best of 5, the 'S' key was assigned to begin the countdown and is printed upon initialising the game to tell the user what key they need to press to start the countdown.

Once the 'S' key was pressed it initiated flags to begin the countdown which was referenced with the `time.time()` function as shown below:

    countdown = False
    countdown_first = False
    sec_3 = False
    sec_2 = False
    sec_1 = False

        k = cv2.waitKey(1)
        if k == ord('s'):
            countdown = True
            countdown_first = True
            start_time = time.time()
        if countdown is True and countdown_first is True:
            print('Get your answer ready!')
            countdown_first = False
            sec_3 = True
        elif sec_3 is True and (1.9 >= (time.time() - start_time) >= 1):
            print('3')
            sec_3 = False
            sec_2 = True
        elif sec_2 is True and (2.9 >= (time.time() - start_time) >= 2):
            print('2')
            sec_2 = False
            sec_1 = True
        elif sec_1 is True and (3.9 >= (time.time() - start_time) >= 3):
            print('1')
            sec_1 = False

As shown, when the 'S' key is pressed, the countdown & countdown_first booleans were changed from `False` to `True`. As well as a snapshot of the time being taken and stored into the variable `start_time`. 

THe first part of the if statement prints `Get your answer ready!` showing the user they need to begin to select one of the options required to play rock, paper, scissors. After this, the '3, 2, 1' was initiated, each part required a separate flag to become `True` in the previous statement, whilst within the statement itself, it turned the flag that was needed to `False` this meant that even if `time.time() - start_time` was in between the inequalities surrounding it twice, it would only print the number for the countdown once.

Once the timer hit 1, the snapshot of the frame is taken and the output of rock, paper or scissors was used within `get_winner()`. 

### Tying up the loose end
If the user chose `Nothing` there was an if statement within `play(options)` that made sure it would not pick a computer choice if the user did not pick one of the verified rock, paper, scissors options:

    user_choice = game.get_user_choice()
    if user_choice == 'Nothing':
        print('\nMake sure you pick an option!\n')
    else:
        computer_choice = game.get_computer_choice(options)
        game.get_winner(user_choice, computer_choice)

## Conclusion

Throughout this project, I have refined my skills in Python, being able to successfully create a computer vision project from scratch independently through the `manual_rps.py` file as well as a minimum amount of help within the `cv_rps.py` file. I have got the understanding of how to input classes into Python as well as understanding the parameters and arguments within each function to ensure a seemless experience for anyone reading through to review the code, as well as feeling confident with my skills to learn new parts of code with ease such as the `time.time()` function.

One thing I'd focus on to improve the code is to have more understanding around the cv2.putText to be able to display the countdown on the frame so the user can launch the project from the command line and not need to worry, as well as create an intuitive GUI so that the score & computers answer can be featured alongside the frame. Overall, I'm pleased with what I've created so far and will continue to try and understand the operations cv2 has for later use.
