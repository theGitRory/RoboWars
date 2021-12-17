import pygame
import math
from Robot import Robot

class DanielRobot(Robot):
    def __init__(self, image, name):
        super().__init__(image, name)
    
    def update(self):
        super().update()
        state = self.state
        #self.moveDown()
        #self.turnRight()
        #print(str(state))
        
        if(state == {}):
            return
        
        if "AIRobot" in state:
            self.turnTowards(state["AIRobot"])
            if self.isLookingAt(state["AIRobot"]):
                self.shoot()
        
        #self.moveUp()
        #self.moveLeft()
        #self.moveRight()