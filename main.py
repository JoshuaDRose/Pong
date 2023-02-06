""" This is a docstring"""
import sys
import pygame

from paddle import Paddle
from ball import Ball

# Initialize pygame
pygame.init()

# Window dimensions
width = 700
height = 400

# Background color
background_color = (0, 0, 0)

#Creating a display
screen = pygame.display.set_mode((width, height), 0, 32)

# Exit flag for game-loop
running = True

paddle_a = Paddle(0, 0)
paddle_b = Paddle(width-paddle_a.rect.width, 0)

clock = pygame.time.Clock()
fps = 60
ball = Ball(width // 2, height // 2, 15)


# Start game-loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_a.rect.y -= 1

            elif event.key == pygame.K_s:
                paddle_a.rect.y += 1

            if event.key == pygame.K_UP:
                print ("Up pressed")

            elif event.key == pygame.K_DOWN:
                print ("Down pressed")


    # fill the screen
    screen.fill(background_color)

    screen.blit(paddle_a.image, paddle_a.rect)
    screen.blit(paddle_b.image, paddle_b.rect)

    ball.draw(screen)
    ball.update()

    if ball.rect.y +50 > height:
        ball.direction.y = -1
    elif ball.rect.y  <= 0:
        ball.direction.y = 1
    if ball.rect.x + 50 > width:
        ball.direction.x = -1
    elif ball.rect.x <= 0:
        ball.direction.x = 1

    if pygame.Rect.colliderect(ball.rect, paddle_a.rect):
        ball.direction.x = 1
    elif pygame.Rect.colliderect(ball.rect, paddle_b.rect):
        ball.direction.x = -1


    # Update the display
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()
