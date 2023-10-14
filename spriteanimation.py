#import pygame and initialize the pygame engine.
import pygame
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((640,480))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
# Clock
clock = pygame.time.Clock()
#Colors
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
black = (0,0,0)
# coordinates
x = 100
y = 100
# Image variables
dog_idle_right=[]
dog_idle_left=[]
dog_walk_right=[]
dog_walk_left=[]
dog_jump_right=[]
dog_jump_left=[]
dog_fall_right=[]
dog_fall_left=[]
width = 80
height = 70
def loadingimages():
    for i in range(1,11,1):
        dog_path=f"dog/Idle ({str(i)}).png"
        dog=pygame.image.load(dog_path)
        dog=pygame.transform.scale(dog,(width,height))
        dog_idle_right.append(dog)
        dog = pygame.transform.flip(dog, True, False)
        dog_idle_left.append(dog)
        dog_path=f"dog/Walk ({str(i)}).png"
        dog=pygame.image.load(dog_path)
        dog=pygame.transform.scale(dog,(width, height))
        dog_walk_right.append(dog)
        dog = pygame.transform.flip(dog, True, False)
        dog_walk_left.append(dog)
    for j in range(1,9,1):
        jump_path = f"dog/Jump ({str(j)}).png"
        jump = pygame.image.load(jump_path)
        jump = pygame.transform.scale(jump, (80, 70))
        dog_jump_right.append(jump)
        jump = pygame.transform.flip(jump, True, False)
        dog_jump_left.append(jump)
        fall_path = f"dog/Fall ({str(j)}).png"
        fall = pygame.image.load(fall_path)
        fall = pygame.transform.scale(fall, (80, 70))
        dog_fall_right.append(fall)
        fall = pygame.transform.flip(fall, True, False)
        dog_fall_left.append(fall)

def idle_right():
    global i, x, y
    screen.blit(dog_idle_right[i],(x,y))
def idle_left():
    global i, x, y
    screen.blit(dog_idle_left[i],(x,y))
def walk_right():
    global i, x, y
    screen.blit(dog_walk_right[i],(x,y))
    x = x+5
def walk_left():
    global i, x, y
    screen.blit(dog_walk_left[i],(x,y))
    x = x-5
def jump_right():
    global x, y
    for a in range(0,8,1):
        if a < 4:
            y=y-10
        else:
            y=y+10
        screen.blit(dog_jump_right[a],(x,y))
        pygame.display.update()
        screen.fill(black)
        clock.tick(12)
        x = x+5
def jump_left():
    global x, y
    for a in range(0,8,1):
        if a < 4:
            y=y-10
        else:
            y=y+10
        screen.blit(dog_fall_left[a], (x,y))
        pygame.display.update()
        screen.fill(black)
        clock.tick(12)
        x = x-5

loadingimages()
i = 0
# Flag variables for keys
left = 0
right = 0
up = 0
lastkeypressed = "right"
#The Game Loop”
while True:
    screen.fill(black)
    #Most of our game logic goes here   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right = 1
                left = 0
            if event.key == pygame.K_LEFT:
                left = 1
                right = 0
            if event.key == pygame.K_UP:
                up = 1
                
        if event.type == pygame.KEYUP:
            if left == 1:
                lastkeypressed = "left"
                left = 0
            if right == 1:
                lastkeypressed = "right"
                right = 0
            # if lastkeypressed == "right":
            #     screen.fill(black)
            #     idle_right()
            # if lastkeypressed == "left":
            #     screen.fill(black)
            #     idle_left()

    if up == 1 and right == 1:
        jump_right()
        up = 0
    elif up == 1 and left == 1:
        jump_left()
        up = 0
    elif left == 1:
        #screen.fill(black)
        walk_left()
    elif right == 1:
        #screen.fill(black)
        walk_right()
    elif left == 0 and right == 0:
        if lastkeypressed == "right":
            idle_right()
        if lastkeypressed == "left":
            screen.fill(black)
            idle_left()

    clock.tick(20)

    i+=1
    if i == 10:
        i = 0
    #Continuously update the screen
    pygame.display.update()