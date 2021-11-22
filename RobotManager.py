import pygame
from AIRobot import AIRobot
from DanielRobot import DanielRobot

class RobotManager():
    def __init__(self):
        self.__robotarr = []
        self.__sprites = pygame.sprite.Group()
        pass

    def addRobot(self, robot):
        self.__robotarr.append(robot)
        self.__sprites.add(robot)

    def addAllRobots(self):
        self.addRobot(DanielRobot(150, 150, "robot.png", "DanielRobot"))
        self.addRobot(AIRobot(300, 300, "robot2.png", "AIRobot"))

    def getRobots(self):
        return self.__robotarr

    def update(self):
        for p in self.__robotarr:
            if p.isAlive():
                p.updateBegin()
                p.update()