
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


