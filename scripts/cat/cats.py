from __future__ import annotations
from random import choice, randint, sample
import os.path

import scripts.cat.appearance_utility as util
from scripts.utility import *
from scripts.game_structure.game_essentials import *



class Cat():

    def __init__(self):

        # Private attributes
        self._moons = 0
        
        # Public attributes

        self.age = "adult"
        self.pelt = SingleColour("WHITE", "short")
        self.tint = "none"
        self.eye_colour = "BLUE"
        self.eye_colour2 = None
        self.scars = []
        self.scar_slot_list = [
            None,
            None,
            None,
            None
        ]
        self.dead = False
        self.df = False
        self.tortiebase = "single"
        self.pattern = "ONE"
        self.tortiepattern = "single"
        self.tortiecolour = "GINGER"
        self.white_patches = None
        self.white_patches_tint = "none"
        self.accessory = None
        self.shading = False
        self.age_sprites = {
            "kitten": 0,
            "adolescent": 3,
            "adult": 8,
            "elder": 3
        }
        self.current_poses = {
            "kitten": "1",
            "adolescent": "1",
            "adult": "3",
            "elder": "1"
        }
        self.platform = "None"

        # Helpers:
        self.stored_eye_color_2 = "BLUE"

        self.opacity = 100
        self.reverse = False
        self.skin = "BLACK"

        # Unused
        self.gender = "female"
        self.skill = None
        self.trait = None
        self.parent1 = None
        self.parent2 = None

        # Sprite sizes
        self.sprite = None
        self.big_sprite = None
        self.large_sprite = None

    def randomize_looks(self):
        self.age = choice(list(self.age_sprites.keys()))
        util.randomize_pelt(self)
        util.randomize_eyes(self)
        util.randomize_sprite(self)
        util.randomize_scars(self)
        util.randomize_accessories(self)
        util.randomize_white_patches(self)
        util.randomize_pattern(self)
        util.randomize_platform(self)
        util.randomize_tint(self)

        lineart = choice(["Star", "Normal", "DF"])
        if lineart == "Star":
            self.dead = True
            self.df = False
        elif lineart == "Normal":
            self.dead = False
            self.df = False
        elif lineart == "DF":
            self.dead = True
            self.df = True

        self.shading = choice([True, False])





# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
