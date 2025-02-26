import pygame
from states.state import State
from objects.player import Player
import variables
from map import Map

class Level1State(State):
    def __init__(self):
        super().__init__()
        
        # map
        self.map = Map()
        
        # player
        self.player = Player()
        
        # camera
        self.camera_x, self.camera_y = 0, 0

    def update(self, mouse_x, mouse_y):
        new_x, new_y = self.player.player_x, self.player.player_y
        
        # update player
        self.player.update(mouse_x, mouse_y, self.map)
        #self.map.update(self.player)

    def draw(self, screen, mouse_x, mouse_y):
        screen.fill(variables.COLOUR_GROUND)
        
        # component drawings
        self.map.draw(screen, self.camera_x, self.camera_y, self.player)
        self.player.draw(screen, self.camera_x, self.camera_y)

    def handle_events(self, event, state_manager):
        if event.type == pygame.QUIT:
            self.running = False  # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state_manager.change_state("menu")
                
        # component events
        self.player.handle_events(event, state_manager)