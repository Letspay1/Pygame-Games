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
yellow = (255,225,0) 
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
black = (0,0,0)
# Y coordinate for flappy bird
y = 240
height = 25
# Pygame Clock
clock = pygame.time.Clock()
#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y-=height
    y+=1
    clock.tick(30)

    screen.fill(black)
    pygame.draw.circle(screen, yellow,(320,y),15,0)
    #Continuously update the screen
    pygame.display.update()