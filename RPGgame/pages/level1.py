import pygame
from states.state import State
from player import Player
import variables

class Level1State(State):
    def __init__(self):
        super().__init__()
        self.player = Player()

    def update(self, mouse_x, mouse_y):
        # component updates
        self.player.update(mouse_x, mouse_y)

    def draw(self, screen, mouse_x, mouse_y):
        screen.fill(variables.BLACK)
        
        # component drawings
        self.player.draw(screen, mouse_x, mouse_y)

    def handle_events(self, event, state_manager):
        if event.type == pygame.QUIT:
            self.running = False  # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_manager.change_state("menu")
                
        # component events
        self.player.handle_events(event, state_manager)