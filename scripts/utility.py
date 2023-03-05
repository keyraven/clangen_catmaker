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


    # THE SPRITE UPDATE
    # draw colour & style
    new_sprite = pygame.Surface((sprites.size, sprites.size), pygame.HWSURFACE | pygame.SRCALPHA)

    try:
        if cat.pelt.name not in ['Tortie', 'Calico']:
            if cat.age == 'elder' or (cat.pelt.length == 'long' and cat.age not in ['kitten', 'adolescent']):
                new_sprite.blit(
                    sprites.sprites[cat.pelt.sprites[1] + 'extra' + cat.pelt.colour + str(cat.age_sprites[cat.age])],
                    (0, 0))
            else:
                new_sprite.blit(sprites.sprites[cat.pelt.sprites[1] + cat.pelt.colour + str(cat.age_sprites[cat.age])],
                                (0, 0))
        else:
            if cat.age == 'elder' or (cat.pelt.length == 'long' and cat.age not in ['kitten', 'adolescent']):
                # Base Coat
                new_sprite.blit(
                    sprites.sprites[cat.tortiebase + 'extra' + cat.pelt.colour + str(cat.age_sprites[cat.age])],
                    (0, 0))

                # Create the patch image
                patches = sprites.sprites[
                    cat.tortiepattern + 'extra' + cat.tortiecolour + str(cat.age_sprites[cat.age])].copy()
                patches.blit(sprites.sprites["tortiemask" + cat.pattern + str(cat.age_sprites[cat.age] + 9)],
                             (0, 0),
                             special_flags=pygame.BLEND_RGBA_MULT
                             )

                # Add patches onto cat.
                new_sprite.blit(patches, (0, 0))
            else:
                # Base Coat
                new_sprite.blit(
                    sprites.sprites[cat.tortiebase + cat.pelt.colour + str(cat.age_sprites[cat.age])],
                    (0, 0))

                # Create the patch image
                if cat.tortiepattern == "Single":
                    tortie_pattern = "SingleColour"
                else:
                    tortie_pattern = cat.tortiepattern

                patches = sprites.sprites[
                    tortie_pattern + cat.tortiecolour + str(cat.age_sprites[cat.age])].copy()
                patches.blit(sprites.sprites["tortiemask" + cat.pattern + str(cat.age_sprites[cat.age])], (0, 0),
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
            if cat.age == 'elder' or (cat.pelt.length == 'long' and cat.age not in ['kitten', 'adolescent']):
                white_patches = sprites.sprites['whiteextra' + cat.white_patches + str(cat.age_sprites[cat.age])].copy()
            else:
                white_patches = sprites.sprites['white' + cat.white_patches + str(cat.age_sprites[cat.age])].copy()

            # Apply tint to white patches.
            if cat.white_patches_tint != "none" and cat.white_patches_tint in Sprites.white_patches_tints[
                "tint_colours"]:
                tint = pygame.Surface((50, 50)).convert_alpha()
                tint.fill(tuple(Sprites.white_patches_tints["tint_colours"][cat.white_patches_tint]))
                white_patches.blit(tint, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

            new_sprite.blit(white_patches, (0, 0))

        # draw eyes & scars1
        if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
            new_sprite.blit(
                sprites.sprites['eyesextra' + cat.eye_colour +
                                str(cat.age_sprites[cat.age])], (0, 0))
            if cat.eye_colour2 != None:
                new_sprite.blit(
                sprites.sprites['eyes2extra' + cat.eye_colour2 +
                                str(cat.age_sprites[cat.age])], (0, 0))
            for scar in cat.scars:
                if scar in scars1:
                    new_sprite.blit(
                        sprites.sprites['scarsextra' + scar + str(cat.age_sprites[cat.age])],
                        (0, 0)
                    )
                if scar in scars3:
                    new_sprite.blit(
                        sprites.sprites['scarsextra' + scar + str(cat.age_sprites[cat.age])],
                        (0, 0)
                    )
            
        else:
            new_sprite.blit(
                sprites.sprites['eyes' + cat.eye_colour +
                                str(cat.age_sprites[cat.age])], (0, 0))
            if cat.eye_colour2 != None:
                new_sprite.blit(
                sprites.sprites['eyes2' + cat.eye_colour2 +
                                str(cat.age_sprites[cat.age])], (0, 0))
            for scar in cat.scars:
                if scar in scars1:
                    new_sprite.blit(
                        sprites.sprites['scars' + scar + str(cat.age_sprites[cat.age])],
                        (0, 0)
                    )
                if scar in scars3:
                    new_sprite.blit(
                        sprites.sprites['scars' + scar + str(cat.age_sprites[cat.age])],
                        (0, 0)
                    )
            

        # draw line art
        if cat.shading:
            if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
                new_sprite.blit(
                    sprites.sprites['shaders' +
                                    str(cat.age_sprites[cat.age] + 9)],
                    (0, 0),
                    special_flags=pygame.BLEND_RGB_MULT)
                new_sprite.blit(
                    sprites.sprites['lighting' +
                                    str(cat.age_sprites[cat.age] + 9)],
                    (0, 0))
            else:
                new_sprite.blit(
                    sprites.sprites['shaders' +
                                    str(cat.age_sprites[cat.age])], (0, 0),
                    special_flags=pygame.BLEND_RGB_MULT)
                new_sprite.blit(
                    sprites.sprites['lighting' +
                                    str(cat.age_sprites[cat.age])],
                    (0, 0))


        if not cat.dead:
            if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
                new_sprite.blit(
                    sprites.sprites['lines' +
                                    str(cat.age_sprites[cat.age] + 9)],
                    (0, 0))
            else:
                new_sprite.blit(
                    sprites.sprites['lines' + str(cat.age_sprites[cat.age])],
                    (0, 0))
        elif cat.df:
            if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
                new_sprite.blit(
                    sprites.sprites['lineartdf' +
                                    str(cat.age_sprites[cat.age] + 9)],
                    (0, 0))
            else:
                new_sprite.blit(
                    sprites.sprites['lineartdf' +
                                    str(cat.age_sprites[cat.age])], (0, 0))
        elif cat.dead:
            if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
                new_sprite.blit(
                    sprites.sprites['lineartdead' +
                                    str(cat.age_sprites[cat.age] + 9)],
                    (0, 0))
            else:
                new_sprite.blit(
                    sprites.sprites['lineartdead' +
                                    str(cat.age_sprites[cat.age])], (0, 0))
        # draw skin and scars2
        blendmode = pygame.BLEND_RGBA_MIN
        if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
            new_sprite.blit(
                sprites.sprites['skinextra' + cat.skin +
                                str(cat.age_sprites[cat.age])], (0, 0))
            for scar in cat.scars:
                if scar in scars2:
                    new_sprite.blit(sprites.sprites['scarsextra' + scar +
                                                    str(cat.age_sprites[cat.age])], (0, 0), special_flags=blendmode)

        else:
            new_sprite.blit(
                sprites.sprites['skin' + cat.skin +
                                str(cat.age_sprites[cat.age])], (0, 0))
            for scar in cat.scars:
                if scar in scars2:
                    new_sprite.blit(sprites.sprites['scars' + scar +
                                                    str(cat.age_sprites[cat.age])], (0, 0), special_flags=blendmode)

        # draw accessories        
        if cat.pelt.length == 'long' and cat.age not in ["kitten", "adolescent"] or cat.age == 'elder':
            if cat.accessory in plant_accessories:
                new_sprite.blit(
                    sprites.sprites['acc_herbsextra' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
            elif cat.accessory in wild_accessories:
                new_sprite.blit(
                    sprites.sprites['acc_wildextra' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
            elif cat.accessory in collars:
                new_sprite.blit(
                    sprites.sprites['collarsextra' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
            elif cat.accessory in collars:
                new_sprite.blit(
                    sprites.sprites['collarsextra' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
        else:
            if cat.accessory in plant_accessories:
                new_sprite.blit(
                    sprites.sprites['acc_herbs' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
            elif cat.accessory in wild_accessories:
                new_sprite.blit(
                    sprites.sprites['acc_wild' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
            elif cat.accessory in collars:
                new_sprite.blit(
                    sprites.sprites['collars' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
            elif cat.accessory in collars:
                new_sprite.blit(
                    sprites.sprites['collars' + cat.accessory +
                                    str(cat.age_sprites[cat.age])], (0, 0))
    except (TypeError, KeyError):
        print(f"ERROR: Failed to load cat ID #{cat}'s sprite:\n", traceback.format_exc())

        # Placeholder image
        new_sprite.blit(
            image_cache.load_image(f"sprites/faded/faded_adult.png").convert_alpha(),
            (0, 0)
        )

    # reverse, if assigned so
    if cat.reverse:
        new_sprite = pygame.transform.flip(new_sprite, True, False)

    # Apply opacity
    if cat.opacity < 100 and not cat.prevent_fading and game.settings["fading"]:
        new_sprite = apply_opacity(new_sprite, cat.opacity)

    # apply
    cat.sprite = new_sprite
    cat.big_sprite = pygame.transform.scale(
        new_sprite, (sprites.new_size, sprites.new_size))
    cat.large_sprite = pygame.transform.scale(
        cat.big_sprite, (sprites.size * 3, sprites.size * 3))



def apply_opacity(surface, opacity):
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = list(surface.get_at((x, y)))
            pixel[3] = int(pixel[3] * opacity/100)
            surface.set_at((x,y), tuple(pixel))
    return surface
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





