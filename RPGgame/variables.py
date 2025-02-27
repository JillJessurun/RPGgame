import pygame

pygame.init()

# universal colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# other colours
COLOUR_START_BUTTON = (0, 0, 0)
COLOUR_START_BUTTON_HOVER = (0, 51, 153)
#COLOUR_WALL = (30, 14, 1)
COLOUR_GROUND = (87, 65, 32)
COLOUR_WALL = (24, 15, 2)
COLOUR_PLAYER = (255, 119, 0)

# state of the application
running = True

# window width and height
window_width, window_height = pygame.display.Info().current_w, pygame.display.Info().current_h

def round_corners(image, radius):
    """Applies rounded corners to an image."""
    mask = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    mask.fill((0, 0, 0, 0))
    
    # draw a rounded rectangle
    pygame.draw.rect(mask, (255, 255, 255, 255), (0, 0, *image.get_size()), border_radius=radius)
    
    # apply mask to image
    image = image.copy()
    image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    
    return image