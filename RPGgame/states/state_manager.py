from pages.menu import MenuState
from pages.level1 import Level1State

class StateManager:
    def __init__(self):
        self.states = {
            "menu": MenuState(),
            "level1": Level1State()
        }
        self.current_scene = self.states["menu"]

    def change_state(self, scene_name):
        self.current_scene = self.states[scene_name]

    def handle_events(self, event, state_manager):
        next_scene = self.current_scene.handle_events(event, state_manager)
        if next_scene:
            if next_scene == "quit":
                return False
            self.change_state(next_scene)
        return True

    def update(self, mouse_x, mouse_y):
        self.current_scene.update(mouse_x, mouse_y)

    def draw(self, screen, mouse_x, mouse_y):
        self.current_scene.draw(screen, mouse_x, mouse_y)