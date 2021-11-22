import pygame
from Robot import Robot

class DanielRobot(Robot):
    def __init__(self, x, y, image, name):
        super().__init__(x, y, image, name)
    
    def update(self):
        #self.moveDown()
        self.turnRight()

        #self.moveUp()
        #self.moveLeft()
        #self.moveRight()