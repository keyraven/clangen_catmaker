from random import choice
from scripts.cat.sprites import Sprites
import random
from re import sub
from scripts.game_structure.game_essentials import game
import scripts.global_vars as global_vars


    

class Pelt():
    
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'Tabby': 'tabby',
        'Marbled': 'marbled',
        'Rosette': 'rosette',
        'Smoke': 'smoke',
        'Ticked': 'ticked',
        'Speckled': 'speckled',
        'Bengal': 'bengal',
        'Mackerel': 'mackerel',
        'Classic': 'classic',
        'Sokoke': 'sokoke',
        'Agouti': 'agouti',
        'Singlestripe': 'singlestripe',
        'Tortie': None,
        'Calico': None,
    }
    
    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    pelt_c_no_white = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    pelt_c_no_bw = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]

    tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'HALF',
                    'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE', 'CHIMERA', 'DAUB', 'EMBER', 'BLANKET',
                    'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'SMUDGED', 'DAPPLENIGHT', 'STREAK', 'MASK', 'CHEST', 'ARMTAIL']
    tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
                'classic', 'sokoke', 'agouti', 'singlestripe']

    pelt_length = ["short", "medium", "long"]
    eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
        'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER']
    yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'COPPER', 'GREENYELLOW', 'BRONZE', 'SILVER']
    blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'GREY']
    green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL']
    # scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
    # bite scars by @wood pank on discord
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
            "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
    scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
            "FROSTSOCK", ]

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                        "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                        "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                        ]
    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                        ]
    tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
    collars = [
        "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
        "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
        "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
        "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
        "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
        "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
        "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
        "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
        "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
    ]

    tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"]
    spotted = ["Speckled", "Rosette"]
    plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe"]
    exotic = ["Bengal", "Marbled"]
    torties = ["Tortie", "Calico"]
    pelt_categories = [tabbies, spotted, plain, exotic, torties]

    # SPRITE NAMES
    single_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    ginger_colours = ['CREAM', 'PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA']
    black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK']
    white_colours = ['WHITE', 'PALEGREY', 'SILVER']
    brown_colours = ['LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN', 'CHOCOLATE']
    colour_categories = [ginger_colours, black_colours, white_colours, brown_colours]
    eye_sprites = [
        'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
        'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
        'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER'
    ]
    little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                    'EXTRA']
    mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR', 'WINGS',
                'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER', 'WOODPECKER', 'MISS']
    high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
                'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
                'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'SHIBAINU', 'OWL']
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO','PEBBLESHINE', 'BOOTS', 'COW', 'COWTWO']
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER', 'BLEACHED']
    white_sprites = [
        little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

    skin_sprites = ['BLACK',  'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                    'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'RED']

    """Holds all appearence information for a cat. """
    def __init__(self,
                 name:str="SingleColour",
                 length:str="short",
                 colour:str="WHITE",
                 white_patches:str=None,
                 eye_color:str="BLUE",
                 eye_colour2:str=None,
                 tortiebase:str=None,
                 tortiecolour:str="GINGER",
                 pattern:str="ONE",
                 tortiepattern:str="single",
                 vitiligo:str=None,
                 points:str=None,
                 accessory:str=None,
                 paralyzed:bool=False,
                 opacity:int=100,
                 scars:list=None,
                 tint:str="none",
                 skin:str="BLACK",
                 white_patches_tint:str="none",
                 kitten_sprite:int=None,
                 adol_sprite:int=None,
                 adult_sprite:int=None,
                 senior_sprite:int=None,
                 para_adult_sprite:int=None,
                 reverse:bool=False,
                 ) -> None:
        self.name = name
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length=length
        self.points = points
        self.accessory = accessory
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scar_slot_list = [
            None,
            None,
            None,
            None
        ]
        self.tint = tint
        self.white_patches_tint = white_patches_tint
        self.cat_sprites =  {
            "kitten": kitten_sprite if kitten_sprite is not None else 0,
            "adolescent": adol_sprite if adol_sprite is not None else 3,
            "young adult": adult_sprite if adult_sprite is not None else 8,
            "adult": adult_sprite if adult_sprite is not None else 8,
            "senior adult": adult_sprite if adult_sprite is not None else 8,
            "senior": senior_sprite if senior_sprite is not None else 12,
        }        
        self.cat_sprites['newborn'] = 20
        self.cat_sprites['para_young'] = 17
        self.cat_sprites["sick_adult"] = 18
        self.cat_sprites["sick_young"] = 19
        
        
        self.current_poses = {
            "newborn": "1",
            "kitten": "1",
            "adolescent": "1",
            "adult": "3",
            "senior": "1",
        }
        self.not_working = False
        self.stored_eye_color_2 = "BLUE"
        
        self.reverse = reverse
        self.skin = skin

    def randomize_pelt(self):
        
        self.init_pattern_color()
        self.init_white_patches()
        self.init_pose()
        self.init_scars()
        self.init_accessories()
        self.init_eyes()
        self.init_pattern()
        self.init_tint()
        
        self.paralyzed = choice([True, False])
        self.not_working = choice([True, False])
    
    #-------------------------------------------------------------------------------------------------#
    #                               Setter Functions                                                  #
    #-------------------------------------------------------------------------------------------------#
    
    def set_pose(self, age, pose):
        """Sets the pose, updating cat_sprites """
        if not pose:
            return
           
        if age in ["young adult", "adult", "senior adult"]:
            for inter_age in ["young adult", "adult", "senior adult"]:
                self.cat_sprites[inter_age] = global_vars.poses[
                self.length]["adult"][pose]

                # Adjust tracked poses.
            self.current_poses["adult"] = pose
        else:
            # Change the sprite number.
            self.cat_sprites[age] = global_vars.poses[
                self.length][age][pose]

            # Adjust tracked poses.
            self.current_poses[age] = pose
    
    def set_pelt_length(self, fur_length):
        if fur_length not in ["short", "long"]:
            return
        
        self.length = fur_length

        # Update the sprite numbers:
        for age in self.current_poses:
            self.set_pose(age, self.current_poses[age])

    #-------------------------------------------------------------------------------------------------#
    #                               Randomize Functions                                                  #
    #-------------------------------------------------------------------------------------------------#

    def init_eyes(self):
        
        self.eye_colour = choice(list(global_vars.eye_colors.keys()))
        
        if not random.randint(0, 4):
            self.eye_colour2 = choice(list(global_vars.eye_colors.keys()))
        else:
            self.eye_colour2 = None


    def init_pattern_color(self) -> bool:
        """Inits self.name, self.colour, self.length, 
            self.tortiebase """
        
        self.name = random.choice(list(global_vars.pelt_options.keys()) + ["Tortie"])
        self.tortiebase = random.choice(list(global_vars.tortie_patches_patterns.keys()))
        self.colour = random.choice(list(global_vars.colors.keys()))
        self.length = random.choice(["short", "long"])
        self.skin = choice(list(global_vars.skin_colors.keys()))
        
    def init_pose(self):

        poses = ["1", "2", "3"]
        for age in self.current_poses:
            self.set_pose(age, random.choice(poses))
        
        self.reverse = choice([True, False])

    def init_scars(self):
        self.scar_slot_list = [
            None,
            None,
            None,
            None
        ]
        
        for i in range(0, len(self.scar_slot_list)):
            if random.randint(0, 1):
                self.scar_slot_list[i] = random.choice(list(global_vars.scars.keys()))
        
    def init_accessories(self):
        
        self.accessory = random.choice(list(global_vars.accessories.keys()))

    def init_pattern(self):
        
        self.pattern = random.choice(list(global_vars.tortie_patches_shapes.keys()))
        self.tortiecolour = random.choice(list(global_vars.colors.keys()))
        self.tortiepattern = random.choice(list(global_vars.tortie_patches_patterns.keys()))

    def init_white_patches(self):
         
        self.white_patches = choice(list(global_vars.white_patches.keys()))
        
        if random.random() > 0.5:
            self.points = choice(list(global_vars.points.keys()))
        else:
            self.points = None
        
        if random.random() > 0.9:
            self.vitiligo = choice(list(global_vars.vit.keys()))
        else:
            self.vitiligo = None
        
        
    def init_tint(self):
        """Sets tint for pelt and white patches"""

        self.tint = choice(list(global_vars.tints.keys()))
        self.white_patches_tint = choice(list(global_vars.white_patches_tint.keys()))

    @property
    def white(self):
        return self.white_patches or self.points
    
    @white.setter
    def white(self, val):
        print("Can't set pelt.white")
        return    

    @staticmethod
    def describe_appearance(cat, short=False):
        
        # Define look-up dictionaries
        if short:
            renamed_colors = {
                "white": "pale",
                "palegrey": "gray",
                "darkgrey": "gray",
                "grey": "gray",
                "paleginger": "ginger",
                "darkginger": "ginger",
                "sienna": "ginger",
                "lightbrown": "brown",
                "lilac": "brown",
                "golden-brown": "brown",
                "darkbrown": "brown",
                "chocolate": "brown",
                "ghost": "black"
            }
        else:
            renamed_colors = {
                "white": "pale",
                "palegrey": "pale gray",
                "grey": "gray",
                "darkgrey": "dark gray",
                "paleginger": "pale ginger",
                "darkginger": "dark ginger",
                "sienna": "dark ginger",
                "lightbrown": "light brown",
                "lilac": "light brown",
                "golden-brown": "golden brown",
                "darkbrown": "dark brown",
                "chocolate": "dark brown",
                "ghost": "black"
            }

        pattern_des = {
            "Tabby": "c_n tabby",
            "Speckled": "speckled c_n",
            "Bengal": "unusually dappled c_n",
            "Marbled": "c_n tabby",
            "Ticked": "c_n ticked",
            "Smoke": "c_n smoke",
            "Mackerel": "c_n tabby",
            "Classic": "c_n tabby",
            "Agouti": "c_n tabby",
            "Singlestripe": "dorsal-striped c_n",
            "Rosette": "unusually spotted c_n",
            "Sokoke": "c_n tabby"
        }

        # Start with determining the base color name. 
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]
        
        # Replace "white" with "pale" if the cat is 
        if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
            color_name = "pale"

        # Time to descibe the pattern and any additional colors. 
        if cat.pelt.name in pattern_des:
            color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
        elif cat.pelt.name in Pelt.torties:
            # Calicos and Torties need their own desciptions. 
            if short:
                # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                    color_name = "mottled"
                else:
                    color_name = cat.pelt.name.lower()
            else:
                base = cat.pelt.tortiebase.lower()
                if base in Pelt.tabbies + ['bengal', 'rosette', 'speckled']:
                    base = 'tabby'
                else:
                    base = ''

                patches_color = cat.pelt.tortiecolour.lower()
                if patches_color in renamed_colors:
                    patches_color = renamed_colors[patches_color]
                color_name = f"{color_name}/{patches_color}"
                
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                        color_name = f"{color_name} mottled"
                else:
                    color_name = f"{color_name} {cat.pelt.name.lower()}"

        if cat.pelt.white_patches:
            if cat.pelt.white_patches == "FULLWHITE":
                # If the cat is fullwhite, discard all other information. They are just white. 
                color_name = "white"
            if cat.pelt.white_patches in Pelt.mostly_white and cat.pelt.name != "Calico":
                color_name = f"white and {color_name}"
            elif cat.pelt.name != "Calico":
                color_name = f"{color_name} and white"
        
        if cat.pelt.points:
            color_name = f"{color_name} point"
            if "ginger point" in color_name:
                color_name.replace("ginger point", "flame point")

        if "white and white" in color_name:
            color_name = color_name.replace("white and white", "white")

        # Now it's time for gender
        if cat.genderalign in ["female", "trans female"]:
            color_name = f"{color_name} she-cat"
        elif cat.genderalign in ["male", "trans male"]:
            color_name = f"{color_name} tom"
        else:
            color_name = f"{color_name} cat"

        # Here is the place where we can add some additional details about the cat, for the full non-short one. 
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
        if not short:
            
            scar_details = {
                "NOTAIL": "no tail", 
                "HALFTAIL": "half a tail", 
                "NOPAW": "three legs", 
                "NOLEFTEAR": "a missing ear", 
                "NORIGHTEAR": "a missing ear",
                "NOEAR": "no ears"
            }

            additional_details = []
            if cat.pelt.vitiligo:
                additional_details.append("vitiligo")
            for scar in cat.pelt.scars:
                if scar in scar_details and scar_details[scar] not in additional_details:
                    additional_details.append(scar_details[scar])
            
            if len(additional_details) > 1:
                color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
            elif additional_details:
                color_name = f"{color_name} with {additional_details[0]}"
        
        
            if len(cat.pelt.scars) >= 3:
                color_name = f"scarred {color_name}"
            if cat.pelt.length == "long":
                color_name = f"long-furred {color_name}"

        return color_name
    
    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
