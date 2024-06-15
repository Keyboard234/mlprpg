from classes.Spritesheet import Spritesheet
from classes.Animation import Animation

from functions import Calculator

class Player:
    def __init__(self, position):
        self.position = position
        self.x_vel = 0
        self.y_vel = 0

        self.health = 100

        self.can_interact = (False, None)
        self.in_dialogue = (False, None)
        
        self.moving = False
        self.direction = {"up": False, "down": False, "left": False, "right": True}
        
        self.movinganims = {"up": [(6, 3), (7, 3), (8, 3), (7, 3)], "down": [(6, 0), (7, 0), (8, 0), (7, 0)], "left": [(6, 1), (7, 1), (8, 1), (7, 1)], "right": [(6, 2), (7, 2), (8, 2), (7, 2)]}
        self.idlesprites = {"up": (7, 3), "down": (7, 0), "left": (7, 1), "right": (7, 2)}
        
        self.sprite_locations = [(6, 0)]
        self.spritesheet = Spritesheet("assets/sprites/mlp1-sheet.png", 48)
        
        for dir in self.idlesprites:
            self.idlesprites[dir] = self.spritesheet.getImageAt(self.idlesprites[dir])

        for dir in self.movinganims:
            self.movinganims[dir] = [self.spritesheet.getImageAt(self.movinganims[dir][i]) for i, _ in enumerate(self.movinganims[dir])]
            self.movinganims[dir] = Animation(self.movinganims[dir], 30, 8)
            
    def startmoving(self, new_vel):
        self.moving = True
        self.x_vel = new_vel[0]
        self.y_vel = new_vel[1]
    def stopmoving(self):
        self.moving = False
        self.x_vel = 0
        self.y_vel = 0
    def cleardirection(self):
        for dir in self.direction:
            self.direction[dir] = False
    def finddirection(self):
        for dir in self.direction:
            if self.direction[dir]:
                return dir
    def update(self):
        if self.in_dialogue[0]:
            self.in_dialogue[1].nextChar()
            return
        
        self.position[0] += self.x_vel
        self.position[1] += self.y_vel
        
        if self.y_vel > 0:
            self.cleardirection()
            self.direction["down"] = True
        elif self.y_vel < 0:
            self.cleardirection()
            self.direction["up"] = True
            
        if self.x_vel > 0:
            self.cleardirection()
            self.direction["right"] = True
        elif self.x_vel < 0:
            self.cleardirection()
            self.direction["left"] = True
    def checkForInteractions(self, NPCs):
        self.can_interact = (False, None)
        for npc in NPCs:
            if Calculator.dist(self.position, npc.position) < 75:
                if npc.dialogue != None:
                    self.can_interact = (True, npc)
    def interact(self):
        if self.can_interact[0] and not self.in_dialogue[0]:
            if self.can_interact[1].dialogue != None:
                self.in_dialogue = (True, self.can_interact[1].dialogue)
                self.in_dialogue[1].start()
        elif self.in_dialogue[0]:
            self.in_dialogue[1].nextText()
            if self.in_dialogue[1].isfinished:
                self.in_dialogue = (False, None)
    def render(self, screen, cam):
        direction = self.finddirection()
        myimage = None
        if self.moving and not self.in_dialogue[0]:
            self.movinganims[direction].nextFrame()
            myimage = self.movinganims[direction].getCurrentFrame()
        else:
            myimage = self.idlesprites[direction]

        centeredpos = [i - 24 for i in self.position]
        screen.blit(myimage, (cam.toCameraPos(centeredpos)))
