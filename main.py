import sys
import math

import pygame

from classes.Camera import Camera
from classes.Level import Level
from classes.NPC import NPC
from classes.Player import Player
from classes.GUI import GUI

import data.dialogues

DISPLAY = pygame.display.set_mode((480, 480))
pygame.display.set_caption('mlprpg')

def render(cam, level, player, NPCs, gui):
    level.render(DISPLAY, cam)
    for i in NPCs:
        i.render(DISPLAY, cam)
    player.render(DISPLAY, cam)
    gui.render(player)

def update(player, cam, NPCs):
    player.stopmoving()

    pressed_keys = pygame.key.get_pressed()
    
    new_x_vel = 0
    new_y_vel = 0

    if pressed_keys[pygame.K_w] and not pressed_keys[pygame.K_s]:
        new_y_vel = -5
    if pressed_keys[pygame.K_s] and not pressed_keys[pygame.K_w]:
        new_y_vel = 5
    if pressed_keys[pygame.K_a] and not pressed_keys[pygame.K_d]:
        new_x_vel = -5
    if pressed_keys[pygame.K_d] and not pressed_keys[pygame.K_a]:
        new_x_vel = 5
    
    if (new_x_vel, new_y_vel) != (player.x_vel, player.y_vel):
        player.startmoving((new_x_vel, new_y_vel))
    
    player.checkForInteractions(NPCs)

    player.update()
    cam.moveTo(player.position)

def main():
    pygame.init()
    MAX_FPS = 30
    #gametimer = 0

    NPCs = [NPC([500, 500], (1, 0), data.dialogues.DIALOGUE_PINKIE), NPC([700, 500], (1, 5), None)]
    
    playerstartpos = [240, 240]
    newlevel = Level()
    newlevel.loadTileImgs()
    newlevel.loadMap("assets/map.tmx")
    player = Player(playerstartpos)
    gui = GUI(DISPLAY, "assets/font/PressStart2P-Regular.ttf")
    cam = Camera(playerstartpos)
    
    clock = pygame.time.Clock()
    while True:
        clock.tick(MAX_FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    player.interact()
        
        #gametimer += 1
        #if gametimer > MAX_FPS:
        #    gametimer = 0

        update(player, cam, NPCs)
        render(cam, newlevel, player, NPCs, gui)
        pygame.display.update()

if __name__ == "__main__":
    main()
