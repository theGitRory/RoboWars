import pygame
from Robot import Robot

class SlowRobot(Robot):
    moveState = -15
    shootState = 0
    def __init__(self, image, name):
        super().__init__(image, name)
        self.movingLeft = False
        self.movingRight = True
        self.movingUp = False
        self.movingDown = True

    def update(self):
        super().update()
        
        state = self.state
        
        if ("DanielRobot" in state or "MadRobot" in state or "AIRobot" in state or "ScatterRobot" in state or "MicroManRobot" in state):
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
            
        if((self.moveState)% 25 == 0 or self.moveState < 0):
            
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

            self.shootState = self.shootState + 1
            
            if((self.shootState)% 10 == 0):
                self.shoot()
