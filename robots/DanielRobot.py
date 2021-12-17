import pygame
import math
from Robot import Robot

class DanielRobot(Robot):
    def __init__(self, image, name):
        super().__init__(image, name)
    
    def update(self):
        super().update()
        state = self.state
        
        if(state == {}):
            return
        
        if "AIRobot" in state:
            self.turnTowards(state["AIRobot"])
            if self.isLookingAt(state["AIRobot"]):
                self.shoot()
        elif "MicroManRobot" in state:
            self.turnTowards(state["MicroManRobot"])
            if self.isLookingAt(state["MicroManRobot"]):
                self.shoot()
        elif "SlowRobot" in state:
            self.turnTowards(state["SlowRobot"])
            if self.isLookingAt(state["SlowRobot"]):
                self.shoot()