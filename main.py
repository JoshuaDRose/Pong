import pygame, sys

#Initiating Pygame
pygame.init()

#Window dimensions
WinSize = (700,400)

#Creating a display
Screen = pygame.display.set_mode(WinSize, 0, 32)

#Events loop.
while True:
	for event in pygame.event.get():
		
		#Quits Pygame
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
