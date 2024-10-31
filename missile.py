import pygame
import random
from gameSprite import GameSprite
from pygame.locals import RLEACCEL

from screen import Screen

# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Missile(GameSprite):

    def __init__(self):
        super(Missile, self).__init__()
        self.surf = pygame.image.load("icons/missile.png")
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                Screen.width + 20,
                random.randint(0, Screen.height)
            )
        )
        self.__speed = 40
        self.time = 0

    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.time += 1
        self.rect.move_ip(-self.__speed, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Missile()
