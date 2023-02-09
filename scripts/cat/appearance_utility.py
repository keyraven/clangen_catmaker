import random
from .pelts import *
from scripts.cat.sprites import Sprites
import scripts.global_vars as global_vars

# ---------------------------------------------------------------------------- #
#                                init functions                                #
# ---------------------------------------------------------------------------- #


def randomize_eyes(cat):
    cat.eye_colour2 = None

    cat.eye_colour = choice(list(global_vars.eye_colors.keys()))

    cat.eye_colour2 = None
    hit = randint(0, 6)
    if hit == 0:
        cat.eye_colour2 = choice(list(global_vars.eye_colors.keys()))

def randomize_pelt(cat):
    # ------------------------------------------------------------------------------------------------------------#
    #   PELT
    # ------------------------------------------------------------------------------------------------------------#

    # Determine pelt.
    chosen_pelt = choice(list(global_vars.pelt_options.keys()))

    # Tortie chance
    torbie = random.getrandbits(2) == 1

    chosen_tortie_base = None
    if torbie:
        # If it is tortie, the chosen pelt above becomes the base pelt.
        chosen_tortie_base = chosen_pelt
        if chosen_tortie_base in ["SingleColour"]:
            chosen_tortie_base = "Single"
        chosen_tortie_base = chosen_tortie_base.lower()
        chosen_pelt = "Tortie"

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT COLOUR
    # ------------------------------------------------------------------------------------------------------------#

    chosen_pelt_color = choice(list(global_vars.colors.keys()))

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT LENGTH
    # ------------------------------------------------------------------------------------------------------------#

    chosen_pelt_length = random.choice(["long", "short"])

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT WHITE
    # ------------------------------------------------------------------------------------------------------------#

    chosen_white = random.randint(1, 100) <= 40

    # Adjustments to pelt chosen based on if the pelt has white in it or not.

    cat.pelt = choose_pelt(chosen_pelt_color, chosen_white, chosen_pelt, chosen_pelt_length)
    cat.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.


def randomize_sprite(cat):
    cat.age_sprites = {
        'kitten': randint(0, 2),
        'adolescent': randint(3, 5),
        'elder': randint(3, 5)
    }
    cat.reverse = choice([True, False])

    # skin chances
    cat.skin = choice(list(global_vars.skin_colors.keys()))
            
    if cat.pelt is not None:
        if cat.pelt.length != 'long':
            cat.age_sprites['adult'] = randint(6, 8)
        else:
            cat.age_sprites['adult'] = randint(0, 2)


def randomize_platform(cat):
    cat.platform = choice(list(global_vars.platforms.keys()))

def randomize_scars(cat):

    cat.scar_slot_list = [
        None,
        None,
        None,
        None,
    ]

    scar_number = random.choices([0,1,2,3,4], weights=[50, 20, 15, 10, 5], k=1)[0]

    i = 0
    all_scars = list(global_vars.scars.keys())
    while True:
        if i >= scar_number:
            break
        if all_scars:
            add_scar = choice(all_scars)
            cat.scar_slot_list[i] = add_scar
            all_scars.remove(add_scar)
        i += 1

    if 'NOTAIL' in cat.scars and 'HALFTAIL' in cat.scars:
        for ele in range(len(cat.scar_slot_list)):
            if cat.scar_slot_list[ele] == 'HALFTAIL':
                cat.scar_slot_list[ele] = None


def randomize_accessories(cat):
    acc_display_choice = randint(0, 2)
    if acc_display_choice == 1:
        cat.accessory = choice(list(global_vars.accessories.keys()))
    else:
        cat.accessory = None


def randomize_pattern(cat):

    if cat.pelt.name in torties:
        cat.tortiecolour = cat.pelt.colour

        cat.tortie_patches_pattern = choice(list(global_vars.tortie_patches_patterns.keys()))
        cat.tortiepattern = "tortie" + cat.tortie_patches_pattern

        cat.tortie_patches_shape = choice(list(global_vars.tortie_patches_shapes.keys()))
        cat.tortie_patches_color = choice(list(global_vars.tortie_patches_color.keys()))
        cat.pattern = cat.tortie_patches_color + cat.tortie_patches_shape

def randomize_white_patches(cat):

    chosen_white_patches = choice(list(global_vars.white_patches.keys()))
    cat.white_patches = chosen_white_patches

def randomize_tint(cat):
    # Basic tints as possible for all colors.
    cat.tint = choice(list(global_vars.tints.keys()))

