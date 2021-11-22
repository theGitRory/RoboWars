import pygame
from Settings import Settings
from abc import abstractmethod


class Robot(pygame.sprite.Sprite):

    def __init__(self, x, y, image, name):
        super(Robot, self).__init__()
        self.__surf = pygame.image.load(image).convert()
        self.__originalsurf = pygame.image.load(image).convert()
        self.__rect = self.__surf.get_rect()
        self.__name = name
        self.__angle = 0
        #
        #   Settings
        #
        self.__speed = Settings.SPEED
        self.__health = Settings.HEALTH
        self.__rect.centery = y
        self.__rect.centerx = x
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)
        self.__textSurface = self.myfont.render(self.getName() + " - " + str(self.getHealth()), False, (0, 0, 0))
        self.__isAlive = True
        self.__commandsIssued = 0

    def getName(self):
        return self.__name

    def getTextSurface(self):
        return self.__textSurface

    def getImageSize(self):
        return self.__surf.get_size()

    def getOriginalSize(self):
        return self.__originalsurf.get_size()

    def getHealth(self):
        return self.__health

    def turn(self, angle):
        if self.canRunCommand():
            self.__angle += angle
            self.__surf = pygame.transform.rotate(self.__originalsurf, self.__angle)
            x = self.__rect.centerx
            y = self.__rect.centery
            self.__rect = self.__surf.get_rect(center = self.__originalsurf.get_rect(center = (x, y)).center)
            self.__commandsIssued += 1

    def turnLeft(self):
        self.turn(Settings.TURN_SPEED)

    def turnRight(self):
        self.turn(-Settings.TURN_SPEED)        
    
    def takeDamage(self, amount):
        self.__health -= amount
        self.__textSurface = self.myfont.render(self.getName() + " - " + str(self.getHealth()), False, (0, 0, 0))

    def isAlive(self):
        if self.getHealth() <= 0:
            self.__isAlive = False
        return self.__isAlive

    def getSurf(self):
        return self.__surf

    def updateBegin(self):
        self.__commandsIssued = 0
    
    def getRect(self):
        return self.__rect

    def move(self):
        if self.canRunCommand():
            if self.__rect.centerx < Settings.SCREEN_WIDTH - (self.getImageSize()[0] / 2):
                self.__rect.centerx += self.__speed
                self.__commandsIssued += 1

    def canRunCommand(self):
        boolVal = self.isAlive() and self.__commandsIssued < Settings.MAX_COMMANDS_PER_TICK
        return boolVal

    def __move(self, x, y):
        self.__rect = self.__rect.move(x, y)
        self.__commandsIssued += 1
        pass

    def moveLeft(self):
        if self.canRunCommand():
            if self.__rect.centerx > (self.getImageSize()[0] / 2):
                self.__rect = self.__rect.move(-Settings.SPEED, 0)
                self.__commandsIssued += 1
           

    def moveRight(self):
        if self.canRunCommand():
            if self.__rect.centerx < Settings.SCREEN_WIDTH - (self.getImageSize()[0] / 2):
                self.__rect = self.__rect.move(Settings.SPEED, 0)
                self.__commandsIssued += 1


    def moveUp(self):
        if self.canRunCommand():
            if self.__rect.centery > (self.getOriginalSize()[1] / 2):
                self.__rect = self.__rect.move(0, -Settings.SPEED)
                self.__commandsIssued += 1


    def moveDown(self):
        if self.canRunCommand():
            if self.__rect.centery < Settings.SCREEN_HEIGHT - (self.getImageSize()[0] / 2):
                self.__rect = self.__rect.move(0, Settings.SPEED)
                self.__commandsIssued += 1

    def draw(self, screen):
        # Draw the actual robot
        screen.blit(self.getSurf(), self.getRect())  

        # Hard coded offsets, need to investigate font/image size/image location 
        # Draws the UI Text
        x = self.getRect().centerx - (self.getOriginalSize()[0] - 120)
        y = self.getRect().centery - (self.getOriginalSize()[1] - 60)
        screen.blit(self.getTextSurface(),(x, y))

    @abstractmethod
    def update(self):
        raise Exception('Update method not implemented')