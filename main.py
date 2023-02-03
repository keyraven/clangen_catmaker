import sys
import os
directory = os.path.dirname(__file__)
if directory:
    os.chdir(directory)
import pygame
import scripts.global_vars as global_vars
import scripts.game_structure.game_essentials
from scripts.game_structure.game_essentials import *
import scripts.screens.all_screens


clock = pygame.time.Clock()

# MAIN GAME LOOK
while True:
    time_delta = clock.tick(60) / 1000.0

    game.all_screens[game.current_screen].on_use()
    for event in pygame.event.get():
        game.all_screens[game.current_screen].handle_event(event)

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        # F2 turns toggles visual debug mode for pygame_gui, allowed for easier bug fixes.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                if not global_vars.MANAGER.visual_debug_active:
                    global_vars.MANAGER.set_visual_debug_mode(True)
                else:
                    global_vars.MANAGER.set_visual_debug_mode(False)

        global_vars.MANAGER.process_events(event)

    global_vars.MANAGER.update(time_delta)

    if game.switch_screens:
        game.all_screens[game.last_screen_forupdate].exit_screen()
        game.all_screens[game.current_screen].screen_switches()
        game.switch_screens = False

    scripts.global_vars.MANAGER.draw_ui(global_vars.SCREEN)
    pygame.display.update()
