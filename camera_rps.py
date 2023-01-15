import cv2
import time
from keras.models import load_model
import numpy as np
import random

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def get_prediction():
    return(model.predict(data))

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def get_user_choice():
    user_choice_prediction = np.argmax(get_prediction())
    user_choice_options = ["Rock","Paper","Scissors"]
    print(user_choice_options[user_choice_prediction])
    return user_choice_options[user_choice_prediction]

def get_winner(computer_choice, user_choice):
    if computer_choice == 'Rock' and user_choice == 'Rock':
        print("It is a tie!")
        return "Tie" 
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        print("You lost")
        return "Computer"
    elif computer_choice == 'Rock' and user_choice == 'Paper':
        print("You won!")
        return "User"
    elif computer_choice == 'Paper' and user_choice == 'Rock':
        print("You lost")
        return "Computer"
    elif computer_choice == 'Paper' and user_choice == 'Scissors':
        print("You won!")
        return "User"
    elif computer_choice == 'Paper' and user_choice == 'Paper':
        print("It is a tie!")
        return "Tie"
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        print("You lost")
        return "Computer"
    elif computer_choice == 'Scissors' and user_choice == 'Rock':
        print("You won!")
        return "User"
    else:
        print("It is a tie")
        return "Tie"

def play():
    return get_winner(get_computer_choice(),  get_user_choice())

time_start = time.time()
round_count = 0
computer_wins = 0
user_wins = 0
while True:
    if round_count > 5 or computer_wins == 3 or user_wins == 3:
        break
    if time.time() - time_start > 5:
        round_count += 1
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(model.predict(data))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        result=play()
        if result == "User":
            user_wins += 1
        if result == "Computer":
            computer_wins += 1

        print(f"Computer wins: {computer_wins}, User wins: {user_wins}, Round: {round_count}")
        time_start = time.time()
        