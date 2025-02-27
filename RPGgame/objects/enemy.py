import pygame
import variables
from objects.component import Component
import random

class Enemy(Component):
    def __init__(self):
        super().__init__()
        
        # constants
        self.ENEMY_SPEED = 3
        self.SPAWNER_FOUND = False
        self.IS_MOVING = False
        self.ANIMATION_SPEED = 10
        self.ENEMY_SCALE = 90
        self.NUM_SPRITES = 4
        self.SPRITE_WIDTH = 115.5 # sheet is 462 pixels and 4 sprites -> 462 / 4
        self.SPRITE_HEIGHT = 111 # sheet height
        
        self.direction_indexes = []
        
        # enemy and direction positions
        self.enemy_pos_x = 0
        self.enemy_pos_y = 0
        self.direction_pos_x = 0
        self.direction_pos_y = 0
        
        # directions booleans
        self.direction_assigned = False
        self.moving_down = False
        self.moving_up = False
        self.moving_left = False
        self.moving_right = False
        
        # save new tile after moving
        self.new_current_tile = 0
        
        # sprite
        self.sprite_sheet = pygame.image.load("RPGgame/images/enemy_sheet.png").convert_alpha()
        
        # Extract individual frames
        self.frames = []
        for i in range(self.NUM_SPRITES):
            frame = self.sprite_sheet.subsurface((i * self.SPRITE_WIDTH, 0, self.SPRITE_WIDTH, self.SPRITE_HEIGHT))
            frame = pygame.transform.rotate(frame, 90)
            self.frames.append(frame)
            
        # Animation variables
        self.current_frame = 0
        self.animation_timer = 0
        
    def update(self, mouse_x, mouse_y, map):
        # Update animation
        self.animation_timer += 1
        if self.animation_timer >= self.ANIMATION_SPEED:
            self.current_frame = (self.current_frame + 1) % self.NUM_SPRITES
            self.animation_timer = 0
            
        # set enemy position to the spawner on the map
        if not self.SPAWNER_FOUND:
            for row_index, row in enumerate(map.game_map):
                for tile_index, tile in enumerate(row):
                    if tile == 2:
                        # spawner found, set x and y
                        self.enemy_pos_x = map.grid_column * tile_index
                        self.enemy_pos_y = map.grid_row * row_index
                        self.SPAWNER_FOUND = True
                        
                        # set initial direction index to current index
                        self.direction_indexes = [row_index, tile_index]
        
        if not self.IS_MOVING:
            # iterate trough every tile
            for row_index, row in enumerate(map.game_map):
                for tile_index, tile in enumerate(row):
                    # check if enemy pos found
                    if self.direction_indexes[0] == row_index and self.direction_indexes[1] == tile_index:
                        # create arrays with the row and tile index per direction from the current enemy position
                        
                        # left
                        left = [row_index, tile_index-1]
                        # right
                        right = [row_index, tile_index+1]
                        # up
                        up = [row_index-1,tile_index]
                        # down
                        down = [row_index+1, tile_index]
                        
                        # create lists of the direction indexes
                        direction_list = [left, right, up, down]
                        ground_list = []
                        
                        # add ground tiles to ground list
                        for direction in direction_list:
                            if map.game_map[direction[0]][direction[1]] == 0:
                                # it is ground!
                                ground_list.append(direction)
                        
                        # random direction
                        direction = random.choice(ground_list)
                        
                        # set target indexes
                        self.direction_indexes = direction
                            
                        # define the x and y of the final direction tile
                        self.direction_pos_y = map.grid_row * self.direction_indexes[0]
                        self.direction_pos_x = map.grid_column * self.direction_indexes[1]
                                                
                        # set ismoving
                        self.IS_MOVING = True
                        
                        break
                    
                        
        else: # move enemy
            if not self.direction_assigned:
                if self.enemy_pos_x != self.direction_pos_x:
                    # Move on the x-axis
                    if self.enemy_pos_x < self.direction_pos_x:
                        self.moving_right = True
                    if self.enemy_pos_x > self.direction_pos_x:
                        self.moving_left = True
                if self.enemy_pos_y != self.direction_pos_y:
                    # Move on the y-axis
                    if self.enemy_pos_y > self.direction_pos_y:
                        self.moving_up = True
                    if self.enemy_pos_y < self.direction_pos_y:
                        self.moving_down = True
                self.direction_assigned = True
            else:
                # move based on direction
                if self.moving_up:
                    self.enemy_pos_y -= min(self.ENEMY_SPEED, self.enemy_pos_y - self.direction_pos_y)  # Move up
                    if self.enemy_pos_y <= self.direction_pos_y:  # Check if target reached
                        self.IS_MOVING = False
                        self.moving_up = False
                        self.direction_assigned = False

                elif self.moving_down:
                    self.enemy_pos_y += min(self.ENEMY_SPEED, self.direction_pos_y - self.enemy_pos_y)  # Move down 
                    if self.enemy_pos_y >= self.direction_pos_y:  # Check if target reached
                        self.IS_MOVING = False
                        self.moving_down = False
                        self.direction_assigned = False

                        
                elif self.moving_left:
                   self.enemy_pos_x -= min(self.ENEMY_SPEED, self.enemy_pos_x - self.direction_pos_x)  # Move left
                   if self.enemy_pos_x <= self.direction_pos_x: # check whether target reached
                        # target reached
                        self.IS_MOVING = False
                        self.moving_left = False
                        self.direction_assigned = False
                        
                elif self.moving_right:
                    self.enemy_pos_x += min(self.ENEMY_SPEED, self.direction_pos_x - self.enemy_pos_x)  # Move right
                    if self.enemy_pos_x >= self.direction_pos_x: # check whether target reached
                        # target reached
                        self.IS_MOVING = False
                        self.moving_right = False
                        self.direction_assigned = False
                else:
                    self.IS_MOVING = False
                    self.direction_assigned = False

    def draw(self, screen,  camera_x, camera_y, game_map):
        screen.blit(self.frames[self.current_frame], (self.enemy_pos_x, self.enemy_pos_y))