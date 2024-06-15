class Camera:
    def __init__(self, pos):
        self.pos = pos
    def moveTo(self, newpos):
        self.pos = newpos
    def toCameraPos(self, pos):
        return (pos[0]-self.pos[0]+240, pos[1]-self.pos[1]+240)
