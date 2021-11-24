import pygame
from Robot import Robot

class DanielRobot(Robot):
    def __init__(self, x, y, image, name):
        super().__init__(x, y, image, name)
    
    def update(self):
        super().update()
        #self.moveDown()
        self.turnRight()
        self.shoot()
        #self.moveUp()
        #self.moveLeft()
        #self.moveRight()

    def draw(self, screen):
        super().draw(screen)
        Color_line=(255,0,0)
        x = self.getRect().centerx
        y = self.getRect().centery

        pygame.draw.line(screen, Color_line, (x, y), (500, 500))