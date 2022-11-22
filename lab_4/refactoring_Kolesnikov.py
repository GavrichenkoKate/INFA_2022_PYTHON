import pygame
from pygame.draw import *

def Jdun(position_x, position_y, scale):   # мишутка
	pygame.draw.line(sc, (0, 0, 0), [position_x + (3 * scale), position_y + 4 * scale], [position_x + (12 * scale), position_y - 2 * scale], 3)
	pygame.draw.aaline(sc, (0, 0, 0), [position_x + (12 * scale), position_y - 2 * scale], [position_x + (12 * scale), position_y + 7 * scale])
	# удочка

	pygame.draw.ellipse(sc, (200, 200, 200), (position_x + 2 * scale, position_y - scale, 3.5 * scale, 2 * scale))
	pygame.draw.ellipse(sc, (0, 0, 0), (position_x + 2 * scale, position_y - scale, 3.5 * scale, 2 * scale), 1)
	# голова

	pygame.draw.ellipse(sc, (200, 200, 200), (position_x, position_y, 4 * scale, 8 * scale))
	pygame.draw.ellipse(sc, (0, 0, 0), (position_x, position_y, 4 * scale, 8 * scale), 1)
	# тело

	pygame.draw.ellipse(sc, (200, 200, 200), (position_x + (2 * scale), position_y + 5.5 * scale, 4 * scale, 3 * scale))
	pygame.draw.ellipse(sc, (0, 0, 0), (position_x + (2 * scale), position_y + 5.5 * scale, 4 * scale, 3 * scale), 1)
	# бедро

	pygame.draw.ellipse(sc, (200, 200, 200), (position_x + (4 * scale), position_y + 7.75 * scale, 3 * scale, scale))
	pygame.draw.ellipse(sc, (0, 0, 0), (position_x + (4 * scale), position_y + 7.75 * scale, 3 * scale, scale), 1)
	# нога

	pygame.draw.ellipse(sc, (200, 200, 200), (position_x + (3 * scale), position_y + 2 * scale, 2.5 * scale, 1.5 * scale))
	pygame.draw.ellipse(sc, (0, 0, 0), (position_x + (3 * scale), position_y + 2 * scale, 2.5 * scale, 1.5 * scale), 1)
	# рука

	pygame.draw.circle(sc, (200, 200, 200), (position_x + 3 * scale, position_y - 0.75 * scale), 0.5 * scale)
	pygame.draw.circle(sc, (0, 0, 0), (position_x + 3 * scale, position_y - 0.75 * scale), 0.5 * scale, 1)
	# ухо

	pygame.draw.circle(sc, (0, 0, 0), (position_x + 4 * scale, position_y - 0.25 * scale), 0.1 * scale)
	pygame.draw.circle(sc, (0, 0, 0), (position_x + 5 * scale, position_y - 0.25 * scale), 0.1 * scale)
	# глаза

	pygame.draw.aaline(sc, (0, 0, 0), [position_x + 4 * scale, position_y + 0.25 * scale], [position_x + 5 * scale, position_y + 0.25 * scale])
	# рот

def Riba(position_x, position_y, scale):
	pygame.draw.polygon(sc, (200, 100, 100), [[position_x + 2 * scale, position_y], [position_x + scale, position_y - 1.5 * scale], [position_x - scale, position_y - 1.5 * scale]])
	pygame.draw.aalines(sc, (0, 0, 0), True, [[position_x + 2 * scale, position_y], [position_x + scale, position_y - 1.5 * scale], [position_x - scale, position_y - 1.5 * scale]])
	# плавники_1
	pygame.draw.polygon(sc, (200, 100, 100), [[position_x + 2 * scale, position_y], [position_x + scale, position_y + 1.5 * scale], [position_x - scale, position_y + 1.5 * scale]])
	pygame.draw.aalines(sc, (0, 0, 0), True, [[position_x + 2 * scale, position_y], [position_x + scale, position_y + 1.5 * scale], [position_x - scale, position_y + 1.5 * scale]])
	# плавники_2
	pygame.draw.polygon(sc, (200, 100, 100), [[position_x + 2 * scale, position_y], [position_x + 4 * scale, position_y + 1.5 * scale], [position_x + 3 * scale, position_y + 1.5 * scale]])
	pygame.draw.aalines(sc, (0, 0, 0), True, [[position_x + 2 * scale, position_y], [position_x + 4 * scale, position_y + 1.5 * scale], [position_x + 3 * scale, position_y + 1.5 * scale]])
	# плавники_3

	pygame.draw.polygon(sc, (150, 255, 150), [[position_x, position_y], [position_x + 2 * scale, position_y + scale], [position_x + 4 * scale, position_y], [position_x + 2 * scale, position_y - scale]])
	pygame.draw.aalines(sc, (0, 0, 0), True, [[position_x, position_y], [position_x + 2 * scale, position_y + scale], [position_x + 4 * scale, position_y], [position_x + 2 * scale, position_y - scale]])
	# тело

	pygame.draw.polygon(sc, (150, 255, 150), [[position_x, position_y], [position_x - 2 * scale, position_y + scale], [position_x - 2 * scale, position_y - scale]])
	pygame.draw.aalines(sc, (0, 0, 0), True, [[position_x, position_y], [position_x - 2 * scale, position_y + scale], [position_x - 2 * scale, position_y - scale]])
	# хвост

	pygame.draw.circle(sc, (0, 0, 0), (position_x + 3 * scale, position_y), 0.5 * scale)
	# глаз


def Prorub(position_x, position_y, scale):
	pygame.draw.ellipse(sc, (200, 200, 200), (position_x, position_y, 2 * scale, scale))
	pygame.draw.ellipse(sc, (0, 0, 0), (position_x + 0.2 * scale, position_y + 0.2 * scale, 1.6 * scale, 0.8 * scale))

def Mnogorib(position_x, position_y, scale):
	Riba(position_x, position_y, scale)
	Riba(position_x + 4 * scale, position_y + scale, scale)
	Riba(position_x + 8 * scale, position_y - scale, scale)
	Riba(position_x, position_y - 9.5 * scale, scale / 2)
	Riba(position_x + 2 * scale, position_y - 8.5 * scale, scale / 2)
	Riba(position_x + 4 * scale, position_y - 9 * scale, scale / 2)
	

pygame.init()

FPS = 30
sc = pygame.display.set_mode((400, 600))

pygame.draw.rect(sc, (100, 100, 200), (0, 0, 400, 200))   # небо
pygame.draw.circle(sc, (200, 200, 50), (300, 100), 50)    # Солнце
pygame.draw.rect(sc, (200, 200, 200), (0, 200, 400, 400))  # лёд

Prorub(295, 265, 23)
Mnogorib(300, 300, 5)
Jdun(200, 200, 10)

Prorub(242.5, 397.5, 34.5)
Mnogorib(250, 450, 7.5)
Jdun(100, 300, 15)

Prorub(490, 530, 46)
Mnogorib(500, 600, 10)
Jdun(300, 400, 20)

Prorub(162.5, 597.5, 34.5)
Mnogorib(170, 650, 7.5)
Jdun(20, 500, 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()