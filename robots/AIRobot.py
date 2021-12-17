import pygame
from Robot import Robot

class AIRobot(Robot):
    def __init__(self, image, name):
        super().__init__( image, name)
        self.movingLeft = True
        self.movingRight = False
        self.movingUp = False
        self.movingDown = True

    def update(self):
        super().update()

        self.turnLeft()
        self.shoot()

        if self.movingLeft:
            self.movingLeft = self.moveLeft()
            if not self.movingLeft:
                self.movingRight = True
            if self.movingUp:    
                self.movingUp = self.moveUp()
                if not self.movingUp:
                    self.movingDown = True
            else:
                self.movingDown = self.moveDown()
                if not self.movingDown:
                    self.movingUp = True
        else:
            self.movingRight = self.moveRight()
            
            if not self.movingRight:
                self.movingLeft = True
            
            if self.movingDown:           
                self.movingDown = self.moveDown()
                if not self.movingDown:
                    self.movingUp = True
            else:
                self.movingUp = self.moveUp()
                if not self.movingUp:
                    self.movingDown = True
        
