class Dialogue:
    def __init__(self, texts: tuple[str]):
        self.texts = texts
        self.iswriting = False
        self.isfinished = True
        self.text_index = 0
        self.char_index = 0
    def start(self):
        self.iswriting = True
        self.isfinished = False
    def reset(self):
        self.char_index = 0
        self.text_index = 0
        self.isfinished = True
    def nextText(self):
        if self.iswriting:
            self.char_index = len(self.texts[self.text_index])-1
            self.iswriting = False
        else:
            if self.text_index == len(self.texts)-1:
                self.reset()
            else:
                self.text_index += 1
                self.char_index = 0
                self.iswriting = True
    def nextChar(self):
        if self.iswriting:
            self.char_index += 1
            if self.char_index == len(self.texts[self.text_index])-1:
                self.iswriting = False
