import sys
import pygame
import random
from tkinter import *
from tkinter import messagebox

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1366,768), pygame.FULLSCREEN | pygame.RESIZABLE)

bg = pygame.image.load("background.png")
chicken = pygame.image.load("chicken.png")
shell = pygame.image.load("shell.png")
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
delta = 0.0
time = 0.0
End = 0
endTime = 60
amountShells = 5
kills = 0
isChickenVisible = 0
x = 0 
y = 0
myList = [1.0, 2.0, 3.0, 4.0]
ChickenTimeDisplay = random.choice(myList)
XChicken = random.randint(0, 1200)
YChicken = random.randint(0, 570)

#Font
myfont = pygame.font.SysFont('Comic Sans MS', 80)

Tk().wm_withdraw() #to hide the main window

while True:
    screen.blit(bg, (0, 0))
    delta += clock.tick()/1000.0

    #Time display
    time += clock2.tick()/1000.0
    End = endTime - int(time)
    textsurface = myfont.render(str(End), False, (255, 0, 0))
    screen.blit(textsurface, (10, 660))
    if End == -1:
        message = messagebox.showinfo("Koniec!","Uzyskales " + str(kills) + " punktow.\n")
        break;

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            amountShells = 5
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            amountShells -= 1
            if XChicken < pos[0] and XChicken+150 > pos[0] and YChicken < pos[1] and YChicken+200 > pos[1] and amountShells >= 0 and isChickenVisible == 1:
                isChickenVisible = 0
                kills += 1
                delta = 0.0
                ChickenTimeDisplay = random.choice(myList)
                XChicken = random.randint(0, 1200)
                YChicken = random.randint(0, 570)     

    #Chicken display
    if delta > ChickenTimeDisplay and delta < ChickenTimeDisplay+2.5:
        isChickenVisible = 1
        screen.blit(chicken, (XChicken, YChicken))
    if delta > 4.5:
        isChickenVisible = 0
        delta = 0.0
        ChickenTimeDisplay = random.choice(myList)
        XChicken = random.randint(0, 1200)
        YChicken = random.randint(0, 570)
        
    
    #Shell display
    p = 10
    for y in range (0, amountShells):
        screen.blit(shell, (1210+p, 650))
        p += 25

    pygame.display.flip() 