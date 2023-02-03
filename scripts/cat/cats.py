from __future__ import annotations
from random import choice, randint, sample
from typing import Dict, List, Any
import math
import os.path

from .pelts import *
from .names import *
from .sprites import *

from scripts.utility import *
from scripts.game_structure.game_essentials import *



class Cat():

    def __init__(self,
                 prefix=None,
                 gender=None,
                 age="adult",
                 parent1=None,
                 parent2=None,
                 pelt=None,
                 eye_colour=None,
                 suffix=None,
                 moons=None,
                 ):

        # Private attributes
        self._moons = None
        
        # Public attributes

        self.age = age
        self.pelt = pelt
        self.tint = None
        self.eye_colour = eye_colour
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
            "kitten": None,
            "adolescent": None,
            "young adult": None,
            "adult": None,
            "senior adult": None,
            "elder": None
        }
        self.opacity = 100

        self.gender = gender
        self.skill = None
        self.trait = None
        self.parent1 = parent1
        self.parent2 = parent2

        # Sprite sizes
        self.sprite = None
        self.big_sprite = None
        self.large_sprite = None

    def randomize_looks(self):
        pass

# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
