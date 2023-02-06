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
while True:
	screen.fill(background_color)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	# Update the display
	pygame.display.update()
pygame.quit()
sys.exit()
