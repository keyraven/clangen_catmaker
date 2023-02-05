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
        self.dead = False
        self.df = False
        self.tortiebase = None
        self.pattern = None
        self.tortiepattern = None
        self.tortiecolour = None
        self.white_patches = None
        self.accessory = None
        self.age_sprites = {
            "kitten": 0,
            "adolescent": 3,
            "adult": 8,
            "elder": 3
        }
        self.opacity = 100
        self.reverse = False
        self.skin = "BLACK"

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
        util.init_pelt(self)
        util.init_tint(self)
        util.init_sprite(self)
        util.init_scars(self)
        util.init_accessories(self)
        util.init_white_patches(self)
        util.init_eyes(self)
        util.init_pattern(self)


# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
