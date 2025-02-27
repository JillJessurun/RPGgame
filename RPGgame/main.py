import pygame
from states.state_manager import StateManager
import variables

pygame.init()

# create the display window
screen = pygame.display.set_mode((variables.window_width, variables.window_height), pygame.FULLSCREEN)

# set proper window size based on monitor
window_x, window_y = pygame.display.get_window_size()
variables.window_width = window_x
variables.window_height = window_y

# set the window title
pygame.display.set_caption('My Pygame Window')

# create state manager
state_manager = StateManager()

# main game loop
while variables.running:
    screen.fill((0, 0, 0))
    
    # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # get keys
    keys = pygame.key.get_pressed()
    
    # page event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            variables.running = False  # close the window
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                state_manager.change_state("menu")
            if event.key == pygame.K_2:
                state_manager.change_state("level1")
            if event.key == pygame.K_3:
                state_manager.change_state("level2")
        
        # handle events within the page
        state_manager.handle_events(event, state_manager)
    
    # update page state manager
    state_manager.update(mouse_x, mouse_y)
    state_manager.draw(screen, mouse_x, mouse_y)
    
    # update the display
    pygame.display.flip()

# quit Pygame
pygame.quit()
