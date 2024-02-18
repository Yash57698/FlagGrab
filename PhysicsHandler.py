import Player
timestep = 0.01


def tickPlayer(player):
    player.acc = (0,0.1)
    player.pos = player.vel * timestep + (0.5)*player.acc*timestep*timestep
