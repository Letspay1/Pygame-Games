#import pygame and initialize the pygame engine.
import pygame
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((640,480))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
# Colors
yellow = (235,225,0) 
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
# Define the text function
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont('freesans',128)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            show_text("X",x,y,pure_red)

    #Continuously update the screen
    pygame.display.update()