import numpy as np
import cv2

bounds = {
	"red" : (np.array([160, 75, 75]), np.array([180, 255, 255])),
	"blue" : (np.array([110, 75, 75]), np.array([130, 255, 255])),
	"green" : (np.array([35, 0, 0]), np.array([85, 255, 255])),
	"yellow" : (np.array([20, 75, 75]), np.array([40, 255, 255])),
	"white" : (np.array([0, 0, 20]), np.array([180, 30, 255])),
	"orange" : (np.array([10, 100, 100]), np.array([20, 255, 255]))
}

def density(img, color):
	lower = bounds[color][0]
	upper = bounds[color][1]
	mask = cv2.inRange(img, lower, upper)
	return np.sum(mask)/255
