import numpy as np
from PIL import ImageGrab
import cv2
import time
from colorlabeler import density

def screen_record():
    last_time = time.time()
    cv2.startWindowThread()
    # cv2.namedWindow("preview")

    cap = cv2.VideoCapture(0)

    while(True):
        _, img = cap.read()
        last_time = time.time()
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        offset = 75
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cv2.circle(img,(358 + i * offset, 280 + j * offset), 5, (0,255,0), -1)
        """
        red = [160, 75, 75], [180, 255, 255]
        blue = [110, 75, 75], [130, 255, 255]
        green = [40, 0, 0], [80, 255, 255]
        yellow = [20, 75, 75], [40, 255, 255]
        orange = [10, 100, 100], [20, 255, 255]
        white = [0, 0, 50], [180, 20, 255]
        """
        lower = np.array([35, 0, 0])
        upper = np.array([80, 255, 255])

        mask = cv2.inRange(img_hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask = mask)

        cv2.imshow('window', img)
        print(density(img_hsv[403:463, 250:310], "yellow"))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.imwrite("yert.jpg", img[478:538, 250:310])
            cv2.destroyAllWindows()
            cap.release()
            break

screen_record()
