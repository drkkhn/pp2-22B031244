import pygame
import pytmx
from settings import TILE_SIZE

class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha = True)
        self.tmx_data = tm
        self.width = tm.width * TILE_SIZE
        self.height = tm.height * TILE_SIZE

    def render(self, surface):
        tile_image = self.tmx_data.get_tile_image_by_gid
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tile_image(gid)
                    if tile:
                        tile = pygame.transform.scale(tile, (TILE_SIZE, TILE_SIZE))
                        surface.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA).convert_alpha()
        self.render(temp_surface)
        return temp_surface
