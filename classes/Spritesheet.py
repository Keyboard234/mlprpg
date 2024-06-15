import pygame

class Spritesheet:
    def __init__(self, filepath: str, tilesize: int):
        self.filepath = filepath
        self.tilesize = tilesize
        self.sheetimg = pygame.image.load(filepath).convert_alpha()
    def getImageAt(self, tile_pos):
        tile_x, tile_y = tile_pos
        rect = pygame.Rect(tile_x*self.tilesize, tile_y*self.tilesize, self.tilesize, self.tilesize)
        imgsurf = pygame.Surface(rect.size, pygame.SRCALPHA)
        imgsurf.blit(self.sheetimg, (0, 0), rect)
        return imgsurf