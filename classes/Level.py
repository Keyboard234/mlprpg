import pygame
import xml.etree.ElementTree as ET

class Level:
    def __init__(self):
        self.tilesize = 32

    def loadTileImgs(self):
        tileimgs = []
        tilesheetpath = "assets/tileimg/tilesheet.tsx"
        tree = ET.parse(tilesheetpath)
        root = tree.getroot()
        for child in root:
            if child.tag == "tile":
                for img in child:
                    tileimg = pygame.image.load("assets/tileimg/" + img.attrib["source"])
                    tileimg = pygame.transform.scale(tileimg, (self.tilesize, self.tilesize))
                    tileimgs.append(pygame.Surface.convert(tileimg))
        self.tileimgs = tileimgs

    def loadMap(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        for child in root:
            if child.tag == "layer":
                self.width = int(child.attrib["width"])
                self.height = int(child.attrib["height"])
                data = child[0].text.replace("\n", "")
                data = [int(i) for i in data.split(",")]
                self.tiles = data

    def posToTile(self, pos):
        pass
    def tileToIndex(self, tilepos):
        return tilepos[0] + tilepos[1]*self.width
    def render(self, display, camera):
        
        x = 0
        y = 0
        for tile in self.tiles:
            tile_pos = camera.toCameraPos([x*self.tilesize, y*self.tilesize])
            display.blit(self.tileimgs[tile-1], tile_pos)
            x += 1
            if x == self.width:
                x = 0
                y += 1