import pygame
from states.state import State
import variables

# define colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 255)
DARK_BLUE = (0, 51, 153)

# button properties
button_rect = pygame.Rect(variables.window_width // 2 - 75, variables.window_height // 2 - 25, 150, 50)  # (x, y, width, height)
font = pygame.font.Font(None, 36)  # Default font, size 36
button_text = font.render("Click Me", True, (0, 0, 0))

class MenuState(State):
    def __init__(self):
        super().__init__()

    def update(self, mouse_x, mouse_y):
        # Logic for the main menu
        pass

    def draw(self, screen, mouse_x, mouse_y):
        screen.fill((0, 0, 255))  # Blue background for the menu
        
        # Change button color if hovered
        button_color = DARK_BLUE if button_rect.collidepoint(mouse_x, mouse_y) else BLUE

        # Draw button
        pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
        screen.blit(button_text, (button_rect.x + 35, button_rect.y + 10))

    def handle_events(self, event, state_manager):
        if event.type == pygame.QUIT:
            variables.running = False  # Exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "gameplay"  # Transition to gameplay state
            if event.key == pygame.K_ESCAPE:
                variables.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click
            if button_rect.collidepoint(event.pos):
                state_manager.change_state("level1")