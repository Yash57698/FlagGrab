import Player
import Map

class GameHandler:
    map = None
    Players = []

    def __init__(self,map, players):
        self.map = map
        self.Players = players

