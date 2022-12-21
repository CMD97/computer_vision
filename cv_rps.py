import random
import cv2
from keras.models import load_model
import numpy as np
import time
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

class RPS:
    def __init__(self, options, games_played=0, wins=0, losses=0, ties=0):

        self.computer_choice = random.choice(options)
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.games_played = games_played

        print('\nWelcome to Rock, Paper, Scissors! This game is a best of 5.\n')
        print('Press the S key to start the countdown. \n')

    def get_user_choice(self):
        user_choice = ''
        countdown = False
        countdown_first = False
        while True:
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data, verbose=0)
            cv2.imshow('frame', frame)
            k = cv2.waitKey(1)
            if k == ord('s'):
                countdown = True
                countdown_first = True
                start_time = time.time()
            if countdown is True and countdown_first is True:
                print('Get your answer ready!')
            if (time.time() - start_time) == 1:
                print((time.time() - start_time))
                countdown_first = False
            if countdown is True and (time.time() - start_time >= 3):
                user_index = np.argmax(prediction[0])
                user_choice = user_options[user_index]
                print('You chose:', user_choice)
                return user_choice
                
    def get_computer_choice(computer_choice, options):
        computer_choice = random.choice(options)
        print(f'Computer chose:', computer_choice)
        return computer_choice

    def get_winner(self, user_choice, computer_choice):
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
            if user_choice == 'Nothing':
                print('\nMake sure you pick an option!\n')
            else:
                computer_choice = game.get_computer_choice(options)
                game.get_winner(user_choice, computer_choice)
        elif game.wins == 3 and game.losses == 1:
            print(f'You won! {game.wins} wins over the computers {game.losses} win. \n')
            play_again()
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
                cap.release()               # After the loop release the cap object
                cv2.destroyAllWindows()     # Destroy all the windows
                break
            else: 
                print('Invalid selection, please choose either Y or N')

def countdown():
    print('Get your answer ready!')
    prev = time.time() + 1
    TIMER = int(4)
    while TIMER >= 1:
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER -1
            print(TIMER)

if __name__ == '__main__':
    options = ['Rock', 'Paper', 'Scissors']
    user_options = ['Rock', 'Paper', 'Scissors', 'Nothing']
    play(options)