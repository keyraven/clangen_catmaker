import scripts.screens.base_screens as base_screens
import pygame_gui
import pygame
import scripts.global_vars as global_vars
from scripts.utility import update_sprite
from scripts.game_structure.image_cache import load_image
import scripts.game_structure.image_button as custom_buttons
from scripts.cat.cats import Cat
from scripts.cat.pelts import choose_pelt

class CreationScreen(base_screens.Screens):

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
        self.pose_select = None
        self.base_pelt_select = None
        self.dropdown_menus = {}

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
                self.build_dropdown_menus()
                self.update_cat_image()
            elif event.ui_element == self.randomize:
                global_vars.CREATED_CAT.randomize_looks()
                self.build_dropdown_menus()
                self.update_cat_image()
        elif event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.dropdown_menus["color_select"]:
                global_vars.CREATED_CAT.pelt.colour = global_vars.colors.inverse[event.text]
                print(global_vars.CREATED_CAT.pelt.colour)
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["white_patches_select"]:
                global_vars.CREATED_CAT.white_patches = global_vars.white_patches.inverse[event.text]
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pelt_length_select"]:
                self.change_fur_length(event.text.lower())
                self.update_cat_image()
            elif event.ui_element == self.dropdown_menus["pose_select"]:
                self.change_pose(event.text[-1])
                self.update_cat_image()
            elif event.ui_element == self.base_pelt_select:
                if event.text == "Plain":
                    selected = 'SingleColour'
                else:
                    selected = event.text

                global_vars.CREATED_CAT.pelt = choose_pelt(
                    global_vars.CREATED_CAT.pelt.colour,
                    False,
                    selected,
                    global_vars.CREATED_CAT.pelt.length
                )
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

        self.build_dropdown_menus()


    def update_cat_image(self):
        update_sprite(global_vars.CREATED_CAT)
        self.cat_image.set_image(pygame.transform.scale(global_vars.CREATED_CAT.sprite, (300, 300)))

    def build_dropdown_menus(self):
        for ele in self.dropdown_menus:
            self.dropdown_menus[ele].kill()
        self.dropdown_menus = {}

        # GENERAL TAB CONTENTS
        self.dropdown_menus["pelt_length_select"] = pygame_gui.elements.UIDropDownMenu(["Short", "Long"],
                                                                                       global_vars.CREATED_CAT.pelt.length.capitalize(),
                                                                                       pygame.Rect((10, 10), (200, 40)),
                                                                                       container=self.general_tab)

        self.dropdown_menus["pose_select"] = pygame_gui.elements.UIDropDownMenu(["Pose 1", "Pose 2", "Pose 3"],
                                                                                 "Pose " +
                                                                                 global_vars.CREATED_CAT.current_poses[
                                                                                 global_vars.CREATED_CAT.age
                                                                                 ],
                                                                                 pygame.Rect((10, 50), (200, 40)),
                                                                                 container=self.general_tab)

        # PATTERN TAB CONTENTS
        self.dropdown_menus["color_select"] = pygame_gui.elements.UIDropDownMenu(global_vars.colors.values(),
                                                                                 global_vars.colors[
                                                                                 global_vars.CREATED_CAT.pelt.colour],
                                                                                 pygame.Rect((10, 10), (200, 40)),
                                                                                 container=self.pattern_tab)


        current_base_pelt = global_vars.CREATED_CAT.pelt.name
        if current_base_pelt in ["Tortie", "Calcio"]:
            current_base_pelt = global_vars.CREATED_CAT.tortiebase.capitalize()
            if current_base_pelt == "Single":
                current_base_pelt = "SingleColour"

        self.dropdown_menus["pelt_select"] = pygame_gui.elements.UIDropDownMenu(global_vars.pelt_options.values(),
                                                                                global_vars.pelt_options[
                                                                                    current_base_pelt
                                                                                ],
                                                                                pygame.Rect((220, 10), (200, 40)),
                                                                                container=self.pattern_tab)

        if global_vars.CREATED_CAT.white_patches:
            white_patches = (global_vars.CREATED_CAT.white_patches.lower()).capitalize()
        else:
            white_patches = "None"
        self.dropdown_menus["white_patches_select"] = pygame_gui.elements.UIDropDownMenu(global_vars.white_patches.values(),
                                                                                         global_vars.white_patches[
                                                                                         global_vars.CREATED_CAT.white_patches
                                                                                         ],
                                                                                         pygame.Rect((10, 60), (200, 40)),
                                                                                         container=self.pattern_tab)

    def change_pose(self, pose: str=None):
        # Changes the pose from 1, 2, or 3
        if pose:
            # Change the sprite number.
            global_vars.CREATED_CAT.age_sprites[global_vars.CREATED_CAT.age] = self.poses[
                global_vars.CREATED_CAT.pelt.length][global_vars.CREATED_CAT.age][pose]

            # Adjust tracked poses.
            global_vars.CREATED_CAT.current_poses[global_vars.CREATED_CAT.age] = pose


    def change_fur_length(self, fur_length: str=None):
        if fur_length:
            global_vars.CREATED_CAT.pelt.length = fur_length

            # Change all poses for all ages. 
            for age in global_vars.CREATED_CAT.current_poses:
                # This is such a mess of dictionary lookups.
                global_vars.CREATED_CAT.age_sprites[age] = self.poses[
                    fur_length][age][global_vars.CREATED_CAT.current_poses[age]]



    def open_extras_tab(self):
        pass


