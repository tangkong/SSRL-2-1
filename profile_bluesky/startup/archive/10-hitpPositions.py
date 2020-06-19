import numpy as np

y = [9.0, 4.5, 0.0, -4.5, -9.0, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, 
    -18.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, 
    27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, 
    -27.0, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, 
    -22.5, -27.0, 31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, 
    -13.5, -18.0, -22.5, -27.0, -31.5, 31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 
    4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, -31.5, 31.5, 27.0, 22.5, 
    18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, -31.5, 
    31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, -9.0, -13.5, -18.0, 
    -22.5, -27.0, -31.5, 31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 0.0, -4.5, 
    -9.0, -13.5, -18.0, -22.5, -27.0, -31.5, 27.0, 22.5, 18.0, 13.5, 9.0, 4.5, 
    0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, 27.0, 22.5, 18.0, 13.5, 9.0,
    4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, -27.0, 22.5, 18.0, 13.5, 9.0, 
    4.5, 0.0, -4.5, -9.0, -13.5, -18.0, -22.5, 18.0, 13.5, 9.0, 4.5, 0.0, 
    -4.5, -9.0, -13.5, -18.0, 9.0, 4.5, 0.0, -4.5, -9.0]

x = [-31.5, -31.5, -31.5, -31.5, -31.5, -27.0, -27.0, -27.0, -27.0, -27.0,
     -27.0, -27.0, -27.0, -27.0, -22.5, -22.5, -22.5, -22.5, -22.5, -22.5, 
     -22.5, -22.5, -22.5, -22.5, -22.5, -18.0, -18.0, -18.0, -18.0, -18.0,
    -18.0, -18.0, -18.0, -18.0, -18.0, -18.0, -18.0, -18.0, -13.5, -13.5,
    -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5, -13.5,
    -13.5, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0, -9.0,
    -9.0, -9.0, -9.0, -9.0, -9.0, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5,
    -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, -4.5, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5,
    4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 
    9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 
    9.0, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 13.5, 
    13.5, 13.5, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 
    18.0, 18.0, 18.0, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 22.5, 
    22.5, 22.5, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 27.0, 31.5, 
    31.5, 31.5, 31.5, 31.5]

loc177 = np.array([x,y])