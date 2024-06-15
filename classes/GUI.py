import pygame

class GUI:
    def __init__(self, screen, fontfilepath):
        self.screen = screen
        self.font = pygame.font.Font(fontfilepath, 14)
        
    def render(self, player):
        if player.can_interact[0]:
            pygame.draw.rect(self.screen, (10, 0, 10), pygame.Rect(50, 380, 50, 50))
        if player.in_dialogue[0]:
            dialogue = player.in_dialogue[1]
            pygame.draw.rect(self.screen, (10, 0, 10), pygame.Rect(0, 350, 480, 130))
            dialoguesurf = self.font.render(dialogue.texts[dialogue.text_index][:dialogue.char_index+1], True, (255, 255, 255))
            self.screen.blit(dialoguesurf, (50, 380))
