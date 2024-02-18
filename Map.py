class Map:
    boundaries = [((100,50),(900,50)) , ((100,50),(100,450)) , ((100,450),(900,450)) , ((900,50),(900,450))]
    obstacles = []

    def get_boundaries(self):
        return self.boundaries
    
    def get_walls(self):
        return self.boundaries

    def get_obstacles(self):
        return self.obstacles
    