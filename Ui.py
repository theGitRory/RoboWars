import pygame
from Settings import Settings

class Ui():
    def __init__(self, robotArr):
        self.robotArr = robotArr

    def draw(self, screen):
        for p in self.robotArr:
            #if p.isAlive():
            p.draw(screen)
    