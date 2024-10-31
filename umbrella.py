import pygame
import random
from gameSprite import GameSprite
from pygame.locals import RLEACCEL

from screen import Screen


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class Umbrella(GameSprite):
    Max_Speed_y = 15
    Min_Speed_y = 7

    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(50, Screen.width),
                0
            )
        )
        self.__speed_y = random.randint(self.Min_Speed_y, self.Max_Speed_y)
        self.time = 0

    # Move the bird based on speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.time += 1

        self.rect.move_ip(-5, self.__speed_y)
        if self.rect.right < 0 or self.rect.bottom > Screen.height:
            self.kill()

    def clone(self):
        return Umbrella()
