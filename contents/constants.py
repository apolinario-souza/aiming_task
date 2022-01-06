import pygame

#Configuration trials
N_TRIALS = 12

#Configuration screen
WIDTH, HEIGHT = 700, 700


#Configuration Lines
ROWS, COLS = 18, 18
LENGTH = 25
SQUARE_SIZE = WIDTH//COLS
THICKNESS = 1
CORRECTION_1 = (22.5*SQUARE_SIZE)//100  #diagonal lines
CORRECTION_2 = (11.25*SQUARE_SIZE)//100 #diagonal lines 


#Configuration Home and Targets 
DIAMETER_H = 20
DIAMETER_T = 20

### Times
HOLDING = 1000
WARNING = 2000
EXECUTION = 1500
RANDOM_INTERVAL = (2000, 3000) 



# Color rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
GREEN = (105, 250, 0)

