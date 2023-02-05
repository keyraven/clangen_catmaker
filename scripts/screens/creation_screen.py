import scripts.screens.base_screens as base_screens
import pygame_gui
import pygame
import scripts.global_vars as global_vars
from scripts.utility import update_sprite
from scripts.game_structure.image_cache import load_image
import scripts.game_structure.image_button as custom_buttons
from scripts.cat.cats import Cat

class CreationScreen(base_screens.Screens):
    pelt_options = ["Plain", "Smoke", "Single Stripe", "Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti",
                    "Speckled", "Rosette", "Bengal", "Marbled"]
    tortie_patches_patterns = ["Tabby", ]
    colors = ['White', 'Grey', 'Dark Grey', 'Pale Grey', 'Silver', 'Golden', 'Ginger', 'Dark Ginger',
              'Pale Ginger', 'Cream', 'Brown', 'Dark Brown', 'Light Brown', 'Black', 'Ghost']
    white_patches = ['None', 'Little', 'Little Creamy', 'Tuxedo', 'Light Tuxedo', 'Tuxedo Creamy', 'Buzzardfang',
                     'Tip', 'Blaze', 'Bib', 'Vee', 'Paws', 'Belly', 'Tail Tip', 'Toes', 'Broken Blaze', 'Lil Two',
                     'Scourge', 'Toes Tail', 'Ravenpaw', 'Honey', 'Fancy', 'Unders', 'Damien', 'Skunk', 'Mitaine',
                     'Squeaks', 'Star', 'Any', 'Any Creamy', 'Any 2', 'Any 2 Creamy', 'Broken', 'Freckles', 'Ringtail',
                     'Half Face', 'Pants 2', 'Goatee', 'Prince', 'Farofa', 'Mister', 'Pants', 'Reverse Pants',
                     'Half White', 'Appaloosa', 'Piebald', 'Curved', 'Glass', 'Mask Mantle', 'Van', 'Van Creamy',
                     'One Ear', 'Lightsong', 'Tail', 'Heart', 'Moorish', 'Apron', 'Cap Saddle', 'Colorpoint',
                     'Colorpoint Creamy', 'Ragdoll', 'Karpati', 'Sepiapoint', 'Minkpoint', 'Sealpoint', 'Full White',
                     'Vitiligo', 'Vitiligo 2']
    tints = ["None", "Blue", "Pink"]
    scars = ["None"]

    poses = {
        "short" : {
            "kitten": {
                "1" : 0,
                "2" : 1,
                "3" : 2
            },
            "adolescent": {
                "1" : 3,
                "2" : 4,
                "3" : 5
            },
            "adult": {
                "1" : 6,
                "2" : 7,
                "3" : 8
            },
            "elder": {
                "1": 3,
                "2": 4,
                "3": 5
            }
        },
        "long": {
            "kitten": {
                "1": 0,
                "2": 1,
                "3": 2
            },
            "adolescent": {
                "1": 3,
                "2": 4,
                "3": 5
            },
            "adult": {
                "1": 0,
                "2": 1,
                "3": 2
            },
            "elder": {
                "1": 3,
                "2": 4,
                "3": 5
            }
        }
    }

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
        self.fur_length_select = None
        self.general_tab_button = None
        self.pattern_tab_button = None
        self.extras_tab_button = None
        self.color_select = None
        self.white_patches_select = None

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
            elif event.ui_element == self.clear:
                global_vars.CREATED_CAT = Cat()
                self.update_cat_image()
        elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.color_select:
                global_vars.CREATED_CAT.pelt.colour = (event.text.upper()).replace(" ", "")
                self.update_cat_image()
            elif event.ui_element == self.white_patches_select:
                if event.text == "None":
                    global_vars.CREATED_CAT.white_patches = None
                else:
                    val = (event.text.upper()).replace(" ", "")
                    val = val.replace("COLOR", "COLOUR")
                    global_vars.CREATED_CAT.white_patches = val
                self.update_cat_image()

    def screen_switches(self):
        update_sprite(global_vars.CREATED_CAT)

        self.back = custom_buttons.UIImageButton(pygame.Rect((50, 25), (105, 30)), "",
                                                 object_id="#back_button")

        self.done = custom_buttons.UIImageButton(pygame.Rect((673, 25), (77, 30)), "",
                                                 object_id="#done_button")

        self.randomize = custom_buttons.UIImageButton(pygame.Rect((630, 291), (50, 50)), "",
                                                      object_id="#random_dice_button")

        self.clear = custom_buttons.UIImageButton(pygame.Rect((690, 291), (50, 50)), "",
                                                  object_id="#clear_button")

        self.cat_image = pygame_gui.elements.UIImage(pygame.Rect((250, 25), (300, 300)),
                                                     pygame.transform.scale(global_vars.CREATED_CAT.sprite,
                                                                            (300, 300)))

        # Tabs
        self.general_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 365), (100, 88)), "",
                                                               object_id="#general_tab_button")
        self.general_tab_button.disable()

        self.pattern_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 456), (100, 88)), "",
                                                               object_id="#pattern_tab_button")

        self.extras_tab_button = custom_buttons.UIImageButton(pygame.Rect((50, 547), (100, 88)), "",
                                                               object_id="#extra_tab_button")

        self.tab_background = pygame_gui.elements.UIImage(pygame.Rect((150, 350), (600, 300)),
                                                          load_image("resources/images/options.png"))

        # TAB CONTAINERS
        self.general_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER)

        self.pattern_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                    global_vars.MANAGER,
                                                                    visible=False)

        self.extras_tab = pygame_gui.elements.UIScrollingContainer(pygame.Rect((150, 350), (600, 300)),
                                                                   global_vars.MANAGER,
                                                                   visible=False)

        # GENERAL TAB CONTENTS
        self.fur_length_select = pygame_gui.elements.UIDropDownMenu(["Short", "Long"], "Short",
                                                                    pygame.Rect((10, 10), (200, 40)),
                                                                    container=self.general_tab)

        # PATTERN TAB CONTENTS
        self.color_select = pygame_gui.elements.UIDropDownMenu(self.colors, self.colors[0],
                                                               pygame.Rect((10, 10), (300, 40)),
                                                               container=self.pattern_tab)

        #White Patches
        self.white_patches_select = pygame_gui.elements.UIDropDownMenu(self.white_patches, self.white_patches[0],
                                                                       pygame.Rect((10, 60), (300, 40)),
                                                                       container=self.pattern_tab)

    def update_cat_image(self):
        update_sprite(global_vars.CREATED_CAT)
        self.cat_image.set_image(pygame.transform.scale(global_vars.CREATED_CAT.sprite, (300, 300)))

    def change_pose(self, pose: str=None):
        # Changes the pose from 1, 2, or 3
        if pose:
            global_vars.CREATED_CAT.age_sprites[global_vars.CREATED_CAT.age] = self.poses[
                global_vars.CREATED_CAT.pelt.length][global_vars.CREATED_CAT.age][pose]


    def change_fur_length(self, fur_length: str=None):
        if fur_length:
            global_vars.CREATED_CAT.pelt.length = fur_length

            # Change all poses for all ages. 
            for age in global_vars.CREATED_CAT.age_sprites:
                global_vars.CREATED_CAT.age_sprites[age] = self.p



    def open_extras_tab(self):
        pass


