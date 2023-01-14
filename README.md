# Computer Vision Rock Paper Scissors

This project is designed to play a game of rock paper and scissors.

## Model

The model was built and trained on the following website (https://teachablemachine.withgoogle.com/train/image). Using a webcam, the model was trained for four class types: Rock, Paper, Scissors and none. For each class, 100 images were captured. The set of images below shows an example from each class

##Rock - Fully closed fist
<p align="center">
    <img src = '/images/rock.png'>
</p>

##Paper - Flat outstretched hand with fingers together

<p align="center">
    <img src = '/images/paper.png'>
</p>

##Scissors - Index and middle finger out with a gap between

<p align="center">
    <img src = '/images/scissors.png'>
</p>

##Nothing - none of the gestures above

<p align="center">
    <img src = '/images/nothing.png'>
</p>

These images were then fed in to the model training algorithim, with the following settings:

- Epochs 50
- Batch Size 16
- Learning Rate 0.001

 Some limitations of the model are that only 1 subject was used for the image capture, and only one location.
