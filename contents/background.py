import pygame
from .constants import BLACK, RED, ROWS, SQUARE_SIZE, COLS, WHITE, LENGTH, THICKNESS, WIDTH, HEIGHT,DIAMETER_H, CORRECTION_1, CORRECTION_2, GREEN, DIAMETER_T, HOLDING, WARNING, EXECUTION, RANDOM_INTERVAL, N_TRIALS  
import random

import numpy as np
import random


pygame.init()

class Target_random:
    def __init__(self):
        self.cont1 = 0
        self.cont2 =0
        self.cont3 = 0
        self.cont4 = 0
        self.response = []
        
    def target_control (self, n_trial):        
        for k in range(n_trial):   
            
            check = True
            while check:
                
                b = random.randint(1,  4)           
                if b == 1 and self.cont1 < n_trial//4:
                    self.response.append(1)
                    self.cont1 +=1
                    check = False
                if b == 2 and self.cont2 < n_trial//4:
                    self.response.append(2)
                    self.cont2 +=1
                    check = False
                if b == 3 and self.cont3 < n_trial//4:
                    self.response.append(3)
                    self.cont3 +=1
                    check = False
                if b == 4 and self.cont4 < n_trial//4:
                    self.response.append(4)
                    self.cont4 +=1
                    check = False
        return self.response
            

                
      
 
        
    

