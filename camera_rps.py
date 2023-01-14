import cv2
import time
time_start = time.time()
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
    if time.time() - time_start > 5:
        print("you chose rock")
        def get_prediction():
            return(model.predict(data))
        break

