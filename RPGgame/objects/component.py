class Component:
    def __init__(self):
        self.running = True

    def update(self, mouse_x, mouse_y, game_map):
        pass

    def draw(self, screen):
        pass

    def handle_events(self, event, state_manager):
        pass