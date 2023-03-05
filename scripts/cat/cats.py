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

    def generate_large_image(self):
        return

    def generate_save_file(self):
        """Generates a basic save file dictionary with all the looks-based info filled in. """
        pelt_name = self.pelt.name
        if pelt_name == "SingleColour" and self.white_patches:
            pelt_name = "TwoColour"
        if pelt_name == "Tortie" and self.white_patches:
            pelt_name = "Calico"

        save = {
            "ID": "1",
            "name_prefix": "Prefix",
            "name_suffix": "Suffix",
            "gender": "female",
            "gender_align": "female",
            "birth_cooldown": 0,
            "status": "warrior",
            "backstory": "clan_founder",
            "age": self.age,
            "moons": 30,
            "trait": "wise",
            "parent1": None,
            "parent2": None,
            "mentor": None,
            "former_mentor": [],
            "patrol_with_mentor": 0,
            "mentor_influence": [],
            "mate": None,
            "dead": False,
            "died_by": [],
            "paralyzed": False,
            "no_kits": False,
            "exiled": False,
            "pelt_name": pelt_name,
            "pelt_color": self.pelt.colour,
            "pelt_white": bool(self.white_patches),
            "pelt_length": self.pelt.length,
            "spirit_kitten": self.age_sprites["kitten"],
            "spirit_adolescent": self.age_sprites["adolescent"],
            "spirit_young_adult": self.age_sprites["adult"],
            "spirit_adult": self.age_sprites["adult"],
            "spirit_senior_adult": self.age_sprites["adult"],
            "spirit_elder": self.age_sprites["elder"],
            "spirit_dead": None,
            "eye_colour": self.eye_colour,
            "eye_colour2": self.eye_colour2,
            "reverse": self.reverse,
            "white_patches": self.white_patches,
            "white_patches_tint": self.white_patches_tint,
            "pattern": self.pattern if self.pelt.name == "Tortie" else None,
            "tortie_base": self.tortiebase if self.pelt.name == "Tortie" else None,
            "tortie_color": self.tortiecolour if self.pelt.name == "Tortie" else None,
            "tortie_pattern": self.tortiepattern if self.pelt.name == "Tortie" else None,
            "skin": self.skin,
            "tint": self.tint,
            "skill": "great hunter",
            "scars": [x for x in self.scar_slot_list if x],
            "accessory": self.accessory,
            "experience": 0,
            "dead_moons": 0,
            "current_apprentice": [],
            "former_apprentices": [],
            "possible_scar": None,
            "scar_event": [],
            "df": False,
            "outside": False,
            "corruption": 0,
            "life_givers": [],
            "known_life_givers": [],
            "virtues": [],
            "retired": False,
            "faded_offspring": [],
            "opacity": 100,
            "prevent_fading": False
        }

        return save

# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
