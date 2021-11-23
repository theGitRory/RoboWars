import pygame
from AIRobot import AIRobot
from DanielRobot import DanielRobot

class RobotManager():
    def __init__(self, sprites):
        self.__robotarr = []
        self.__sprites = sprites
        self.addRobot(DanielRobot(150, 150, "robot.png", "DanielRobot"))
        self.addRobot(AIRobot(300, 300, "robot2.png", "AIRobot"))

    def addRobot(self, robot):
        self.__robotarr.append(robot)
        self.__sprites.add(robot)

    def getRobots(self):
        return self.__robotarr

    def update(self, events):
        for p in self.__robotarr:
            if p.isAlive():
                p.updateBegin()
                p.update()
    
    def draw(self, screen):
        for p in self.getRobots():
            p.draw(screen)