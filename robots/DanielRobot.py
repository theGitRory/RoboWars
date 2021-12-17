import pygame
import math
from Robot import Robot

class DanielRobot(Robot):
    def __init__(self, x, y, image, name):
        super().__init__(x, y, image, name)
    
    def update(self):
        super().update()
        state = self.state
        #self.moveDown()
        #self.turnRight()
        #print(str(state))
        
        if(state == {}):
            return
        
        if self.turnLeftTowards(state["AIRobot"]):
            #print("left")
            self.turnLeft()
        else:
            #print("Right") 
            self.turnRight()

        if self.isLookingAt(state["AIRobot"]):
            self.shoot()
        
        #self.moveUp()
        #self.moveLeft()
        #self.moveRight()

    def draw(self, screen):
        super().draw(screen)
        Color_line=(255,0,0)
        x = self.getRect().centerx
        y = self.getRect().centery
        lineLength = 350
        
        x2 = x + (lineLength * math.cos((self.getAngle()%360)*(math.pi/180)))
        y2 = (y + (lineLength * math.sin((self.getAngle()%360)*(math.pi/180))) * (-1))
        #print(f'centre:  {x},{y} new point {x2},{y2} angle: {(self.getAngle()%360):.2f}')
        
        pygame.draw.line(screen, Color_line, (x, y), (x2, y2))