class Background:
    def __init__(self):
        self.clicked = False
        self.start = False
        self.current_time = []
        self.trial = 0
        self.pos_target_x = []
        self.pos_target_y = []
        self.cont = 0
        self.cont2 = False
        self.mouse_position = []
        self.check = False
        self.execution_time = []
        self.sequence = Target_random().target_control(N_TRIALS)   
        self.random = 0
                  
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                if row == 1 and col == 1 or row == 16 and col == 1 or row == 1 and col == 16 or row == 16 and col == 16:
                    pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, LENGTH, THICKNESS))
                    
                else: 
                    pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, LENGTH, THICKNESS))              
                    
    def draw_holding(self, win):
        win.fill(BLACK)
        pygame.draw.line(win, WHITE, [WIDTH//2,HEIGHT//2-THICKNESS*10], [HEIGHT//2,WIDTH//2+THICKNESS*10], THICKNESS)
        pygame.draw.line(win, WHITE, [WIDTH//2-THICKNESS*10,HEIGHT//2], [WIDTH//2+THICKNESS*10, HEIGHT//2], THICKNESS)
    
    def draw_black(self, win):
        win.fill(BLACK)
       
    
    def draw_circle(self, win, pos_x, pos_y, diameter, fill):
        pygame.draw.circle(win, WHITE, (pos_x, pos_y), diameter, fill)
    
    def draw_line(self, win, pos_col, pos_line):
        pygame.draw.line(win, WHITE, [(pos_col*SQUARE_SIZE)+CORRECTION_2,(pos_line*SQUARE_SIZE)-CORRECTION_1], [(pos_col*SQUARE_SIZE)-CORRECTION_2,(pos_line*SQUARE_SIZE)+CORRECTION_1], THICKNESS)
        pygame.draw.line(win, WHITE, [(pos_col*SQUARE_SIZE)+CORRECTION_2+CORRECTION_2*2,(pos_line*SQUARE_SIZE)-CORRECTION_1], [(pos_col*SQUARE_SIZE)-CORRECTION_2+CORRECTION_2*2,(pos_line*SQUARE_SIZE)+CORRECTION_1], THICKNESS)
        pygame.draw.line(win, WHITE, [(pos_col*SQUARE_SIZE)+CORRECTION_2+CORRECTION_2*4,(pos_line*SQUARE_SIZE)-CORRECTION_1], [(pos_col*SQUARE_SIZE)-CORRECTION_2+CORRECTION_2*4,(pos_line*SQUARE_SIZE)+CORRECTION_1], THICKNESS)
    
    def draw_mouse(self, win, mouse_position):
        mouse_position = mouse_position        
        for pos in mouse_position:                                  
            pygame.draw.circle(win, RED, (pos[0],pos[1]), DIAMETER_T//4, 0)
        
    def text_write (self, win, text, width, height):
        base_font = pygame.font.Font(None, 32)
        text_surface = base_font.render(text, True, (255,255,255))
        win.blit(text_surface, (width, height))     
        
    def draw_button (self, win):
        win.fill(BLACK)        
        pos = pygame.mouse.get_pos()       
        button_1 = pygame.Rect(WIDTH//2.5, HEIGHT//2, SQUARE_SIZE*2, SQUARE_SIZE)
        pygame.draw.rect(win, GREEN, button_1)
        if button_1.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                
                
        
        self.text_write(win,'Start', WIDTH//2.4, HEIGHT//1.95)
    
    def goback_home (self):
        pos = pygame.mouse.get_pos()
        point = (WIDTH//2, HEIGHT//2)             
        check = 'out'
        if pos[0] > (point[0]-DIAMETER_H//2) and pos[0] < (point[0] + DIAMETER_H//2):
               check = 'ok'
        return check
                     
          
      
        
    def draw(self, win):
        
        
        #Set random value      
        if self.cont2 == False:
            self.random = random.randint(RANDOM_INTERVAL[0],  RANDOM_INTERVAL[1])
        
        self.cont2  = True
        

        if self.clicked == True and self.trial < N_TRIALS:
            #Hide mouse 
            pygame.mouse.set_visible(False)
        
            #def cont timer
            self.current_time.append(pygame.time.get_ticks())            
            self.cont = self.current_time[-1] - self.current_time[0]
                       
            
            # Screen 1: Holding 
            if self.cont >= 0 and self.cont < HOLDING:
                self.draw_holding(win)                
               
            
            # Screen 2: Stimulus 
            if self.cont >= HOLDING and self.cont < WARNING:
                
                #print('Stimulus')                                 
                self.draw_squares(win)                
                #Circle of home position
                self.draw_circle(win, WIDTH//2, HEIGHT//2, DIAMETER_H, 0)
                
                #Circles of target
                self.draw_circle(win, 1*SQUARE_SIZE+DIAMETER_T//2, 1*SQUARE_SIZE,DIAMETER_T, 1)#left top
                self.draw_circle(win, 16*SQUARE_SIZE+DIAMETER_T//2, 1*SQUARE_SIZE,DIAMETER_T, 1)#right top
                self.draw_circle(win, 1*SQUARE_SIZE+DIAMETER_T//2, 16*SQUARE_SIZE,DIAMETER_T, 1)#left bottom
                self.draw_circle(win, 16*SQUARE_SIZE+DIAMETER_T//2, 16*SQUARE_SIZE,DIAMETER_T, 1)#right bottom
                
                
                # lines inside circle
                if self.sequence[self.trial] == 1:
                    self.draw_line(win, 1,1) #left top
                    self.pos_target_x = 1*SQUARE_SIZE+DIAMETER_T//2
                    self.pos_target_y = 1*SQUARE_SIZE
                
                if self.sequence[self.trial] == 2:
                    self.draw_line(win, 16,1) #right top
                    self.pos_target_x = 16*SQUARE_SIZE+DIAMETER_T//2
                    self.pos_target_y = 1*SQUARE_SIZE
                
                if self.sequence[self.trial] == 3:
                    self.draw_line(win, 1,16) #left bottom
                    self.pos_target_x = 1*SQUARE_SIZE+DIAMETER_T//2
                    self.pos_target_y = 16*SQUARE_SIZE
                
                if self.sequence[self.trial] == 4:
                    self.draw_line(win, 16,16) #right bottom
                    self.pos_target_x = 16*SQUARE_SIZE+DIAMETER_T//2
                    self.pos_target_y = 16*SQUARE_SIZE
                
                
                
                #Get mouse position and draw
                #self.mouse_position.append(pygame.mouse.get_pos())
                #self.draw_mouse(win, self.mouse_position)
            
            #Screen 3: Empty         
            if self.cont >= WARNING and self.cont < WARNING+self.random:
                #print('Empty')
                self.draw_black(win)
                self.start = True
                self.mouse_position = [] #Set mouse position
                pygame.mouse.set_pos([WIDTH//2, HEIGHT//2]) #Set to center
                
                
            #Screen 4: Start 
            if  self.cont >= WARNING+self.random and self.cont < WARNING+EXECUTION+self.random and self.start == True :
                #print('Start')
                self.draw_squares(win)
                
                #Circle of home position
                self.draw_circle(win, WIDTH//2, HEIGHT//2, DIAMETER_H, 0)
                
                #Circles of target
                self.draw_circle(win, 1*SQUARE_SIZE+DIAMETER_T//2, 1*SQUARE_SIZE,DIAMETER_T, 1)#left top
                self.draw_circle(win, 16*SQUARE_SIZE+DIAMETER_T//2, 1*SQUARE_SIZE,DIAMETER_T, 1)#right top
                self.draw_circle(win, 1*SQUARE_SIZE+DIAMETER_T//2, 16*SQUARE_SIZE,DIAMETER_T, 1)#left bottom
                self.draw_circle(win, 16*SQUARE_SIZE+DIAMETER_T//2, 16*SQUARE_SIZE,DIAMETER_T, 1)#right bottom
                
                #Get time of response 
                self.execution_time.append(pygame.time.get_ticks())  
                
                
                #Get mouse position and draw                
                self.mouse_position.append(pygame.mouse.get_pos())
                self.draw_mouse(win, self.mouse_position)
            
            
                             
             
                
                
            # Set all ans Save
            if self.cont > WARNING+EXECUTION+self.random:
                print('Set all')
                self.trial +=1
                
                #Save data
                target_x = []
                target_y = []
                names = ['Time', 'Mouse_x', 'Mouse_y', 'Target_x', 'Target_y']
                
                for i in range (len(self.execution_time)):
                    target_x.append(self.pos_target_x)
                    target_y.append(self.pos_target_y)
                np.savetxt('trials/trial_'+ str(self.trial)+'.csv', np.column_stack([self.execution_time,self.mouse_position,target_x, target_y] ), header = ','.join(names), delimiter=',')
                
                #Set data
                self.current_time = []
                self.mouse_position = []
                self.execution_time = []                
                print(self.trial) 
                self.cont2 = False 
                
               
                
                             
        
        else:
            
            pygame.mouse.set_visible(True)
            
            self.draw_button(win)
            
            
            
                
              
        
 