import sys
import os
directory = os.path.dirname(__file__)
if directory:
    os.chdir(directory)
import pygame
import ujson
import pygame_gui

pygame.init()

window_surface = pygame.display.set_mode((800, 700))
manager = pygame_gui.ui_manager.UIManager((800, 700), 'resources/defaults.json')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
