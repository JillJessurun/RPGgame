from pages.menu import MenuState
from pages.level1 import Level1State
from pages.level2 import Level2State

class StateManager:
    def __init__(self):
        self.states = {
            "menu": MenuState(),
            "level1": Level1State(),
            "level2": Level2State()
        }
        self.current_state = self.states["menu"]

    def change_state(self, scene_name):
        self.current_state = self.states[scene_name]

    def handle_events(self, event, state_manager):
        next_scene = self.current_state.handle_events(event, state_manager)
        if next_scene:
            if next_scene == "quit":
                return False
            self.change_state(next_scene)
        return True

    def update(self, mouse_x, mouse_y):
        self.current_state.update(mouse_x, mouse_y)

    def draw(self, screen, mouse_x, mouse_y):
        self.current_state.draw(screen, mouse_x, mouse_y)