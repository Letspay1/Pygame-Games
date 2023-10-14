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
#Colors for our shapes
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
black = (0,0,0)
# Coordinates
x = 0
y = 0
foodx = (random.randint(0,640) // 10 ) * 10
foody = (random.randint(0,480) // 10 ) * 10
snakex = (random.randint(0,640) // 10) * 10
snakey = (random.randint(0,480) // 10) * 10
# Flag Variables
up = 0
down = 0
left = 0
right = 0
# Clock Variable
clock = pygame.time.Clock()
# Recording Snake movement
snake_list = [[snakex,snakey]]
# Score Variable
score = 0
#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up = 1
                down = 0
                left = 0
                right = 0
            if event.key == pygame.K_DOWN:
                down = 1
                up = 0
                left = 0
                right = 0
            if event.key == pygame.K_LEFT:
                left = 1
                down = 0
                up = 0
                right = 0
            if event.key == pygame.K_RIGHT:
                right = 1
                left = 0
                up = 0
                down = 0

    clock.tick(15)
    screen.fill(black)

    pygame.draw.rect(screen, pure_red,(foodx,foody,10,10),0)
    for segment in snake_list:
        pygame.draw.rect(screen, pure_blue,(segment[0],segment[1],10,10),0)

    if up == 1:
        snakey -= 10
    if down == 1:
        snakey += 10
    if right == 1:
        snakex += 10
    if left == 1:
        snakex -= 10

    snake_list.append([snakex,snakey])
    snake_list.pop(0)
    
    if [snakex,snakey] in snake_list[:-1]:
        print("your score is", score)
        pygame.quit()
        exit()

    if snakex < 0 or snakex > 640:
        print("your score is", score)
        pygame.quit()
        exit()
    if snakey < 0 or snakex > 480:
        print("your score is", score)
        pygame.quit()
        exit()

    if snakex == foodx and snakey == foody:
        foodx = (random.randint(0,640) // 10 ) * 10
        foody = (random.randint(0,480) // 10 ) * 10
        score+=1
        snake_list.append([foodx,foody])

    #Continuously update the screen
    pygame.display.update()