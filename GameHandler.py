from Player import Player
from Map import Map
import pygame
import gui
import time
import PhysicsHandler

class GameHandler:
    map = None
    screen = None
    clock = None
    Players = []

    def __init__(self,map, players):
        self.map = map
        self.Players = players
        pygame.init()
        self.screen = pygame.display.set_mode((1000,500))
        pygame.display.set_caption('FlagGrab')
        self.clock = pygame.time.Clock()

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.screen.fill("white")
        
        for player in self.Players:
            gui.draw_players(player)

        gui.draw_boundaries(self.map.get_boundaries())
        pygame.display.update()

        

    def StartGame(self):
        while True:
            self.draw()


            for player in self.Players:
                PhysicsHandler.tickPlayer(player)
            
            PhysicsHandler.HandleCollsion(self.map,self.Players)
            time.sleep(0.02)
            # self.clock.tick(60)

m = Map()
ps = [Player((200,200),(10,0))]

handler = GameHandler(m ,ps)
handler.draw()

handler.StartGame()