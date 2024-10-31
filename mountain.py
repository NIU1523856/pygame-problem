import pygame
from gameSprite import GameSprite
from pygame.locals import RLEACCEL

from screen import Screen

# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Mountain(GameSprite):
    def __init__(self):
        super(Mountain, self).__init__()
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                Screen.width + 100,
                Screen.height
            )
        )

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        return Mountain()