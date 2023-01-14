# Computer Vision Rock Paper Scissors

This project is designed to play a game of rock paper and scissors.

## Model

The model was built and trained on the following website (https://teachablemachine.withgoogle.com/train/image). Using a webcam, the model was trained for four class types: Rock, Paper, Scissors and none. For each class, 100 images were captured. The set of images below shows an example from each class

### Rock - Fully closed fist
<p align="center">
    <img src = '/images/rock.png'>
</p>

### Paper - Flat outstretched hand with fingers together

<p align="center">
    <img src = '/images/paper.png'>
</p>

### Scissors - Index and middle finger out with a gap between

<p align="center">
    <img src = '/images/scissors.png'>
</p>

### Nothing - none of the gestures above

<p align="center">
    <img src = '/images/nothing.png'>
</p>

These images were then fed in to the model training algorithim, with the following settings:

- Epochs 50
- Batch Size 16
- Learning Rate 0.001

 Some limitations of the model are that only 1 subject was used for the image capture, and only one location.


### Enviroment Setup

A new environment was set up within conda, called tensorflow-env. As I'm running an M2 mac, python 3.9 was used for the environment. The steps found on this page (https://developer.apple.com/metal/tensorflow-plugin/) were then followed to setup Tensorflow-Metal. , which enables the acceleration of machine learning models with Metal on Mac. Initially when verifying the install had run ok,it failed. This was due to the versions of tensorflow-metal, which worked when stepped back to 0.5.0. Similarly tesnorflow-macos had to be stepped back to 2.9.0. A full list of installed packages may be found in the requirements.txt file contained within the repository root directory.

## Manual rock paper scissors game code

A python script (manual_rps.py) was set up to play a non-webcame game of Rock, Paper, Scissors. The following functions were defined to achieve this:

- get_computer_choice(): This picks one of "Rock", "Paper" or "Scissors" at random, with the choice returned.

- get_user_choice(): This ask the use to pick one of "Rock", "Paper" or "Scissors".

- get_winner(computer_choice, user_choice): This function prints the result of Rock, Paper, Scissors. The result can either be computer wins, user wins, or a tie. The result is calculated through a series of if/elif/else statements are used to compare the computer's choice vs the user's choice

- play(): This calls the above 3 functions, so as to play RPS.