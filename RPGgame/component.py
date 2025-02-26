class Component:
    def __init__(self):
        self.running = True

    def update(self, mouse_x, mouse_y):
        pass

    def draw(self, screen, mouse_x, mouse_y):
        pass

    def handle_events(self, event, state_manager):
        pass