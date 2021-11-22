import pygame
from AIRobot import AIRobot
from DanielRobot import DanielRobot
from RobotManager import RobotManager
from Settings import Settings
from Ui import Ui

pygame.init()
pygame.font.init() 

screen = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT])
running = True
myRobotManager = RobotManager()
myRobotManager.addAllRobots()

myUi = Ui(myRobotManager.getRobots())

Settings.lastUpdatedTick = pygame.time.get_ticks()

def draw(): 
    screen.fill((255, 255, 255))  
    # 
    #
    #
    myUi.draw(screen)
    #
    #   
    #
    pygame.display.flip()

def update():
    myRobotManager.update()


while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    

    # Only update/draw when ticks passed tickrate
    if(pygame.time.get_ticks() - Settings.lastUpdatedTick > Settings.TICK_RATE):
        Settings.lastUpdatedTick = pygame.time.get_ticks()
        update()
        draw()
