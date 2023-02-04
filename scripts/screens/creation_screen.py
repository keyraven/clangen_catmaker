import scripts.screens.base_screens as base_screens
import pygame_gui
import pygame
import scripts.global_vars
from scripts.utility import update_sprite
from scripts.game_structure.image_cache import load_image
import scripts.game_structure.image_button as custom_buttons

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
        self.back = None
        self.randomize = None
        self.clear = None
        self.done = None
        self.tab_background = None

        super().__init__(name)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.general_tab_button:
                self.general_tab_button.disable()
                self.pattern_tab_button.enable()
                self.extras_tab_button.enable()

                self.general_tab.show()
                self.pattern_tab.hide()
                self.extras_tab.hide()
            elif event.ui_element == self.pattern_tab_button:
                self.general_tab_button.enable()
                self.pattern_tab_button.disable()
                self.extras_tab_button.enable()

                self.general_tab.hide()
                self.pattern_tab.show()
                self.extras_tab.hide()
            elif event.ui_element == self.extras_tab_button:
                self.general_tab_button.enable()
                self.pattern_tab_button.enable()
                self.extras_tab_button.disable()

                self.general_tab.hide()
                self.pattern_tab.hide()
                self.extras_tab.show()

    def screen_switches(self):
        update_sprite(scripts.global_vars.CREATED_CAT)

        self.back = custom_buttons.UIImageButton(pygame.Rect((50, 25), (105, 30)), "",
                                                 object_id="#back_button")

        self.done = custom_buttons.UIImageButton(pygame.Rect((673, 25), (77, 30)), "",
                                                 object_id="#done_button")

        self.randomize = custom_buttons.UIImageButton(pygame.Rect((630, 291), (50, 50)), "",
                                                      object_id="#random_dice_button")

        self.clear = custom_buttons.UIImageButton(pygame.Rect((690, 291), (50, 50)), "",
                                                  object_id="#clear_button")

        self.cat_image = pygame_gui.elements.UIImage(pygame.Rect((250, 25), (300, 300)),
                                                     pygame.transform.scale(scripts.global_vars.CREATED_CAT.sprite,
                                                                            (300, 300)))

        # Tabs

        #Tab background

        self.general_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 365), (100, 88)), "",
                                                               object_id="#general_tab_button")
        self.general_tab_button.disable()

        self.pattern_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 456), (100, 88)), "",
                                                               object_id="#pattern_tab_button")

        self.extras_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 547), (100, 88)), "",
                                                               object_id="#extra_tab_button")

        self.tab_background = pygame_gui.elements.UIImage(pygame.Rect((150, 350), (600, 300)),
                                                          load_image("resources/images/options.png"))

        self.general_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    scripts.global_vars.MANAGER)

        self.pattern_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    scripts.global_vars.MANAGER,
                                                                    visible=False)

        self.extras_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                   scripts.global_vars.MANAGER,
                                                                   visible=False)



        self.fur_length_select = pygame_gui.elements.UIDropDownMenu(["Short", "Long"], "Short",
                                                                    pygame.Rect((10, 10), (200, 40)),
                                                                    container=self.general_tab)

        #General Tab Contents
        self.pelt_select = pygame_gui.elements.UIDropDownMenu(self.pelt_options, "Plain",
                                                              pygame.Rect((10, 10), (300, 40)),
                                                              container=self.pattern_tab)

        #White Patches
        self.white_patches_select = pygame_gui.elements.UIDropDownMenu(self.white_patches, "None",
                                                                       pygame.Rect((10, 60), (300, 40)),
                                                                       container=self.pattern_tab)


    def open_basics_tab(self):
        pass

    def open_pattern_tab(self):
        pass

    def open_extras_tab(self):
        pass


