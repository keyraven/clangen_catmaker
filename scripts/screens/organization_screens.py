import scripts.screens.base_screens as base_screens
import pygame_gui
import scripts.game_structure.image_button as custom_buttons
import pygame
import scripts.global_vars
from scripts.utility import update_sprite

class StartScreen(base_screens.Screens):

    def __init__(self, name):
        self.start_button = None
        super().__init__(name)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.start_button:
                self.change_screen("creation screen")

    def screen_switches(self):
        self.start_button = pygame_gui.elements.UIButton(pygame.Rect((350, 200), (100, 50)), "Start")

    def exit_screen(self):
        self.start_button.kill()
        self.start_button = None
