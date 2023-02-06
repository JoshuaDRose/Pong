import sys
import pygame

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
				
			elif event.key == pygame.K_UP:
				print ("Up pressed")

			elif event.key == pygame.K_DOWN:
				print ("Down pressed")
				
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				print ("A released")

			elif event.key == pygame.K_s:
				print ("S released")
				
			elif event.key == pygame.K_UP:
				print ("Up released")

			elif event.key == pygame.K_DOWN:
				print ("Down released")
			
	# Update the display
	pygame.display.update()
pygame.quit()
sys.exit()
