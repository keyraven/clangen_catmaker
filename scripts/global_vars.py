import pygame
import pygame_gui

pygame.init()
screen_x, screen_y = 800, 700
SCREEN = pygame.display.set_mode((screen_x, screen_y))
MANAGER = pygame_gui.ui_manager.UIManager((screen_x, screen_y), 'resources/defaults.json')

import scripts.cat.cats

CREATED_CAT = scripts.cat.cats.Cat()