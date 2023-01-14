import random 

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    return random.choice(options)

def get_user_choice():
    user_choice = input("Enter one of Rock/Paper/Scissors: ")
    return user_choice



