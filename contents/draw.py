import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from contents.background import Background


class Draw:
    def __init__(self, win):
        self.background = Background()       
        self.win = win
        
        
    
    def update(self):   
                       
        self.background.draw(self.win)        
        pygame.display.update()

  

   