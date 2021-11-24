import pygame

class BulletManager():

    SINGLETON = None

    def __init__(self, screen):
        self.screen = screen
        self.__bulletArr = []

    def draw(self, screen):     
        for p in self.getBullets():
            p.draw(screen)   

    @staticmethod
    def getBulletManager():
        return BulletManager.SINGLETON
    
    @staticmethod
    def createBulletManager(screen):
        BulletManager.SINGLETON = BulletManager(screen)
        return BulletManager.SINGLETON

    def addBullets(self, bullet):
        self.__bulletArr.append(bullet)

    def getBullets(self):
        return self.__bulletArr

    def update(self, event, dt):
        for i in self.__bulletArr:
            if i.update(event, dt):
                i.draw(self.screen)
            else:
                self.__bulletArr.remove(i)
