import scripts.screens.base_screens as base_screens
import pygame_gui
import pygame
import scripts.global_vars
from scripts.utility import update_sprite

class CreationScreen(base_screens.Screens):
    pelt_options = ["Tabby", "Plain", "Classic", "Single Stripe", "Tortie/Calico"]
    white_patches = ["None", "Ravenpaw", "Any"]
    tints = ["None", "Blue", "Pink"]
    scars = ["None"]

    def __init__(self, name):
        self.general_tab = None
        self.pattern_tab = None
        self.extras_tab = None
        self.cat_image = None

        super().__init__(name)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            pass

    def screen_switches(self):
        update_sprite(scripts.global_vars.CREATED_CAT)

        self.cat_image = pygame_gui.elements.UIImage(pygame.Rect((250, 100), (300, 300)),
                                                     scripts.global_vars.CREATED_CAT.sprite)

        # Tabs

        self.general_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((120, 350), (560, 325)),
                                                                    scripts.global_vars.MANAGER)

        self.pattern_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((120, 350), (560, 325)),
                                                                    scripts.global_vars.MANAGER,
                                                                    visible=False)

        self.extras_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((120, 350), (560, 325)),
                                                                   scripts.global_vars.MANAGER,
                                                                   visible=False)


        #General Tab Contents
        self.pelt_select = pygame_gui.elements.UIDropDownMenu(self.pelt_options, "Plain", pygame.Rect((),()))

        #White Patches
        self.white_patches_select = pygame_gui.elements.UIDropDownMenu(self.white_patches, "None", pygame.Rect((),()))

        #Tint
        self.tint_select = pygame_gui.elements.UIDropDownMenu(self.tints, "None", pygame.Rect((), ()))

        # Hetero Check-mark

        # Eye Color Type
        self.eye_color1 = pygame_gui.elements.UIDropDownMenu(self.tints, "None", pygame.Rect((), ()))

        self.eye_color2 = pygame_gui.elements.UIDropDownMenu(self.tints, "None", pygame.Rect((), ()))

        #Scars
        self.scar1 = pygame_gui.elements.UIDropDownMenu(self.scars, "None", pygame.Rect((), ()))
        self.scar2 = pygame_gui.elements.UIDropDownMenu(self.scars, "None", pygame.Rect((), ()))
        self.scar3 = pygame_gui.elements.UIDropDownMenu(self.scars, "None", pygame.Rect((), ()))
        self.scar4 = pygame_gui.elements.UIDropDownMenu(self.scars, "None", pygame.Rect((), ()))


    def open_basics_tab(self):
        pass

    def open_pattern_tab(self):
        pass

    def open_extras_tab(self):
        pass


