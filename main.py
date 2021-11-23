import pygame
from AIRobot import AIRobot
from DanielRobot import DanielRobot
from RobotManager import RobotManager
from Settings import Settings
from BulletManager import BulletManager
pygame.init()
pygame.font.init() 

screen = pygame.display.set_mode([Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT])
sprites = pygame.sprite.Group()

running = True

clock = pygame.time.Clock()

myBulletManager = BulletManager.createBulletManager(screen)
myRobotManager =  RobotManager(sprites)

Settings.lastUpdatedTick = pygame.time.get_ticks()

def draw(): 
    screen.fill((255, 255, 255))  
    # 
    #
    #
    myBulletManager.draw(screen)
    myRobotManager.draw(screen)
    #
    #   
    #
    pygame.display.flip()

def update(events, dt):
    myBulletManager.update(events, dt)
    myRobotManager.update(events)

clock = pygame.time.Clock()

while running:
    # Did the user click the window close button?
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False    

    # Only update/draw when ticks passed tickrate
    if(pygame.time.get_ticks() - Settings.lastUpdatedTick > Settings.TICK_RATE):
        Settings.lastUpdatedTick = pygame.time.get_ticks()
        update(events, dt)
        draw()
    
    dt = clock.tick(60)

