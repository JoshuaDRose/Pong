import sys
import pygame

from paddle import Paddle
from ball import Ball

# Initialize pygame
pygame.init()

# Window dimensions
window_size = [700, 400]

# Background color
background_color = (0, 0, 0)

#Creating a display
screen = pygame.display.set_mode(window_size, 0, 32)

# Exit flag for game-loop
running = True

paddle_a = Paddle(0, 0)
paddle_b = Paddle(0, 0)


# Start game-loop
while running:
	screen.fill(background_color)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print ("A pressed")

			elif event.key == pygame.K_s:
				print ("S pressed")
				
			if event.key == pygame.K_UP:
				print ("Up pressed")

			elif event.key == pygame.K_DOWN:
				print ("Down pressed")
			
	# Update the display
	pygame.display.update()
pygame.quit()
sys.exit()
