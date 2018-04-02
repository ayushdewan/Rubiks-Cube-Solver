import numpy as np
from PIL import ImageGrab
import cv2
import time

def screen_record():
    last_time = time.time()
    cv2.startWindowThread()
    # cv2.namedWindow("preview")
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,30,715,560)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        img = cv2.flip(cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB), 1)
        img_hsv = cv2.cvtColor(printscreen, cv2.COLOR_BGR2HSV)

        offset = 75
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                cv2.circle(img,(358 + i * offset, 280 + j * offset), 5, (0,255,0), -1)
        """
        red = [110, 50, 50], [130, 255, 255] BGR
        blue = [0, 50, 50], [10, 255, 255] BGR
        green = [45, 50, 50], [75, 255, 255] BGR
        yellow = [20, 100, 100], [30, 255, 255] RGB
        orange = [5, 100, 100], [15, 255, 255] RGB
        white = [0, 0, 0], [180, 30, 255] RGB
        """
        lower = np.array([0, 50, 50], dtype = "uint8")
        upper = np.array([10, 255, 255], dtype = "uint8")

        mask = cv2.inRange(img_hsv, lower, upper)
        output = cv2.bitwise_and(img_hsv, img_hsv, mask = mask)

        detector = cv2.SimpleBlobDetector_create()
        keypoints = detector.detect(img)
        im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


        cv2.imshow('window', im_with_keypoints)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
