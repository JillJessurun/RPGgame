import pygame

pygame.init()

# universal colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# other colours
COLOUR_START_BUTTON = (0, 102, 255)
COLOUR_START_BUTTON_HOVER = (0, 51, 153)
COLOUR_WALL = (30, 14, 1)
COLOUR_GROUND = (61, 35, 12)
COLOUR_PLAYER = (255, 119, 0)

# state of the application
running = True

# window width and height
window_width, window_height = pygame.display.Info().current_w, pygame.display.Info().current_h