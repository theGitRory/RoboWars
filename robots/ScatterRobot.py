import pygame
from Robot import Robot

class ScatterRobot(Robot):
    def __init__(self, image, name):
        super().__init__(image, name)

    def update(self):
        super().update()

        self.turnLeft()
        self.shoot()
        self.turnLeft()
        self.shoot()
        self.turnLeft()
        self.shoot()
        self.turnLeft()
        self.shoot()