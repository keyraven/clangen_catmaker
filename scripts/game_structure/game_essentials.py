
# G A M E
class Game():
    # Keeping track of various last screen for various purposes
    last_screen_forupdate = 'start screen'
    last_screen_forProfile = 'list screen'

    # Sort-type
    current_screen = "start screen"

    all_screens = {}
    cur_events = {}


    def __init__(self, current_screen='start screen'):
        self.current_screen = current_screen
        self.switch_screens = False


game = Game()
