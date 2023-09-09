#import pygame and initialize the pygame engine.
import pygame
import os
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((640,480))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
#Colors for the shapes
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
#Show text function
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont('freesans',30)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
#Button coordinate variables
x = 220
y = 200
#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if x <= x1 <= x+180 and y <= y1 <= y+40:
                os.system("python Snake.py")
                pygame.quit()
                exit()

    pygame.draw.rect(screen, pure_blue, (x,y,180,40), 1)
    show_text("Play", 280, 200, pure_blue)
    #Continuously update the screen
    pygame.display.update()