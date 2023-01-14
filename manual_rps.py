import random 

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def get_user_choice():
    user_choice = input("Enter one of Rock/Paper/Scissors: ")
    return user_choice

def get_winner(computer_choice, user_choice):
    if get_computer_choice() == 'Rock' and get_user_choice() == 'Rock':
        print("It is a tie!")
    elif get_computer_choice() == 'Rock' and get_user_choice() == 'Scissors':
        print("You lost")
    elif get_computer_choice() == 'Rock' and get_user_choice() == 'Paper':
        print("You won!")
    elif get_computer_choice() == 'Paper' and get_user_choice() == 'Rock':
        print("You lost")
    elif get_computer_choice() == 'Paper' and get_user_choice() == 'Scissors':
        print("You won!")
    elif get_computer_choice() == 'Paper' and get_user_choice() == 'Paper':
        print("It is a tie!")
    elif get_computer_choice() == 'Scissors' and get_user_choice() == 'Paper':
        print("You lost")
    elif get_computer_choice() == 'Scissors' and get_user_choice() == 'Rock':
        print("You won!")
    else:
        print("It is a tie")

