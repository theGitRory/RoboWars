import pygame
import random
from Robot import Robot

class MadRobot(Robot):
    moveState = 0
    def __init__(self, image, name):
        super().__init__( image, name)
        self.movingLeft = True
        self.movingRight = False
        self.movingUp = False
        self.movingDown = True

    def update(self):
        super().update()
        
        state = self.state
        if ("DanielRobot" in state or "MicroManRobot" in state or "SlowRobot" in state or "ScatterRobot" in state or "AIRobot" in state):
            self.moveState = self.moveState + 1
        else:
            self.turnRight()
            self.shoot()
            self.turnRight()
            self.shoot()
            self.turnRight()
            self.shoot()
            self.turnRight()
            self.shoot()
            
        if((self.moveState)% 55 == 0):
            #change direction randomly every so often!
            rando = random.randint(0, 3)
            if rando == 0:
                self.movingLeft = True
                self.movingRight = False
                self.movingUp = False
                self.movingDown = True
            elif rando == 1:
                self.movingLeft = True
                self.movingRight = False
                self.movingUp = True
                self.movingDown = False
            elif rando == 2:
                self.movingLeft = False
                self.movingRight = True
                self.movingUp = False
                self.movingDown = True
            elif rando == 3:
                self.movingLeft = False
                self.movingRight = False
                self.movingUp = True
                self.movingDown = False

        
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
        
        
        if self.movingLeft and self.movingUp:
            self.turnTowardsAngle(135)
        elif self.movingLeft and self.movingDown:
            self.turnTowardsAngle(-135)
        elif self.movingRight and self.movingUp:
            self.turnTowardsAngle(45)
        else:
            self.turnTowardsAngle(-45)

        self.shoot()