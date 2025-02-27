import pygame
from states.state import State
import variables

class MenuState(State):
    def __init__(self):
        super().__init__()
        
        # button properties
        self.button_rect = pygame.Rect(variables.window_width // 2 - 75, variables.window_height // 2 - 25, 130, 50)  # (x, y, width, height)
        self.font = pygame.font.Font(None, 36)  # Default font, size 36
        self.button_text = self.font.render("Start", True, (255, 255, 255))

    def update(self, mouse_x, mouse_y):
        # Logic for the main menu
        pass

    def draw(self, screen, mouse_x, mouse_y):
        screen.fill(variables.WHITE)
        
        # Change button color if hovered
        button_color = variables.COLOUR_START_BUTTON_HOVER if self.button_rect.collidepoint(mouse_x, mouse_y) else variables.COLOUR_START_BUTTON

        # Draw button
        pygame.draw.rect(screen, button_color, self.button_rect, border_radius=10)
        screen.blit(self.button_text, (self.button_rect.x + 35, self.button_rect.y + 10))

    def handle_events(self, event, state_manager):
        if event.type == pygame.QUIT:
            variables.running = False  # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "gameplay"  # Transition to gameplay state
            if event.key == pygame.K_ESCAPE:
                variables.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click
            if self.button_rect.collidepoint(event.pos):
                state_manager.change_state("level1")