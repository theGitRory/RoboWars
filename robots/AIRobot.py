import pygame
from Robot import Robot

class AIRobot(Robot):
    def __init__(self, x, y, image, name):
        super().__init__(x, y, image, name)
        self.movingLeft = True
        self.movingRight = False

    def update(self):
        super().update()
        if self.movingLeft:
            self.movingLeft = self.moveLeft()
        else:
            self.movingRight = self.moveRight()
            if not self.movingRight:
                self.movingLeft = True
        
