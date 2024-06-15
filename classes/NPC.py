from classes.Spritesheet import Spritesheet
from classes.Dialogue import Dialogue

class NPC:
    def __init__(self, position, spriteloc, dialogue: None):
        self.position = position
        self.spritesheet = Spritesheet("assets/sprites/mlp1-sheet.png", 48)
        self.image = self.spritesheet.getImageAt(spriteloc)
        
        if dialogue is None:
            self.dialogue = None
        else:
            self.dialogue = Dialogue(dialogue)
            
    def render(self, screen, cam):
        centeredpos = [i - 24 for i in self.position]
        screen.blit(self.image, (cam.toCameraPos(centeredpos)))