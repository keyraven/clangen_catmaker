import pygame
from scripts.game_structure import image_cache

from scripts.cat.sprites import *
from scripts.cat.pelts import *
from scripts.game_structure.game_essentials import *
import traceback

def update_sprite(cat):
    # First, check if the cat is faded.
    cat.scars = []
    for scar in cat.scar_slot_list:
        if scar:
            cat.scars.append(scar)


     # setting the cat_sprite (bc this makes things much easier)
    if cat.paralyzed and not cat.not_working:
        if cat.age in ['newborn', 'kitten', 'adolescent']:
            cat_sprite = str(17)
        else:
            if cat.pelt.length == 'long':
                cat_sprite = str(16)
            else:
                cat_sprite = str(15)
    elif cat.not_working:
        if cat.age in ['newborn', 'kitten', 'adolescent']:
            cat_sprite = str(19)
        else:
            cat_sprite = str(18)
    else:
        cat_sprite = str(cat.cat_sprites[cat.age])

# generating the sprite
    try:
        new_sprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

        if cat.pelt.name not in ['Tortie', 'Calico']:
            new_sprite.blit(sprites.sprites[cat.pelt.sprites[1] + cat.pelt.colour + cat_sprite], (0, 0))
        else:
                # Base Coat
                new_sprite.blit(
                    sprites.sprites[cat.tortiebase + cat.pelt.colour + cat_sprite],
                    (0, 0))

                # Create the patch image
                if cat.tortiepattern == "Single":
                    tortie_pattern = "SingleColour"
                else:
                    tortie_pattern = cat.tortiepattern

                patches = sprites.sprites[
                    tortie_pattern + cat.tortiecolour + cat_sprite].copy()
                patches.blit(sprites.sprites["tortiemask" + cat.pattern + cat_sprite], (0, 0),
                             special_flags=pygame.BLEND_RGBA_MULT)

                # Add patches onto cat.
                new_sprite.blit(patches, (0, 0))

        # TINTS
        if cat.tint != "none" and cat.tint in Sprites.cat_tints["tint_colours"]:
            # Multiply with alpha does not work as you would expect - it just lowers the alpha of the
            # entire surface. To get around this, we first blit the tint onto a white background to dull it,
            # then blit the surface onto the sprite with pygame.BLEND_RGB_MULT
            tint = pygame.Surface((50, 50)).convert_alpha()
            tint.fill(tuple(Sprites.cat_tints["tint_colours"][cat.tint]))
            new_sprite.blit(tint, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

        # draw white patches
        if cat.white_patches is not None:
            white_patches = sprites.sprites['white' + cat.white_patches + cat_sprite].copy()

            # Apply tint to white patches.
            if cat.white_patches_tint != "none" and cat.white_patches_tint in Sprites.white_patches_tints[
                "tint_colours"]:
                tint = pygame.Surface((50, 50)).convert_alpha()
                tint.fill(tuple(Sprites.white_patches_tints["tint_colours"][cat.white_patches_tint]))
                white_patches.blit(tint, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

            new_sprite.blit(white_patches, (0, 0))

        # draw vit & points

        if cat.points:
            points = sprites.sprites['white' + cat.points + cat_sprite].copy()
            if cat.white_patches_tint != "none" and cat.white_patches_tint in Sprites.white_patches_tints[
                 "tint_colours"]:
                tint = pygame.Surface((50, 50)).convert_alpha()
                tint.fill(tuple(Sprites.white_patches_tints["tint_colours"][cat.white_patches_tint]))
                points.blit(tint, (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            new_sprite.blit(points, (0, 0))


        if cat.vitiligo:
            new_sprite.blit(sprites.sprites['white' + cat.vitiligo + cat_sprite], (0, 0))

        # draw eyes & scars1
        new_sprite.blit(sprites.sprites['eyes' + cat.eye_colour + cat_sprite], (0, 0))
        if cat.eye_colour2 != None:
            new_sprite.blit(sprites.sprites['eyes2' + cat.eye_colour2 + cat_sprite], (0, 0))
        for scar in cat.scars:
            if scar in scars1:
                new_sprite.blit(sprites.sprites['scars' + scar + cat_sprite], (0, 0))
            if scar in scars3:
                new_sprite.blit(sprites.sprites['scars' + scar + cat_sprite], (0, 0))

        # draw line art
        if cat.shading:
            new_sprite.blit(sprites.sprites['shaders' + cat_sprite], (0, 0), special_flags=pygame.BLEND_RGB_MULT)
            new_sprite.blit(sprites.sprites['lighting' + cat_sprite], (0, 0))

        if not cat.dead:
            new_sprite.blit(sprites.sprites['lines' + cat_sprite], (0, 0))
        elif cat.df:
            new_sprite.blit(sprites.sprites['lineartdf' + cat_sprite], (0, 0))
        elif cat.dead:
            new_sprite.blit(sprites.sprites['lineartdead' + cat_sprite], (0, 0))
        # draw skin and scars2
        blendmode = pygame.BLEND_RGBA_MIN
        new_sprite.blit(sprites.sprites['skin' + cat.skin + cat_sprite], (0, 0))
        for scar in cat.scars:
            if scar in scars2:
                new_sprite.blit(sprites.sprites['scars' + scar + cat_sprite], (0, 0), special_flags=blendmode)

        # draw accessories        
        if cat.accessory in plant_accessories:
            new_sprite.blit(sprites.sprites['acc_herbs' + cat.accessory + cat_sprite], (0, 0))
        elif cat.accessory in wild_accessories:
            new_sprite.blit(sprites.sprites['acc_wild' + cat.accessory + cat_sprite], (0, 0))
        elif cat.accessory in collars:
            new_sprite.blit(sprites.sprites['collars' + cat.accessory + cat_sprite], (0, 0))

        # Apply fading fog
        if cat.opacity <= 97 and not cat.prevent_fading and game.settings["fading"]:
            
            stage = "0"
            if 80 >= cat.opacity > 45:
                # Stage 1
                stage = "1"
            elif cat.opacity <= 45:
                # Stage 2
                stage = "2"

            new_sprite.blit(sprites.sprites['fademask' + stage + cat_sprite], 
                            (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

            if cat.df:
                temp = sprites.sprites['fadedf' + stage + cat_sprite].copy()
                temp.blit(new_sprite, (0, 0))
                new_sprite = temp
            else:
                temp = sprites.sprites['fadestarclan' + stage + cat_sprite].copy()
                temp.blit(new_sprite, (0, 0))
                new_sprite = temp

    except (TypeError, KeyError):
        traceback.print_exc()
        # Placeholder image
        new_sprite = image_cache.load_image(f"sprites/error_placeholder.png").convert_alpha().copy()
        
    # reverse, if assigned so
    if cat.reverse:
        new_sprite = pygame.transform.flip(new_sprite, True, False)

    cat.sprite = new_sprite

# ---------------------------------------------------------------------------- #
#                                     OTHER                                    #
# ---------------------------------------------------------------------------- #

def is_iterable(y):
    try:
        0 in y
    except TypeError:
        return False


def get_text_box_theme(themename=""):
    """Updates the name of the theme based on dark or light mode"""
    if game.settings['dark mode']:
        if themename == "":
            return "#default_dark"
        else:
            return themename + "_dark"
    else:
        if themename == "":
            return "text_box"
        else:
            return themename





