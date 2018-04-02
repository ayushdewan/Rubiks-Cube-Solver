# Rubiks-Cube-Solver
Solves Rubiks cubes using OpenCV

# Instructions For Use
Run main.py and a window will pop up labeled "F Face". Line up the centers of each square with the 9 dots of any face and press H once the colors of the dots match the color of the squares. A new window will pop labeled "U Face" where you will need to scan the up face with respect to the front face scanned previously. Continue until all faces are scanned and the output will be shown in the console.

# Color Identification
I used OpenCV to convert the captured frames from my computer to the HSV color scheme and identified color based on the hue. I then found the color density in each square of the rubiks cube to identify the squares overall color and used the kociemba python module (https://github.com/muodov/kociemba) to solve the cube given its color scheme.

![alt text](https://github.com/ayushdewan/Rubiks-Cube-Solver/blob/master/image.png?raw=true)
