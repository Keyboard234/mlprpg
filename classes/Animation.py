class Animation:
    def __init__(self, images: list, fps, rate):
        self.images = images
        self.index = 0
        self.fps = fps
        self.timer = 0
        self.rate = rate
    def nextFrame(self):
        self.timer += 1
        if self.timer > self.fps / self.rate:
            self.timer = 0
            
            self.index += 1
            if self.index > len(self.images)-1:
                self.index = 0
    def getCurrentFrame(self):
        return self.images[self.index]