import sys
import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship
import game_functions as gf

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load("C:\\Users\\User\\Desktop\\wuliuyu\\exercise\\python\\ship_alien\\images\\alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def blitme(self):

        self.screen.blit(self.image, self.rect)