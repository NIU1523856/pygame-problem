import pygame
from factorySprites import FactorySprites
from game import Game
from screen import Screen
from bird import Bird
from cloud import Cloud
from missile import Missile
from jet import Jet
from umbrella import Umbrella
from mountain import Mountain

level = input("Select mode(easy = e/medium = m/difficult = d): ")

# Initialize PyGame
# setup for sounds_music, defaults are good
pygame.mixer.init()
pygame.init()
# create the screen object
pygame.display.set_mode((Screen.width, Screen.height))

# play
if level == 'e':
    # easy mode, only birds and clouds
    factory_flying = FactorySprites([Bird()], [300], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud()], [400], pygame.USEREVENT + 10)

elif level == 'm':
    factory_flying = FactorySprites([Bird(), Umbrella()], [400, 500], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [500, 2000], pygame.USEREVENT + 10)

elif level == 'd':
    factory_flying = FactorySprites([Bird(), Umbrella(), Jet(), Missile()], [400, 500, 2000, 1500], pygame.USEREVENT + 1)
    factory_landscape = FactorySprites([Cloud(), Mountain()], [500, 2000], pygame.USEREVENT + 10)

else:
    assert False

game = Game(factory_flying, factory_landscape)
game.play()