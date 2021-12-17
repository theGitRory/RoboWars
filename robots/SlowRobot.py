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
        
        SlowRobot.moveState = SlowRobot.moveState + 1
        
        if((SlowRobot.moveState)% 25 == 0 or SlowRobot.moveState < 0):
        
            preX = self.getRect().centerx
            preY = self.getRect().centery
            
            
            
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
            


            SlowRobot.shootState = SlowRobot.shootState + 1
            
            if((SlowRobot.shootState)% 10 == 0):
                self.shoot()