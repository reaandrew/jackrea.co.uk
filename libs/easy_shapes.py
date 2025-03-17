import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Easy Shapes (Thick Lines)")
clock = pygame.time.Clock()

# Set global pen thickness here
PEN_THICKNESS = 4  # Adjust this for thicker or thinner lines

def setup():
    screen.fill((255, 255, 255))
    pygame.display.flip()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def draw_circle(x, y, radius, color="black", speed=360):
    points = []
    for angle in range(0, 361, 2):
        rad = math.radians(angle)
        px = x + radius * math.cos(rad)
        py = y + radius * math.sin(rad)
        points.append((px, py))

    for i in range(1, len(points)):
        handle_events()
        pygame.draw.line(screen, pygame.Color(color), points[i - 1], points[i], PEN_THICKNESS)
        pygame.display.flip()
        clock.tick(speed)

def draw_rectangle(x, y, width, height, color="black", speed=500):
    points = [(x, y), (x + width, y), (x + width, y + height), (x, y + height), (x, y)]
    for i in range(4):
        start, end = points[i], points[i + 1]
        for t in range(0, 101, 4):
            handle_events()
            px = start[0] + (end[0] - start[0]) * t / 100
            py = start[1] + (end[1] - start[1]) * t / 100
            pygame.draw.line(screen, pygame.Color(color), start, (px, py), PEN_THICKNESS)
            pygame.display.flip()
            clock.tick(speed)
        pygame.draw.line(screen, pygame.Color(color), start, end, PEN_THICKNESS)

def draw_square(x, y, size, color="black", speed=500):
    draw_rectangle(x, y, size, size, color, speed)

def draw_triangle(x, y, size, color="black", speed=500):
    points = [(x, y), (x - size // 2, y + size), (x + size // 2, y + size), (x, y)]
    for i in range(3):
        start, end = points[i], points[i + 1]
        for t in range(0, 101, 4):
            handle_events()
            px = start[0] + (end[0] - start[0]) * t / 100
            py = start[1] + (end[1] - start[1]) * t / 100
            pygame.draw.line(screen, pygame.Color(color), start, (px, py), PEN_THICKNESS)
            pygame.display.flip()
            clock.tick(speed)
        pygame.draw.line(screen, pygame.Color(color), start, end, PEN_THICKNESS)

def draw_star(x, y, size, color="black", speed=600):
    points = []
    for i in range(11):
        angle = math.pi / 5 * i
        r = size if i % 2 == 0 else size / 2
        px = x + r * math.cos(angle - math.pi / 2)
        py = y + r * math.sin(angle - math.pi / 2)
        points.append((px, py))

    for i in range(10):
        start, end = points[i], points[i + 1]
        for t in range(0, 101, 10):
            handle_events()
            px = start[0] + (end[0] - start[0]) * t / 100
            py = start[1] + (end[1] - start[1]) * t / 100
            pygame.draw.line(screen, pygame.Color(color), start, (px, py), PEN_THICKNESS)
            pygame.display.flip()
            clock.tick(speed)
        pygame.draw.line(screen, pygame.Color(color), start, end, PEN_THICKNESS)

def finish():
    while True:
        handle_events()
        clock.tick(60)
