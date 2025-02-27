import pygame
import variables
from objects.component import Component

class Enemy(Component):
    def __init__(self):
        super().__init__()
        
        # constants
        self.ANIMATION_SPEED = 10
        self.ENEMY_SCALE = 90
        self.NUM_SPRITES = 4
        self.SPRITE_WIDTH = 115.5 # sheet is 462 pixels and 4 sprites -> 462 / 4
        self.SPRITE_HEIGHT = 111 # sheet height
        
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
        
    def update(self, mouse_x, mouse_y, game_map):
        # Update animation
        self.animation_timer += 1
        if self.animation_timer >= self.ANIMATION_SPEED:
            self.current_frame = (self.current_frame + 1) % self.NUM_SPRITES
            self.animation_timer = 0
        
    def draw(self, screen,  camera_x, camera_y, game_map):
        # Draw the current frame
        screen.blit(self.frames[self.current_frame], (game_map.enemy_spawn_x, game_map.enemy_spawn_y))