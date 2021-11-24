import pygame
from manager.BulletManager import BulletManager
from manager.RobotManager import RobotManager

class GameManager():

    SINGLETON = None

    def __init__(self):
        pass

    def checkCollisions(self):
        pass

    def update(self):
        roboArr = RobotManager.getRobotManager().getRobots()
        bulletArr = BulletManager.getBulletManager().getBullets()

        for robo in roboArr:
            for bullet in bulletArr:
                if robo.isAlive() and bullet.getRobotName() != robo.getRobotName() and bullet.getRect().colliderect(robo.getRect()):
                    robo.takeDamage(10)
                    bullet.destroy()
                    pass
        


    @staticmethod
    def getGameManager():
        return GameManager.SINGLETON
    
    @staticmethod
    def createGameManager():
        GameManager.SINGLETON = GameManager()
        return GameManager.SINGLETON
