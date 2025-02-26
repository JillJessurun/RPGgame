import pygame
import variables
from component import Component

class Player(Component):
    def __init__(self):
        super().__init__()
        
        # constants
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PLAYER_RADIUS = 20
        self.PLAYER_SPEED = 2

        # player position
        self.player_x, self.player_y = variables.window_width // 2, variables.window_height // 2
        
        # moving variables
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self, mouse_x, mouse_y):
        # Boundary checks
        self.player_x = max(self.PLAYER_RADIUS, min(variables.window_width - self.PLAYER_RADIUS, self.player_x))
        self.player_y = max(self.PLAYER_RADIUS, min(variables.window_height - self.PLAYER_RADIUS, self.player_y))
        
        if self.moving_left:
            self.player_x -= self.PLAYER_SPEED
        if self.moving_right:
            self.player_x += self.PLAYER_SPEED
        if self.moving_up:
            self.player_y -= self.PLAYER_SPEED
        if self.moving_down:
            self.player_y += self.PLAYER_SPEED

    def draw(self, screen, mouse_x, mouse_y):
        pygame.draw.circle(screen, self.BLUE, (self.player_x, self.player_y), self.PLAYER_RADIUS)

    def handle_events(self, event, state_manager):
        # Movement logic
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.moving_left = True
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                self.moving_right = True
            if event.key in (pygame.K_UP, pygame.K_w):
                self.moving_up = True
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.moving_left = False
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                self.moving_right = False
            if event.key in (pygame.K_UP, pygame.K_w):
                self.moving_up = False
            if event.key in (pygame.K_DOWN, pygame.K_s):
                self.moving_down = False