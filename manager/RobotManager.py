import pygame

class RobotManager():
    SINGLETON = None

    def __init__(self, sprites):
        self.__robotarr = []
        self.__sprites = sprites
        self.__posArray = []
        self.__posArray.append(pygame.Vector2(150, 150))
        self.__posArray.append(pygame.Vector2(300, 300))
        self.__posArray.append(pygame.Vector2(550, 550))

        self.__posArray.append(pygame.Vector2(700, 700))
        self.__posArray.append(pygame.Vector2(750, 750))




    def addRobot(self, robot):
        print(str(len(self.__robotarr)))

        robot.getRect().centerx = self.__posArray[len(self.__robotarr)].x
        robot.getRect().centery = self.__posArray[len(self.__robotarr)].y

        self.__robotarr.append(robot)
        self.__sprites.add(robot)

    @staticmethod
    def getRobotManager():
        return RobotManager.SINGLETON
    
    @staticmethod
    def createRobotManager(sprites):
        RobotManager.SINGLETON = RobotManager(sprites)
        return RobotManager.SINGLETON

    def getRobots(self):
        return self.__robotarr

    def getState(self):
        state = {}
        for p in self.__robotarr:
            if(p.isAlive()):
                state[p.getRobotName()] = {"health": p.getHealth(), "loc": p.getRect(), "angle": p.getAngle(), "centerx": p.getRect().centerx,  "centery": p.getRect().centery}
                pass
            pass       
        return state 

    def update(self, events):
        for p in self.__robotarr:
            if p.isAlive():
                p.updateBegin()
                p.update()

        state = self.getState()

        for p in self.__robotarr:
            if p.isAlive():  
                  p.updateEnd(state)
    
    def draw(self, screen):
        for p in self.getRobots():
            p.draw(screen)