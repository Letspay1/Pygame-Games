#import pygame and initialize the pygame engine.
import pygame
#initialize pygame
pygame.init()
#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((600,600))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")
# Colors
yellow = (235,225,0) 
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
white = (255,255,255)
# Define the text function
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont('freesans',128)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
# Dictionary for square values
squares = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
block = 0
# Flag variables for whether x or o is playing
turn = 1
# Draw the board
pygame.draw.line(screen,white,(0,200),(600,200),10)
pygame.draw.line(screen,white,(0,400),(600,400),10)
pygame.draw.line(screen,white,(200,0),(200,600),10)
pygame.draw.line(screen,white,(400,0),(400,600),10)
#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if 0 < x < 200 and 0 < y < 200:
                x = 50
                y = 25
                block = 1
            if 200 < x < 400 and 0 < y < 200:
                x = 250
                y = 25
                block = 2
            if 400 < x < 600 and 0 < y < 200:
                x = 450
                y = 25
                block = 3
            if 0 < x < 200 and 200 < y < 400:
                x = 50
                y = 225
                block = 4
            if 200 < x < 400 and 200 < y < 400:
                x = 250
                y = 225
                block = 5
            if 400 < x < 600 and 200 < y < 400:
                x = 450
                y = 225
                block = 6
            if 0 < x < 200 and 400 < y < 600:
                x = 50
                y = 425
                block = 7
            if 200 < x < 400 and 400 < y < 600:
                x = 250
                y = 425
                block = 8
            if 400 < x < 600 and 400 < y < 600:
                x = 450
                y = 425
                block = 9
            if turn == 1 and squares[block] == " ":
                show_text("X",x,y,pure_red)
                turn+=1
                squares[block] = "X"
            elif turn == 2 and squares[block] == " ":
                show_text("O",x,y,pure_blue)
                turn-=1
                squares[block] = "O"
            if squares[1] == squares[2] == squares[3] and squares[1] != " ":
                print("player", squares[1], "won the game!")
                pygame.quit()
                exit()
            elif squares[1] == squares[5] == squares[9] and squares[1] != " ":
                print("player", squares[1], "won the game!")
                pygame.quit()
                exit()
            elif squares[3] == squares[5] == squares[7] and squares[3] != " ":
                print("player", squares[3], "won the game!")
                pygame.quit()
                exit()
            elif squares[3] == squares[6] == squares[9] and squares[3] != " ":
                print("player", squares[3], "won the game!")
                pygame.quit()
                exit()
            elif squares[1] == squares[4] == squares[7] and squares[1] != " ":
                print("player", squares[1], "won the game!")
                pygame.quit()
                exit()
            elif squares[7] == squares[8] == squares[9] and squares[7] != " ":
                print("player", squares[7], "won the game!")
                pygame.quit()
                exit()
            elif squares[4] == squares[5] == squares[6] and squares[4] != " ":
                print("player", squares[4], "won the game!")
                pygame.quit()
                exit()
            elif squares[2] == squares[5] == squares[8] and squares[2] != " ":
                print("player", squares[2], "won the game!")
                pygame.quit()
                exit()

    #Continuously update the screen
    pygame.display.update()