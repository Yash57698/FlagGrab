from Player import Player
from Map import Map
import pygame
import gui

class GameHandler:
    map = None
    screen = None
    clock = None
    Players = []

    def __init__(self,map, players):
        self.map = map
        self.Players = players
        pygame.init()
        screen = pygame.display.set_mode((1000,500))
        pygame.display.set_caption('FlagGrab')
        clock = pygame.time.Clock()

    def draw(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill("white")
            
            gui.draw_circles()
            gui.draw_boundaries(map.get_boundaries())
            pygame.display.update()
            self.clock.tick(60)

m = Map()
ps = [Player(0,0)]

handler = GameHandler(m ,ps)

