import pygame
from states.state import State

class Level2State(State):
    def __init__(self):
        super().__init__()

    def update(self, mouse_x, mouse_y):
        # Logic for gameplay
        pass

    def draw(self, screen, mouse_x, mouse_y):
        screen.fill((0, 255, 0))  # Green background for gameplay
        # Draw game elements here

    def handle_events(self, event, state_manager):
        if event.type == pygame.QUIT:
            self.running = False  # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_manager.change_state("menu")