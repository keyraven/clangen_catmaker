import scripts.screens.base_screens as base_screens
import pygame_gui
import scripts.game_structure.image_button as custom_buttons
import pygame
from scripts.utility import update_sprite
from scripts.game_structure.image_cache import load_image

class StartScreen(base_screens.Screens):

    def __init__(self, name="start"):
        self.start_button = None
        self.title = None
        self.version = None
        super().__init__(name)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.start_button:
                self.change_screen("creation")

    def screen_switches(self):
        
        self.icon = pygame_gui.elements.UIImage(pygame.Rect((0, 100), (76, 84)),
                                                pygame.transform.scale(
                                                    load_image("resources/images/icon.png"),
                                                    (76, 84)),
                                                anchors={
                                                    "centerx":"centerx"
                                                }
                                                )
        
        self.title = pygame_gui.elements.UITextBox("ClanGen CatMaker", pygame.Rect((0, 200), (800, 100)),
                                                   object_id="#title")
        self.start_button = pygame_gui.elements.UIButton(pygame.Rect((350, 320), (100, 50)), "Start")
        self.version = pygame_gui.elements.UITextBox("Version 0.5.0beta"
                                                     "\n Please don't sell any images created, and give proper credit. ", pygame.Rect((250, 400), (300, 100)),
                                                     object_id="#version")
        
    def exit_screen(self):
        self.start_button.kill()
        self.start_button = None
        self.title.kill()
        self.title = None
        self.version.kill()
        self.version = None
        self.icon.kill()
        self.icon = None
