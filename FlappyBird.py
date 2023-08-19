#import pygame and initialize the pygame engine.
import pygame
import random
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
x = 320
height = 25
# Y Coordinate for Rectangles
x1 = 620
y1 = 0
height1 = 300
width1 = 50
# Pygame Clock
clock = pygame.time.Clock()
# The game score
score = 0
# Image paths
flappy_path="FlappyBird.png"
flappybird=pygame.image.load(flappy_path)
flappybird=pygame.transform.scale(flappybird,(60,50))
pipe_path="Pipe.png"
pipe=pygame.image.load(pipe_path)
pipe=pygame.transform.scale(pipe,(width1+15,height1+100))
pipe_inverted = pygame.transform.flip(pipe,False,True)
background_path = "Background.png"
background = pygame.image.load(background_path)
background = pygame.transform.scale(background, (640,480))
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
    x1-=2
    clock.tick(60)
    
    # Reset x when rectangles go out of bounds
    if x1 < 0:
        score+=1
        x1 = 640
        y1 = random.randint(-300,0)
    # Quit when the player goes out of bounds
    if y < 0 or y > 480:
        pygame.quit()
        exit()
    # Detect any collision between the rectangles and the player
    if  x1<x+15<x1+width1:
        # print("boundry")
        if height1+y1 < y < 100+height1+y1:
            pass
        else:
            print("Game Over. Your score was", score)
            pygame.quit()
            exit()




    screen.blit(background,(0,0))
    pygame.draw.circle(screen, yellow,(x,y),15,0)
    screen.blit(flappybird,(x-30,y-30))
    pygame.draw.rect(screen,pure_green,(x1,y1,width1,height1),0)
    screen.blit(pipe_inverted,(x1-5,y1-80))
    pygame.draw.rect(screen,pure_green,(x1,y1+height1+100,width1,height1+100),0)
    screen.blit(pipe,(x1-5,y1+height1+70))
    #Continuously update the screen
    pygame.display.update()