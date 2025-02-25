import pygame
from states.state_manager import StateManager
import variables

pygame.init()

# create the display window
screen = pygame.display.set_mode((variables.window_width, variables.window_height), pygame.FULLSCREEN)

# set the window title
pygame.display.set_caption('My Pygame Window')

# create state manager
state_manager = StateManager()

# main game loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # close the window
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                state_manager.change_state("level1")
            if event.key == pygame.K_2:
                state_manager.change_state("menu")
        
        # handle events within the page
        state_manager.handle_events(event, state_manager)
    
    # update state manager
    state_manager.update(mouse_x, mouse_y)
    state_manager.draw(screen, mouse_x, mouse_y)

    # update the display
    pygame.display.flip()

# quit Pygame
pygame.quit()
