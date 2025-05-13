# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	pygame.init()

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	keepGameRunning = True
	while keepGameRunning:

		pygame.Surface.fill(screen, (0, 0, 0))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGameRunning = False
				return

	pygame.display.flip()


if __name__ == "__main__":
	main()
