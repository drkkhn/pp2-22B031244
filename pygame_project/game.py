import sys
import pygame
from pytmx.util_pygame import load_pygame
from settings import TILE_SIZE, WIDTH, HEIGHT
from tiled_map import TiledMap

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

# Initializing pygame engine
pygame.init()

# initializing display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# loading tmx file
tm = TiledMap('./graphics/tmx/jungle_level.tmx')
tmx_data = load_pygame('./graphics/tmx/jungle_level.tmx')
sprite_group = pygame.sprite.Group()
# enemies_group = pygame.sprite.Group()

# cycle through all layers
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, surf in layer.tiles():
             pos = (x * 16, y * 16)
             Tile(pos = pos, surf = surf, groups = sprite_group)
        
# doors_obj_layer = tmx_data.get_layer_by_name("Doors")
# enemies_obj_layer = tmx_data.get_layer_by_name("Enemies")

#for enemy_obj in enemies_obj_layer:
#    pos = enemy_obj.x, enemy_obj.y
#    if enemy_obj.image:
#        Tile(pos = pos, surf = enemy_obj.image, groups = enemies_group)
# get layers
#print(tmx_data.layers) # get all layers
#for layer in tmx_data.visible_layers:
#    print(layer)

#print(tmx_data.layernames) # getting all layers as dictionaries
#print(tmx_data.get_layer_by_name('ground')) # getting layer by name

#for obj in tmx_data.objectgroups:
#    print(obj) # getting each object layer

# get tiles
# ground_layer = tmx_data.get_layer_by_name('Ground')

#print(dir(ground_layer))
#for x, y, surf in ground_layer.tiles():
#    print(x * 16, y * 16, surf)

# print(ground_layer.data) # get layer data
# print(ground_layer.name) # getting object name
# print(ground_layer.id) # getting layer id

# get objects
# enemies_obj_layer = tmx_data.get_layer_by_name("Enemies")
# print(dir(enemies_obj_layer))
# for enemy_obj in enemies_obj_layer:
#    if enemy_obj.name == "Demon":
#        print(enemy_obj, enemy_obj.x, enemy_obj.y, enemy_obj.image)

#initializing clock object to control time and framerate
clock = pygame.time.Clock()

# creating a image surface object
bg_list = []
for i in range(1, 6):
    bg_surf = pygame.image.load(f'./graphics/jungle_assets/parallax background/plx-{i}.png')
    bg_surf = pygame.transform.scale(bg_surf, (WIDTH, HEIGHT))
    bg_list.append(bg_surf)


# creating a text surface

# creating an image surface for a main character
player_surf = pygame.image.load('./graphics/adventurer/Individual Sprites/adventurer-idle-03.png').convert_alpha()
player_surf = pygame.transform.scale(player_surf, (64, 64))
player_init_pos_x = 50
player_init_pos_y = 500
player_rect = player_surf.get_rect(midbottom = (player_init_pos_x, player_init_pos_y))

 

# Initializing infinite loop to run the game
while True:  
    # Checking for any player input in event loop
    for event in pygame.event.get():
        # checking whether player pressed quit button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_surf, (0, 0))
    for bg_surf in bg_list:
        screen.blit(bg_surf, (0, 0))
    
    screen.blit(tm.make_map(), (0, 0))
    #sprite_group.draw(screen)
    # enemies_group.draw(screen)
    # player_rect.left += 1
    screen.blit(player_surf, player_rect)
    # draw all elements
    # update all events
    pygame.display.update()
