import scripts.global_vars as global_vars
from tkinter import filedialog
import pygame
from pygame_gui.elements import UIWindow
from scripts.game_structure.image_button import UIImageButton
from scripts.game_structure.game_essentials import game
import pygame_gui


class SaveAsImage(UIWindow):
    def __init__(self, image_to_save, file_name):
        super().__init__(pygame.Rect((200, 175), (400, 250)),
                         resizable=False, object_id="#window_base_theme")
        
        self.set_blocking(True)
        #game.switches['window_open'] = True
        
        self.image_to_save = image_to_save
        self.file_name = file_name
        self.scale_factor = 1
        
        button_layout_rect = pygame.Rect((0, 5), (22, 22))
        button_layout_rect.topright = (-2, 10)
        
        self.close_button = UIImageButton(
            button_layout_rect,
            "",
            object_id="#exit_window_button",
            starting_height=2,
            container=self,
            anchors={'right': 'right',
                     'top': 'top'}
        )
        
        self.save_as_image = UIImageButton(
            pygame.Rect((0, 90), (135, 30)),
            "",
            object_id="#save_image_button",
            starting_height=2,
            container=self,
            anchors={'centerx': 'centerx'}
        )
        
        self.small_size_button = UIImageButton(
            pygame.Rect((55, 50), (97, 30)),
            "",
            object_id="#image_small_button",
            container=self,
            starting_height=2
        )
        self.small_size_button.disable()
        
        self.medium_size_button = UIImageButton(
            pygame.Rect((151, 50), (97, 30)),
            "",
            object_id="#image_medium_button",
            container=self,
            starting_height=2
        )
        
        self.large_size_button = UIImageButton(
            pygame.Rect((248, 50), (97, 30)),
            "",
            object_id="#image_large_button",
            container=self,
            starting_height=2
        )
        
        self.confirm_text = pygame_gui.elements.UITextBox(
            "",
            pygame.Rect((5, 125), (390, 45)),
            object_id="#text_box_26_horizcenter_vertcenter_spacing_95",
            container=self,
            starting_height=2
        )
        
    def save_image(self):
        file_name = self.file_name
        file_number = ""
        i = 0
        
        folder_path = filedialog.asksaveasfilename()
        print(folder_path)
        
        scaled_image = pygame.transform.scale_by(self.image_to_save, self.scale_factor)
        pygame.image.save(scaled_image, f"{folder_path}")
        return f"{file_name + file_number}.png"
        
    def process_event(self, event) -> bool:
        super().process_event(event)
        
        if event.type == pygame_gui.UI_BUTTON_START_PRESS:
            if event.ui_element == self.save_as_image:
                file_name = self.save_image()
                self.confirm_text.set_text(f"Saved as {file_name} in the saved_images folder")
            elif event.ui_element == self.small_size_button:
                self.scale_factor = 1
                self.small_size_button.disable()
                self.medium_size_button.enable()
                self.large_size_button.enable()
            elif event.ui_element == self.medium_size_button:
                self.scale_factor = 4
                self.small_size_button.enable()
                self.medium_size_button.disable()
                self.large_size_button.enable()
            elif event.ui_element == self.large_size_button:
                self.scale_factor = 6
                self.small_size_button.enable()
                self.medium_size_button.enable()
                self.large_size_button.disable()