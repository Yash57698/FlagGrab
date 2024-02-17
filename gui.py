import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('FlagGrab')
clock = pygame.time.Clock()

lines = []
circles = []
boundaries = []

def parse_input(input_string):
    tuples_list = []
    tuples_str = input_string.split("),(")
    for tuple_str in tuples_str:
        tuple_str = tuple_str.replace("(", "").replace(")", "")
        pair_str = tuple_str.split(",")
        pair = tuple(int(x) for x in pair_str)
        tuples_list.append(pair)
    return tuples_list

lines = parse_input(lines) 
circles = parse_input(circles) 
boundaries = parse_input(boundaries) 
def draw_boundaries(boundaries):
        for i in range(len(boundaries)):
            pygame.draw.line(screen,"Red",boundaries[i][0],boundaries[i][1],10)

def draw_lines(lines):
    for i in range(len(lines)):
        pygame.draw.line(screen,"black",lines[i][0],lines[i][1],2)

def draw_circles(circles):
    for i in range(len(circles)):
        pygame.draw.circle(screen,"black",circles[i][0],circles[i][1],2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("white")
    draw_lines(lines)
    draw_circles(circles)
    draw_boundaries(boundaries)
    pygame.display.update()
    clock.tick(60)