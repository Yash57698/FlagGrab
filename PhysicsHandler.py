import Player
import gui
import numpy as np

timestep = 0.1
collisionCoeff = 1

def tickPlayer(player):
    player.acc = (0,5)
    player.pos =  np.array(player.pos) +  (np.array(player.vel) * timestep) + ((0.5)*timestep*timestep)* np.array(player.acc)
    player.vel =  np.array(player.vel) + np.array(player.acc)*timestep
    # print("vel" , player.vel , "pos" , player.pos)

def HandleCollsion(map , players):
    for boundary in map.get_boundaries():
        for player in players:
            pt1,pt2 = boundary
            v1 = np.array(player.pos) - np.array(pt1)
            v2 = np.array(player.pos) - np.array(pt2)
            norm = np.linalg.norm(np.array(pt2) - np.array(pt1))
            lcap = (np.array(pt2)-np.array(pt1))/norm
            c = np.linalg.norm(np.cross(lcap,v1))

            if(np.dot(v1,lcap)* np.dot(v2,lcap) <= 0 and c<gui.PlayerRadius):
                d = gui.PlayerRadius - c
                ncap = np.cross(lcap,np.array([0,0,1]))
                ncap = np.resize(ncap , (2))
                if(np.dot(v1,ncap) < 0):
                    ncap = -ncap
                player.pos = player.pos + d*ncap

                player.vel = (-collisionCoeff * np.dot(np.array(player.vel),ncap)) * ncap + (np.dot(player.vel,lcap)* lcap)


