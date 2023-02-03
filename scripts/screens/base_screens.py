import scripts.global_vars
import pygame
from scripts.game_structure.game_essentials import *

class Screens():
    last_screen = ''

    def change_screen(self, new_screen):
        """Use this function when switching screens.
            It will handle keeping track of the last screen and cur screen.
            Last screen must be tracked to ensure a clear transition between screens."""
        # self.exit_screen()
        game.last_screen_forupdate = self.name

        # This keeps track of the last list-like screen for the back button on cat profiles
        if self.name in ['clan screen', 'list screen', 'starclan screen', 'dark forest screen', 'events screen',
                         'med den screen']:
            game.last_screen_forProfile = self.name

        game.switches['cur_screen'] = new_screen
        game.switch_screens = True

    def __init__(self, name=None):
        self.name = name
        if name is not None:
            game.all_screens[name] = self

    def fill(self, tup):
        pygame.Surface.fill(color=tup)

    def on_use(self):
        """Runs every frame this screen is used."""
        pass

    def screen_switches(self):
        """Runs when this screen is switched to."""
        pass

    def handle_event(self, event):
        """This is where events that occur on this page are handled.
        For the pygame_gui rewrite, button presses are also handled here. """
        pass

    def exit_screen(self):
        """Runs when screen exits"""
        pass
