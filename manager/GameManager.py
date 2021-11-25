import pygame
from Settings import Settings
from manager.RobotManager import RobotManager
from manager.BulletManager import BulletManager

class GameManager():

    SINGLETON = None

    def __init__(self, screen, sprites):
        self.myBulletManager = BulletManager.createBulletManager(screen)
        self.myRobotManager =  RobotManager.createRobotManager(sprites)  
        pass

    def update(self, events, dt):
        self.myBulletManager.update(events, dt)
        self.myRobotManager.update(events)
        
        roboArr = RobotManager.getRobotManager().getRobots()
        bulletArr = BulletManager.getBulletManager().getBullets()

        for robo in roboArr:
            for bullet in bulletArr:
                if robo.isAlive() and bullet.getRobotName() != robo.getRobotName() and bullet.getRect().colliderect(robo.getRect()):
                    robo.takeDamage(Settings.BULLET_DAMANGE)
                    bullet.destroy()
                    pass

    def draw (self, screen):
        self.myBulletManager.draw(screen)
        self.myRobotManager.draw(screen)
        
    def checkCollision(self, rect, name):
        roboArr = RobotManager.getRobotManager().getRobots()

        for robo in roboArr:
            if robo.isAlive() and name != robo.getName() and rect.colliderect(robo.getRect()):
                return True
        
        return False


    @staticmethod
    def getGameManager():
        return GameManager.SINGLETON
    
    @staticmethod
    def createGameManager(screen, sprite):
        GameManager.SINGLETON = GameManager(screen, sprite)
        return GameManager.SINGLETON
