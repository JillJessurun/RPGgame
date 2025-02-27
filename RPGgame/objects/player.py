import pygame
import variables
from objects.component import Component

class Player(Component):
    def __init__(self):
        super().__init__()
        
        # constants
        self.PLAYER_RADIUS = 50
        self.PLAYER_HITBOX = 40
        self.PLAYER_HITBOX_OFFSET = 5
        self.PLAYER_SPEED = 4
        self.START_OFFSET = 30
        
        # sprite
        self.player_image = pygame.image.load("RPGgame/images/ghost.png").convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (self.PLAYER_RADIUS, self.PLAYER_RADIUS))

        # player position
        self.player_x = int(variables.window_width/2)
        self.player_y = int(variables.window_height/2-self.START_OFFSET)
        
        # moving variables
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
    def collision_check(self, game_map, old_x, old_y):
        for row_index, row in enumerate(game_map.game_map):
            for tile_index, tile in enumerate(row):
                # calculate x and y positions of the tile
                tile_x = game_map.grid_column * tile_index
                tile_y = game_map.grid_row * row_index
                
                # rects for collission check
                player_rect = pygame.Rect(self.player_x+self.PLAYER_HITBOX_OFFSET, self.player_y+self.PLAYER_HITBOX_OFFSET, self.PLAYER_HITBOX, self.PLAYER_HITBOX)
                tile_rect = pygame.Rect(tile_x-game_map.POSITION_OFFSET, tile_y-game_map.POSITION_OFFSET, game_map.grid_column+game_map.DRAWING_OFFSET, game_map.grid_row+game_map.DRAWING_OFFSET)
                
                # Check for collision
                if tile == 1:
                    if player_rect.colliderect(tile_rect):
                        #print("Collision detected!")
                        self.player_x, self.player_y = old_x, old_y  # Revert position

    def update(self, mouse_x, mouse_y, game_map):
        # Boundary checks
        #self.player_x = max(self.PLAYER_RADIUS, min(variables.window_width - self.PLAYER_RADIUS, self.player_x))
        #self.player_y = max(self.PLAYER_RADIUS, min(variables.window_height - self.PLAYER_RADIUS, self.player_y))
        
        # Store the old position
        old_x, old_y = self.player_x, self.player_y
        
        if self.moving_left:
            self.player_x -= self.PLAYER_SPEED
        elif self.moving_right:
            self.player_x += self.PLAYER_SPEED
        elif self.moving_up:
            self.player_y -= self.PLAYER_SPEED
        elif self.moving_down:
            self.player_y += self.PLAYER_SPEED
            
        self.collision_check(game_map, old_x, old_y)

    def draw(self, screen,  camera_x, camera_y):
        #pygame.draw.rect(screen, variables.COLOUR_PLAYER, (self.player_x - camera_x, self.player_y - camera_y, self.PLAYER_RADIUS, self.PLAYER_RADIUS))
        screen.blit(self.player_image, (self.player_x - camera_x, self.player_y - camera_y))


    def handle_events(self, event, state_manager):
        # movement logic
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.moving_left = True
                self.moving_right = False
                self.moving_up = False
                self.moving_down = False

            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.moving_right = True
                self.moving_left = False
                self.moving_up = False
                self.moving_down = False

            elif event.key in (pygame.K_UP, pygame.K_w):
                self.moving_up = True
                self.moving_down = False
                self.moving_left = False
                self.moving_right = False

            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.moving_down = True
                self.moving_up = False
                self.moving_left = False
                self.moving_right = False

        elif event.type == pygame.KEYUP:
            # check which key was released and disable its movement
            if event.key in (pygame.K_LEFT, pygame.K_a):
                self.moving_left = False
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                self.moving_right = False
            elif event.key in (pygame.K_UP, pygame.K_w):
                self.moving_up = False
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.moving_down = False

            # Check if another movement key is still held
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.moving_left = True
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.moving_right = True
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.moving_up = True
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.moving_down = True

