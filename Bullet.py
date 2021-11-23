
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load('bullet.png').convert_alpha(), (10,10))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8
        self.pos = pygame.math.Vector2(x, y)
        self.dir = pygame.math.Vector2(dx, dy).normalize()
