import pygame
import variables
from objects.component import Component
import random

class Enemy(Component):
    def __init__(self):
        super().__init__()
        
        # constants
        self.ENEMY_SPEED = 20
        self.SPAWNER_FOUND = False
        self.IS_MOVING = False
        self.ANIMATION_SPEED = 10
        self.ENEMY_SCALE = 90
        self.NUM_SPRITES = 4
        self.SPRITE_WIDTH = 115.5 # sheet is 462 pixels and 4 sprites -> 462 / 4
        self.SPRITE_HEIGHT = 111 # sheet height
        
        self.direction_indexes = []
        self.enemy_indexes = []
        
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
            
        # animation variables
        self.current_frame = 0
        self.animation_timer = 0
        
    def update(self, mouse_x, mouse_y, map):
        # update animation
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
                        self.enemy_indexes = [row_index, tile_index]
        
        if not self.IS_MOVING:
            # iterate trough every tile
            for row_index, row in enumerate(map.game_map):
                for tile_index, tile in enumerate(row):
                    # check if enemy pos found
                    if self.enemy_indexes[0] == row_index and self.enemy_indexes[1] == tile_index: # enemy pos found
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
                        self.moving_right = True # right
                        #print("move right")
                    else:
                        self.moving_left = True # left
                        #print("move left")
                else:
                    # Move on the y-axis
                    if self.enemy_pos_y > self.direction_pos_y:
                        self.moving_up = True # up
                        #print("move up")
                    else:
                        self.moving_down = True # down
                        #print("move down")
                self.direction_assigned = True
            else:
                # move based on direction
                if self.moving_up:
                    # temp arrays for wallfinding
                    current_row_index = [self.enemy_indexes[0], self.enemy_indexes[1]]
                    next_wall_indexes = [] # spot to save next wall
                    counter = 0

                    # find wall
                    while next_wall_indexes == []:
                        if map.game_map[current_row_index[0]][current_row_index[1]] == 1:
                            # next wall found!
                            next_wall_indexes = [current_row_index[0],current_row_index[1]]
                            break
                        else:
                            # increment and go to next row to find wall
                            counter = counter + 1
                            current_row_index = [self.enemy_indexes[0]-counter, self.enemy_indexes[1]]     
                            
                            # EERSTE RONDE (BOOLEAN MAKEN VOOR OF HET DE EERSTE RONDE IS) TELLEN TOT 3
                            # BIJ 3 SLA JE DE CURRENT INDEXES OP
                            # DAT WORDT DE TARGET IPV DE NEXT ONE
                            #
                            # NEXT_WALlLINDEXES = LSDKFJSDJFKLFJKLJDLFJSDF
                            # BREAK
                            
                    # next wall coordinates
                    next_wall_y = map.grid_row * next_wall_indexes[0]
                    next_wall_x = map.grid_column * next_wall_indexes[1]
                    
                    # check when enemy and next wall collide
                    if (self.enemy_pos_y < next_wall_y):
                        self.enemy_pos_y = next_wall_y
                        self.enemy_indexes = [next_wall_indexes[0]+1, next_wall_indexes[1]] # +1 because enemy must not be in the wall but next to the wall
                        
                        # end
                        self.moving_up = False
                        self.moving_down = False
                        self.moving_left = False
                        self.moving_right = False
                        
                        self.IS_MOVING = False
                        self.direction_assigned = False
                        
                    # move
                    else: self.enemy_pos_y -= self.ENEMY_SPEED

                if self.moving_down:
                    # temp arrays for wallfinding
                    current_row_index = [self.enemy_indexes[0], self.enemy_indexes[1]]
                    next_wall_indexes = [] # spot to save next wall
                    counter = 0

                    # find wall
                    while next_wall_indexes == []:
                        if map.game_map[current_row_index[0]][current_row_index[1]] == 1:
                            # next wall found!
                            next_wall_indexes = [current_row_index[0],current_row_index[1]]
                        else:
                            # increment and go to next row to find wall
                            counter = counter + 1
                            current_row_index = [self.enemy_indexes[0]+counter, self.enemy_indexes[1]]     
                    
                    # next wall coordinates
                    next_wall_y = (map.grid_row * next_wall_indexes[0])-map.grid_row # minus one gridrow to get hitbox of wall
                    next_wall_x = map.grid_column * next_wall_indexes[1]
                    
                    # check when enemy and next wall collide
                    if (self.enemy_pos_y > next_wall_y):
                        self.enemy_pos_y = next_wall_y
                        self.enemy_indexes = [next_wall_indexes[0]-1, next_wall_indexes[1]]
                        
                        # end
                        self.moving_up = False
                        self.moving_down = False
                        self.moving_left = False
                        self.moving_right = False
                        
                        self.IS_MOVING = False
                        self.direction_assigned = False
                        
                    # move
                    else: self.enemy_pos_y += self.ENEMY_SPEED
                  
                if self.moving_left:
                    # temp arrays for wallfinding
                    current_row_index = [self.enemy_indexes[0], self.enemy_indexes[1]]
                    next_wall_indexes = [] # spot to save next wall
                    counter = 0

                    # find wall
                    while next_wall_indexes == []:
                        if map.game_map[current_row_index[0]][current_row_index[1]] == 1:
                            # next wall found!
                            next_wall_indexes = [current_row_index[0],current_row_index[1]]
                        else:
                            # increment and go to next row to find wall
                            counter = counter + 1
                            current_row_index = [self.enemy_indexes[0], self.enemy_indexes[1]-counter]     
                    
                    # next wall coordinates
                    next_wall_y = self.enemy_pos_y
                    next_wall_x = map.grid_column * next_wall_indexes[1]
                    
                    #print("ENEMY INDEXES: ", self.enemy_indexes[0], ", ", self.enemy_indexes[1])
                    #print ("NEXT WALL INDEXES: ", next_wall_indexes[0], ", ", next_wall_indexes[1])
                    #print("ENEMY COORDINATES: ", self.enemy_pos_x, ", ", self.enemy_pos_y)
                    #print ("NEXT WALL COORDINATES: ", next_wall_x, ", ", next_wall_y)
                    
                    # check when enemy and next wall collide
                    if (self.enemy_pos_x < next_wall_x):
                        self.enemy_pos_x = next_wall_x
                        self.enemy_indexes = [next_wall_indexes[0], next_wall_indexes[1]+1]
                        
                        # end
                        self.moving_up = False
                        self.moving_down = False
                        self.moving_left = False
                        self.moving_right = False
                        
                        self.IS_MOVING = False
                        self.direction_assigned = False
                        
                    # move
                    else: self.enemy_pos_x -= self.ENEMY_SPEED
                        
                if self.moving_right:
                    # temp arrays for wallfinding
                    current_row_index = [self.enemy_indexes[0], self.enemy_indexes[1]]
                    next_wall_indexes = [] # spot to save next wall
                    counter = 0
                    
                    # find wall
                    while next_wall_indexes == []:
                        if map.game_map[current_row_index[0]][current_row_index[1]] == 1:
                            # next wall found!
                            next_wall_indexes = [current_row_index[0],current_row_index[1]]
                        else:
                            # increment and go to next row to find wall
                            counter = counter + 1
                            current_row_index = [self.enemy_indexes[0], self.enemy_indexes[1]+counter]
                            
                    # next wall coordinates
                    next_wall_y = self.enemy_pos_y
                    next_wall_x = (map.grid_column * next_wall_indexes[1])-map.grid_column # - one gridcolumn to get the hitbox of the wall
                    
                    #print("ENEMY COORDINATES: ", self.enemy_pos_x, ", ", self.enemy_pos_y)
                    #print ("NEXT WALL COORDINATES: ", next_wall_x, ", ", next_wall_y)
                    
                    # check when enemy and next wall collide
                    if (self.enemy_pos_x > next_wall_x):
                        self.enemy_pos_x = next_wall_x
                        self.enemy_indexes = [next_wall_indexes[0], next_wall_indexes[1]-1]
                        
                        # end
                        self.moving_up = False
                        self.moving_down = False
                        self.moving_left = False
                        self.moving_right = False
                        
                        self.IS_MOVING = False
                        self.direction_assigned = False
                        
                    # move
                    else: self.enemy_pos_x += self.ENEMY_SPEED
                #else:
                    #print("stand still")
                    #self.IS_MOVING = False
                    #self.direction_assigned = False

    def draw(self, screen,  camera_x, camera_y, game_map):
        screen.blit(self.frames[self.current_frame], (self.enemy_pos_x, self.enemy_pos_y))
        
        # draw hitbox
        #enemy_hitbox_vertical = pygame.Rect(self.enemy_pos_x + self.SPRITE_WIDTH/3, self.enemy_pos_y, self.SPRITE_WIDTH/3, self.SPRITE_HEIGHT)
        #pygame.draw.rect(screen, variables.WHITE, enemy_hitbox_vertical, 1)